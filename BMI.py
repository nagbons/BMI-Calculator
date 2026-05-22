import streamlit as st
from PIL import Image
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="BMI Health Analytics",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background: #0B1120;
    color: white;
}

/* Main container spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1F2937;
}

/* Hero Section */
.hero {
    background: linear-gradient(
        135deg,
        #2563EB,
        #1E3A8A
    );
    padding: 2.5rem;
    border-radius: 24px;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
}

/* Glass Cards */
.glass-card {
    background: rgba(30, 41, 59, 0.75);
    backdrop-filter: blur(10px);
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    color: white;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 3.4rem;
    border-radius: 14px;
    border: none;
    background: linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    );
    color: white;
    font-size: 18px;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #1D4ED8,
        #2563EB
    );
}

/* Metric Styling */
.metric-container {
    text-align: center;
    padding: 20px;
    border-radius: 18px;
    background-color: #1E293B;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(
        90deg,
        #2563EB,
        #60A5FA
    );
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("💪 Health Dashboard")

st.sidebar.markdown("""
### BMI Health Analytics System

Track and monitor your Body Mass Index
using an interactive health dashboard.
""")

st.sidebar.markdown("---")

st.sidebar.success("System Status: Active")

st.sidebar.markdown("""
### Features
- BMI Analysis
- Health Classification
- Risk Assessment
- Health Insights
- Wellness Monitoring
""")

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

# 💪 BMI Health Analytics Dashboard

### Advanced Body Mass Index Monitoring Platform

Monitor your BMI, analyze your health status,
and gain wellness insights through an
interactive health analytics system.

</div>
""", unsafe_allow_html=True)

# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-container">
    <h3>Healthy BMI</h3>
    <h1>18.5 - 24.9</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-container">
    <h3>Health Goal</h3>
    <h1>Balanced</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-container">
    <h3>Wellness Focus</h3>
    <h1>Fitness</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# MAIN LAYOUT
# =========================================================

left_col, right_col = st.columns([1, 1])

# =========================================================
# LEFT COLUMN
# =========================================================

with left_col:

    st.markdown("""
    <div class="glass-card">
    """, unsafe_allow_html=True)

    st.subheader("📝 Personal Information")

    firstname = st.text_input("Firstname")

    lastname = st.text_input("Lastname")

    height = st.number_input(
        "Height (cm)",
        min_value=0.0,
        format="%.2f"
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        format="%.2f"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RIGHT COLUMN
# =========================================================

with right_col:

    image = Image.open("IMG-20260214-WA0003.jpg")

    st.image(
        image,
        caption="Health & Fitness Illustration",
        use_container_width=True
    )

# =========================================================
# BMI CLASSIFICATION TABLE
# =========================================================

st.markdown("## 📊 BMI Classification")

bmi_table = pd.DataFrame({
    "BMI Range": [
        "Below 18.5",
        "18.5 – 24.9",
        "25 – 29.9",
        "30 and above"
    ],
    "Category": [
        "Underweight",
        "Normal Weight",
        "Overweight",
        "Obese"
    ]
})

st.dataframe(
    bmi_table,
    use_container_width=True
)

# =========================================================
# CALCULATE BMI
# =========================================================

if st.button("Calculate BMI"):

    if firstname.strip() == "" or lastname.strip() == "":
        st.warning(
            "⚠️ Please enter both firstname and lastname."
        )

    elif height <= 0 or weight <= 0:
        st.error(
            "❌ Please enter valid values."
        )

    else:

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        fullname = f"{firstname} {lastname}"

        st.markdown("---")

        st.markdown(f"""
        # 📈 Health Analysis Report
        
        ### Patient: {fullname}
        """)
        
        st.metric(
            label="BMI Score",
            value=f"{bmi:.2f}"
        )

        # =====================================================
        # BMI CATEGORY
        # =====================================================

        if bmi < 18.5:

            category = "Underweight"

            st.warning(
                f"{fullname}, your BMI indicates "
                f"you are Underweight."
            )

            recommendation = """
            Increase nutrient-rich calorie intake,
            maintain balanced meals, and consider
            professional dietary guidance.
            """

        elif 18.5 <= bmi < 25:

            category = "Normal Weight"

            st.success(
                f"{fullname}, your BMI is within "
                f"the healthy range."
            )

            recommendation = """
            Maintain your healthy lifestyle through
            balanced nutrition and regular exercise.
            """

        elif 25 <= bmi < 30:

            category = "Overweight"

            st.info(
                f"{fullname}, your BMI indicates "
                f"you are Overweight."
            )

            recommendation = """
            Consider moderate exercise routines and
            healthier dietary habits.
            """

        else:

            category = "Obese"

            st.error(
                f"{fullname}, your BMI indicates Obesity."
            )

            recommendation = """
            Professional medical consultation and
            structured weight management strategies
            are recommended.
            """

        # =====================================================
        # BMI VISUALIZATION
        # =====================================================

        st.markdown("### BMI Indicator")

        bmi_progress = min(bmi / 40, 1.0)

        st.progress(float(bmi_progress))

        st.markdown(f"""
        ### Health Category: **{category}**
        """)

        # =====================================================
        # HEALTH RECOMMENDATION
        # =====================================================

        st.markdown("## 💡 Health Recommendation")

        st.info(recommendation)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "BMI Health Analytics Platform | Powered by Streamlit"
)