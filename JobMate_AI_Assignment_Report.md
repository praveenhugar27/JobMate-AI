# DAYANANDA SAGAR UNIVERSITY
### School of Engineering — Department of CSE (Data Science)
#### Harohalli, Bengaluru

---

## FAI ASSIGNMENT REPORT

| Field | Details |
| :--- | :--- |
| **Course Name** | FOUNDATIONS OF AI & AUTHENTIC INTELLIGENCE |
| **Course Code** | 24DS3502 |
| **Topic** | JobMate AI — Your Personal Placement Strategist |
| **Section** | 5A |

---

### Team Details

| USN | Student Name | Role / Contribution |
| :--- | :--- | :--- |
| **ENG24DS0043** | Ramya Anegundi | Model Integration, UI & Document Parsing |
| **ENG25DS1003** | Praveen J Hugar | SQLite Database, Quiz Missions & Testing |

---

### 1. Agent Name & Role

* **Agent Name**: `JobMate AI — Your Personal Placement Strategist`
* **Agent Role**: 
  JobMate AI is an AI-powered placement preparation assistant developed to help college students prepare for internships and campus placements. It analyses a student's resume alongside a target job description, identifies relevant skills and possible skill gaps, and provides AI-generated preparation guidance.
  
  The application also includes interactive SQL learning missions, target-role-specific quizzes, immediate answer explanations, and an automated learning progress tracker.

---

### 2. Agent Goal

The primary goal of JobMate AI is to help students prepare for technical placements through a personalized, realistic, and structured learning process.

It empowers students to:
1. Understand the core competencies and expectations of a target job role.
2. Objectively recognize specific technical skill gaps in their resumes.
3. Practise essential database and role-based concepts through interactive assessments.
4. Track their preparation trajectory and score improvements over time.

---

### 3. Special Feature: The Resume-to-Readiness Learning Loop

The defining feature of JobMate AI is its **Resume-to-Readiness Learning Loop**.

Traditional tools stop after static resume parsing or keyword scoring. In contrast, JobMate AI creates a continuous, actionable preparation feedback loop:
* **Identification**: Detects missing technical keywords against job descriptions.
* **Planning**: Generates an exact day-by-day study roadmap using the local LLM.
* **Practice**: Directly connects the student to progressive SQL missions and target-role quizzes.
* **Review & Retention**: Delivers contextual explanations for every question and logs attempts into a local SQLite database for persistent tracking.

---

### 4. Main Capabilities

1. **Resume and Job Requirement Analysis**: Accepts PDF resumes and target job descriptions. Extracts selectable text via PyMuPDF and computes boundary-matched skill overlaps and gap diagnostics.
2. **Personalized Preparation Planning**: Leverages the local `Qwen2.5:3B` model through Ollama to generate numbered, day-by-day study plans tailored to available preparation days (e.g., 7 to 180 days).
3. **Interactive Technical Learning**: Features sequential SQL quiz tiers (SQL Basics, SQL Aggregation, Joins & Subqueries) with progressive 80% passing thresholds, alongside dedicated career role quizzes (Data Analyst, Software Engineer, Data Scientist, Web Developer).
4. **Quiz Evaluation and Progress Tracking**: Computes real-time scores, shows question-by-question explanations, provides personalized next-step recommendations, and stores full historical attempts in SQLite.

---

### 5. System Workflow

The application operates on an end-to-end, privacy-preserving local workflow:

```text
[ User Input ]
      │  (Target Role, Available Days, Resume PDF, Job Description)
      ▼
[ Document Processing ]
      │  (PyMuPDF extracts selectable text stream)
      ▼
[ Skill Comparison Engine ]
      │  (Regex boundary matching finds Matched Skills & Skill Gaps)
      ▼
[ AI Preparation Guidance ]
      │  (Ollama + Qwen2.5:3B generates Day 1..N customized study plan)
      ▼
[ Technical Practice Missions ]
      │  (Student takes 5-question SQL or Role-based quizzes)
      ▼
[ Progress Tracking & Analytics ]
      │  (Scores, timestamps, and recommendations saved to SQLite)
```

1. **Input**: The student specifies the target role, preparation days, uploads a resume PDF, and pastes the job description.
2. **Document Processing**: Selectable text is extracted from the uploaded PDF stream without writing unencrypted temp files.
3. **Skill Analysis**: Boundary-enforced regex extracts known skills from both texts, computing match percentage and missing requirements.
4. **Preparation Guidance**: Ollama constructs a contextual prompt and generates a daily plan with topics, tasks, and completion checks.
5. **Practice**: The student attempts sequential SQL or role-specific assessments.
6. **Progress Tracking**: Results, scores, comparisons with previous attempts, and recommendations are permanently logged to SQLite.

---

### 6. Tools Used and Purpose

| Tool / Technology | Purpose |
| :--- | :--- |
| **Python 3.13** | Core programming language powering the application logic, text processing, and system orchestration. |
| **Streamlit** | Powers the interactive web dashboard, dynamic layouts, and reactive session state management. |
| **Ollama** | Local LLM runtime delivering offline, private, low-latency AI inference without external cloud APIs. |
| **Qwen2.5:3B** | High-efficiency 3-billion parameter model used to generate structured, day-numbered preparation roadmaps. |
| **PyMuPDF (fitz)** | High-speed C-backed PDF parsing library used to extract text streams directly from uploaded resumes. |
| **SQLite 3** | Lightweight relational database for persistent storage of quiz attempts, historical scores, and timestamps. |
| **Visual Studio Code** | Primary Integrated Development Environment (IDE) used for writing, debugging, and modular refactoring. |

---

### 7. Sample Input and Observed Output

#### Sample Input Data
* **Target Role**: Data Analyst
* **Preparation Time**: 7 days
* **Resume Document**: `Ramya_Anegundi_Resume.pdf`
* **Job Description**: Data Analyst Intern
* **Required Skills in JD**: Python, SQL, Excel, Power BI, Statistics, Data Visualization

#### Observed Placement Readiness Output
* **Detected Skills in Resume**: Python, SQL
* **Matched Skills**: Python, SQL
* **Potential Skill Gaps**: Excel, Power BI, Statistics, Data Visualization
* **Observed Skill Match Score**: **33%** (2 out of 6 recognized skills matched)
* **AI Plan Output**: Generated an exact 7-day numbered plan focusing on Excel data cleaning, Power BI DAX basics, descriptive statistics, and visualization projects.

#### Observed Assessment Results
| Quiz Level / Topic | Score Observed | Performance |
| :--- | :---: | :--- |
| **SQL Basics** | 4 / 5 | 80% (Pass / Unlocks Aggregation Level) |
| **Data Analyst — Python Basics** | 5 / 5 | 100% (Mastery) |

* **Total Recorded Quiz Attempts in Test Session**: **21 attempts** logged in `jobmate_progress.db`.

---

### 8. Working Prototype Verification

JobMate AI is fully implemented and tested as a local Streamlit web application.

#### Verified Working Features:
* Multi-page/tab navigation (Placement Readiness, SQL Missions, Role Missions, Learning Progress).
* File uploader parsing PDF resumes directly into memory.
* Skill matching engine displaying visual metric badges, matched lists, and gap lists.
* Ollama API integration producing structured preparation schedules.
* Interactive 5-question multiple choice quizzes with radio buttons and form validation.
* Instant grading with green/red answer keys and contextual explanations.
* SQLite database operations (`jobmate_progress.db`) maintaining persistent historical records across restarts.

---

### 9. Limitations & Practical Considerations

1. **Scanned PDF Limitations**: The current text extraction pipeline handles selectable text; scanned image-only PDFs require an integrated OCR layer (e.g., Tesseract).
2. **Catalog-Bound Skill Detection**: Skill recognition relies on a predefined catalog; unusual or highly specialized skill phrasings may require semantic embedding comparisons.
3. **Generative Model Nuances**: While the prompt enforces strict formatting, LLM-generated timelines should be reviewed by candidates for topic pacing.
4. **Scope of Question Banks**: The included quizzes test foundational core concepts rather than exhaustive placement curricula.
5. **Local Hardware Requirements**: The host computer must have Ollama installed with the `qwen2.5:3b` model downloaded (approx. 1.9 GB VRAM/RAM).
6. **Internal Diagnostic Metric**: The match percentage is an informative readiness diagnostic and not an official employability or hiring guarantee.

---

### 10. Conclusion

JobMate AI demonstrates the practical application of local AI models and software engineering principles in addressing placement preparation challenges. By unifying resume gap analysis with day-by-day planning and gamified technical assessments into a single privacy-first tool, it provides an authentic, accessible preparation companion for engineering students.
