import streamlit as st
import matplotlib.pyplot as plt

# Custom CSS for professional UI
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
st.markdown(
    """
    <style>
    .stProgress > div > div > div {
        background-color: #1f77b4;
    }
    .st-bb {
        background-color: #f0f2f6;
    }
    .st-at {
        background-color: #f0f2f6;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1565c0;
    }
    .stMarkdown h1 {
        color: #1f77b4;
    }
    .stMarkdown h2 {
        color: #2ca02c;
    }
    .stMarkdown h3 {
        color: #ff7f0e;
    }
    .stMarkdown h4 {
        color: #d62728;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and Description
st.title("⚖️ Professional BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and understand your health status.")

# Input Fields in Columns
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f", help="Enter your weight in kilograms.")
with col2:
    height = st.number_input("Enter your height (meters)", min_value=0.0, format="%.2f", help="Enter your height in meters.")

# BMI Calculation
if st.button("Calculate BMI", help="Click to calculate your BMI."):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is **{bmi:.2f}**")

        # BMI Categories
        bmi_categories = {
            "Underweight": (0, 18.5),
            "Normal weight": (18.5, 24.9),
            "Overweight": (25, 29.9),
            "Obesity": (30, 100)
        }

        # Determine BMI Category
        category = None
        for cat, (lower, upper) in bmi_categories.items():
            if lower <= bmi <= upper:
                category = cat
                break

        # Display BMI Category
        if category:
            st.subheader(f"Category: **{category}**")

        # Progress Bar
        st.write("BMI Range:")
        progress = min(bmi / 40, 1.0)  # Normalize BMI to 0-40 range
        st.progress(progress)

        # BMI Chart
        fig, ax = plt.subplots()
        categories = list(bmi_categories.keys())
        ranges = [f"{lower}-{upper}" for lower, upper in bmi_categories.values()]
        colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728"]
        ax.barh(categories, [upper - lower for lower, upper in bmi_categories.values()], color=colors)
        ax.axvline(x=bmi, color="red", linestyle="--", label="Your BMI")
        ax.set_xlabel("BMI Range")
        ax.set_title("BMI Categories")
        ax.legend()
        st.pyplot(fig)

    else:
        st.error("Height must be greater than 0.")