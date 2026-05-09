import streamlit as st
from PIL import Image
import pandas as pd 
#Add Title to the app
st.markdown(
    "<h1 style='text-align: center;'>BMI CALCULATOR</h1>",
    unsafe_allow_html=True
)
# Dislay image
image = Image.open("IMG-20260214-WA0003.jpg")
# Create 3 columns to center the image
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        image,
        caption="Body Mass Index Illustration",
        use_container_width=True
    )
#input Fields
st.markdown(
    "<h3 style='text-align: center;'>BMI Classification Table</h3>",
    unsafe_allow_html=True
)
bmi_table = pd.DataFrame({
    "BMI Range": ["Below 18.5", "18.5 – 24.9", "25 – 29.9", "30 and above"],
    "Category": ["Underweight", "Normal Weight", "Overweight", "Obese"]
})
st.table(bmi_table)
# -------------------------
# INPUT SECTION
# -------------------------
Firstname= st.text_input("Enter your Firstname:")
Lastname= st.text_input("Enter your Lastname:")
height = st.number_input("Enter your height {in cm}:", min_value = 0.0, format= "%.2f")
weight = st.number_input("Enter your weight {in kg}:", min_value=0.0, format = "%.2f")
# -------------------------
# BMI CALCULATION
if st.button("Calculate BMI"):
# -------------------------
 # Check for empty names
    if Firstname.strip() == "" or Lastname.strip() == "":
         st.warning("⚠️ Please enter both your Firstname and Lastname.")
    
    elif height <= 0 or weight <= 0:
        st.error("❌ Please enter valid height and weight values.")
    
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        name = f"{Firstname} {Lastname}"

# Determine category + color
        if bmi < 18.5:
            category = "Underweight"
            st.warning(f"⚠️ {name}, your BMI is {bmi:.2f} — {category}")
        
        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
            st.success(f"✅ {name}, your BMI is {bmi:.2f} — {category}")
        
        elif 25 <= bmi < 30:
            category = "Overweight"
            st.info(f"ℹ️ {name}, your BMI is {bmi:.2f} — {category}")
        
        else:
            category = "Obese"
            st.error(f"🚨 {name}, your BMI is {bmi:.2f} — {category}")
