"""Streamlit UI components for JobMate AI."""

import requests
import streamlit as st
from config import MODEL
from database import (
    get_latest_quiz_result,
    get_quiz_history,
    get_recommendation,
    get_total_quiz_attempts,
    save_quiz_result,
)
from quiz_data import QUIZ_LEVELS, ROLE_QUIZZES
from services import (
    build_plan_prompt,
    call_ollama,
    detect_skills,
    extract_resume_text,
)


def render_placement_analyzer():
    """Render the resume upload, skill gap detection, and AI study plan section."""
    st.header("1. Your Placement Goal")
    col1, col2 = st.columns(2)

    with col1:
        target_role = st.text_input(
            "Target job role",
            value=st.session_state.get("target_role", ""),
            placeholder="e.g., Data Analyst",
            key="input_target_role",
        )
        if target_role:
            st.session_state["target_role"] = target_role

    with col2:
        days_available = st.number_input(
            "Days available to prepare",
            min_value=1,
            max_value=180,
            value=15,
            step=1,
            key="input_days_available",
        )

    st.header("2. Upload Your Resume")
    resume_file = st.file_uploader("Choose your resume PDF", type=["pdf"])

    st.header("3. Job Description")
    job_description = st.text_area(
        "Paste the job description",
        placeholder="Paste the responsibilities and required skills...",
        height=200,
        key="input_job_description",
    )

    if st.button("Analyze My Placement Readiness", type="primary"):
        if not target_role.strip():
            st.warning("Please enter your target job role.")
        elif resume_file is None:
            st.warning("Please upload your resume PDF.")
        elif not job_description.strip():
            st.warning("Please paste the job description.")
        else:
            try:
                with st.spinner("Reading your resume..."):
                    resume_text = extract_resume_text(resume_file)

                if not resume_text:
                    st.error(
                        "No selectable text was found in this PDF. "
                        "It may be a scanned image; try a text-based PDF."
                    )
                    st.stop()

                if len(resume_text) < 40:
                    st.warning(
                        "Very little text was extracted. Check whether the PDF is readable."
                    )

                resume_skills = detect_skills(resume_text)
                required_skills = detect_skills(job_description)
                matched_skills = [s for s in required_skills if s in resume_skills]
                missing_skills = [s for s in required_skills if s not in resume_skills]

                st.divider()
                st.header("4. Your Skill Match Results")

                if required_skills:
                    match_score = round(len(matched_skills) / len(required_skills) * 100)
                    st.metric("Detected skill match", f"{match_score}%")
                    st.caption(
                        "This is the percentage of recognized job-description skills "
                        "also detected in your resume. It is not a probability of getting hired."
                    )
                else:
                    st.warning(
                        "No skills from the built-in keyword list were recognized "
                        "in the job description. The score cannot be calculated reliably."
                    )

                left, right = st.columns(2)
                with left:
                    st.subheader("✅ Matched skills")
                    if matched_skills:
                        for skill in matched_skills:
                            st.write(f"• {skill.title()}")
                    else:
                        st.write("No matching keywords detected yet.")

                with right:
                    st.subheader("📌 Potential skill gaps")
                    if missing_skills:
                        for skill in missing_skills:
                            st.write(f"• {skill.title()}")
                    else:
                        st.write("No missing skills detected by the current keyword list.")

                st.subheader("Skills detected in your resume")
                st.write(
                    ", ".join(skill.title() for skill in resume_skills)
                    if resume_skills
                    else "No skills from the built-in keyword list were detected."
                )

                st.divider()
                st.header("5. Your Personalized Preparation Plan")

                prompt = build_plan_prompt(
                    target_role=target_role,
                    days_available=days_available,
                    resume_skills=resume_skills,
                    matched_skills=matched_skills,
                    missing_skills=missing_skills,
                    resume_text=resume_text,
                    job_description=job_description,
                )

                with st.spinner("Ollama is creating your personalized plan..."):
                    plan = call_ollama(prompt)

                st.markdown(plan)
                st.caption(
                    "Review the plan before following it. AI-generated recommendations may contain mistakes."
                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to Ollama. Make sure Ollama is running. "
                    "Check it in another terminal with 'ollama list'."
                )
            except requests.exceptions.Timeout:
                st.error("The AI took too long to respond. Try again with shorter input.")
            except requests.exceptions.RequestException as error:
                st.error(f"Ollama request failed: {error}")
            except Exception as error:
                st.error(f"Something went wrong: {error}")


def render_sql_missions():
    """Render the SQL quiz learning missions and evaluation."""
    st.header("SQL Learning Missions")
    st.write(
        "Choose any level to practise. Each level has five questions, "
        "and every attempt is saved in your SQLite history."
    )

    st.subheader("Available quiz levels")
    for level in QUIZ_LEVELS:
        st.markdown(f"**{level['name']}**")
        st.caption(level["description"])

    level_names = [level["name"] for level in QUIZ_LEVELS]
    selected_level_name = st.selectbox(
        "Choose a SQL quiz level",
        options=level_names,
        key="selected_sql_level",
    )
    selected_level = next(
        level for level in QUIZ_LEVELS if level["name"] == selected_level_name
    )
    quiz_questions = selected_level["questions"]

    with st.form(f"sql_quiz_form_{selected_level_name}"):
        answers = []
        for i, question in enumerate(quiz_questions):
            selected = st.radio(
                question["question"],
                question["options"],
                index=None,
                key=f"{selected_level_name}_question_{i}",
            )
            answers.append(selected)

        submitted = st.form_submit_button("Submit Quiz", type="primary")

    if submitted:
        if any(answer is None for answer in answers):
            st.warning("Please answer all five questions before submitting.")
        else:
            score = sum(
                answer == question["answer"]
                for answer, question in zip(answers, quiz_questions)
            )
            total = len(quiz_questions)
            percentage = score / total
            recommendation = get_recommendation(selected_level_name, score, total)

            previous_result = get_latest_quiz_result()
            previous_percentage = (
                previous_result[1] / previous_result[2]
                if previous_result and previous_result[2] > 0
                else None
            )

            save_quiz_result(selected_level_name, score, total, recommendation)

            if previous_percentage is None:
                progress_message = "Your first recorded attempt is saved."
            elif percentage > previous_percentage:
                progress_message = (
                    "📈 Your score improved compared with your previous quiz attempt."
                )
            elif percentage < previous_percentage:
                progress_message = (
                    "📚 Your score was lower than your previous quiz attempt. "
                    "Review the explanations and try again."
                )
            else:
                progress_message = (
                    "Your score stayed the same as your previous quiz attempt."
                )

            st.session_state["last_quiz_feedback"] = {
                "level": selected_level_name,
                "score": score,
                "total": total,
                "percentage": percentage,
                "recommendation": recommendation,
                "progress_message": progress_message,
                "answers": answers,
                "questions": quiz_questions,
            }
            st.rerun()

    # Show the most recent result after a rerun
    feedback = st.session_state.get("last_quiz_feedback")
    if feedback:
        st.subheader(f"Latest result: {feedback['level']}")
        st.info(feedback["progress_message"])
        st.success(
            f"Your score: {feedback['score']}/{feedback['total']} "
            f"({feedback['percentage'] * 100:.0f}%)"
        )

        with st.expander("Review your latest answers", expanded=True):
            for answer, question in zip(feedback["answers"], feedback["questions"]):
                if answer == question["answer"]:
                    st.write(f"✅ {question['question']}")
                else:
                    st.write(
                        f"❌ {question['question']} Your answer: {answer}. "
                        f"Correct answer: {question['answer']}."
                    )
                st.caption(question["explanation"])

        st.subheader("Recommended next step")
        st.write(feedback["recommendation"])


def render_role_missions(target_role: str = ""):
    """Render the target-role specific quiz learning missions."""
    st.header("Target-Role Learning Missions")
    st.write(
        "Practise questions tailored to a job role. Every submitted attempt "
        "is saved in your existing SQLite quiz history."
    )

    role_names = list(ROLE_QUIZZES.keys())
    typed_role = target_role.strip().casefold() if target_role else ""
    default_role_index = next(
        (i for i, role_name in enumerate(role_names)
         if role_name.casefold() == typed_role),
        0,
    )
    selected_role = st.selectbox(
        "Choose a role for your quiz",
        options=role_names,
        index=default_role_index,
        key="selected_role_quiz_role",
    )

    role_quizzes = ROLE_QUIZZES[selected_role]
    selected_role_quiz = st.selectbox(
        "Choose a role quiz",
        options=role_quizzes,
        format_func=lambda quiz: f"{quiz['name']} — {quiz['description']}",
        key="selected_role_quiz_name",
    )
    role_questions = selected_role_quiz["questions"]
    role_quiz_name = selected_role_quiz["name"]

    with st.form(f"role_quiz_form_{selected_role}_{role_quiz_name}"):
        role_answers = []
        for i, question in enumerate(role_questions):
            answer = st.radio(
                question["question"],
                question["options"],
                index=None,
                key=f"role_{selected_role}_{role_quiz_name}_question_{i}",
            )
            role_answers.append(answer)

        role_submitted = st.form_submit_button("Submit Role Quiz", type="primary")

    if role_submitted:
        if any(answer is None for answer in role_answers):
            st.warning("Please answer all five role-quiz questions before submitting.")
        else:
            role_score = sum(
                answer == question["answer"]
                for answer, question in zip(role_answers, role_questions)
            )
            role_total = len(role_questions)
            role_percentage = role_score / role_total if role_total else 0

            if role_percentage >= 0.8:
                role_recommendation = (
                    f"Great work on {role_quiz_name}! You scored at least 80%. "
                    "Try applying these concepts in a small practical project."
                )
            else:
                role_recommendation = (
                    f"Review the explanations for {role_quiz_name}, practise the "
                    "topics you missed, and then retry the quiz."
                )

            previous_role_result = get_latest_quiz_result()
            previous_role_percentage = (
                previous_role_result[1] / previous_role_result[2]
                if previous_role_result and previous_role_result[2] > 0
                else None
            )

            save_quiz_result(
                role_quiz_name,
                role_score,
                role_total,
                role_recommendation,
            )

            if previous_role_percentage is None:
                role_progress_message = "Your first recorded attempt is saved."
            elif role_percentage > previous_role_percentage:
                role_progress_message = (
                    "Your score is higher than your immediately previous quiz attempt."
                )
            elif role_percentage < previous_role_percentage:
                role_progress_message = (
                    "Your score is lower than your immediately previous quiz attempt. "
                    "Review the explanations and keep practising."
                )
            else:
                role_progress_message = (
                    "Your score matches your immediately previous quiz attempt."
                )

            st.session_state["last_role_quiz_feedback"] = {
                "level": role_quiz_name,
                "score": role_score,
                "total": role_total,
                "percentage": role_percentage,
                "recommendation": role_recommendation,
                "progress_message": role_progress_message,
                "answers": role_answers,
                "questions": role_questions,
            }
            st.rerun()

    role_feedback = st.session_state.get("last_role_quiz_feedback")
    if role_feedback:
        st.subheader(f"Latest role-quiz result: {role_feedback['level']}")
        st.info(role_feedback["progress_message"])
        st.success(
            f"Your score: {role_feedback['score']}/{role_feedback['total']} "
            f"({role_feedback['percentage'] * 100:.0f}%)"
        )
        with st.expander("Review your role-quiz answers", expanded=True):
            for answer, question in zip(
                role_feedback["answers"], role_feedback["questions"]
            ):
                if answer == question["answer"]:
                    st.write(f"✅ {question['question']}")
                else:
                    st.write(
                        f"❌ {question['question']} Your answer: {answer}. "
                        f"Correct answer: {question['answer']}."
                    )
                st.caption(question["explanation"])

        st.subheader("Recommended next step")
        st.write(role_feedback["recommendation"])


def render_learning_progress():
    """Render the SQLite quiz attempt history and progress metrics."""
    st.subheader("Your Learning Progress")
    history = get_quiz_history()
    total_attempts = get_total_quiz_attempts()

    if history:
        latest = history[0]
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Latest quiz score", f"{latest[2]}/{latest[3]}")
        with col2:
            st.metric("Total attempts", total_attempts)

        st.caption("Showing your 10 most recent attempts. Older attempts remain saved.")
        history_display = []
        for row in history:
            attempt_id, quiz_name, score, total, recommendation, created_at = row
            history_display.append(
                {
                    "Attempt": attempt_id,
                    "Quiz level": quiz_name,
                    "Score": f"{score}/{total}",
                    "Percentage": f"{score / total * 100:.0f}%",
                    "Date": str(created_at),
                    "Recommendation": recommendation,
                }
            )

        st.dataframe(history_display, use_container_width=True, hide_index=True)
    else:
        st.info("No quiz attempts saved yet. Complete a quiz to start tracking progress.")
