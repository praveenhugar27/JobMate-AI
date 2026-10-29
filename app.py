"""JobMate AI - Your Personal Placement Strategist.

Main Streamlit Application Entry Point.
"""

import streamlit as st
from config import MODEL
from database import initialize_database
from ui_components import (
    render_learning_progress,
    render_placement_analyzer,
    render_role_missions,
    render_sql_missions,
)

# --------------------------------------------------
# Page Configuration & Database Setup
# --------------------------------------------------
st.set_page_config(page_title="JobMate AI", page_icon="🎯", layout="wide")

initialize_database()

# --------------------------------------------------
# Header & Information
# --------------------------------------------------
st.title("🎯 JobMate AI")
st.subheader("Your Personal Placement Strategist")
st.write(
    "Understand your skill gaps and get a preparation plan tailored to your target job."
)
st.info(f"AI model: {MODEL} running locally through Ollama.")

# Sidebar view navigation
st.sidebar.title("Navigation")
view_mode = st.sidebar.radio(
    "Select layout:",
    options=["📑 Tabbed View", "📜 Single Page View"],
    index=0,
)

target_role = st.session_state.get("target_role", "")

# --------------------------------------------------
# Render Views
# --------------------------------------------------
if view_mode == "📑 Tabbed View":
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Placement Readiness",
        "🗄️ SQL Missions",
        "💼 Role Missions",
        "📊 Progress History",
    ])

    with tab1:
        render_placement_analyzer()

    with tab2:
        render_sql_missions()

    with tab3:
        render_role_missions(target_role=st.session_state.get("target_role", ""))

    with tab4:
        render_learning_progress()

else:
    # Single continuous page view (matching original design)
    render_placement_analyzer()
    st.divider()
    render_sql_missions()
    st.divider()
    render_role_missions(target_role=st.session_state.get("target_role", ""))
    st.divider()
    render_learning_progress()
