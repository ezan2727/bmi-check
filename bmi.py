import streamlit as st

st.set_page_config(page_title="BMI CALCULATOR",page_icon="⛹🏻‍♀️",layout="centered") #setup page web
st.title("BMI CALCULATOR") #TAJUK
st.write("💪 let's calculate your **BMI** here") #copywriting tulis lah apa2 

st.header("Enter your details") #user input 
height = st.number_input("enter your height (in cm)",min_value=90,max_value=200,value=170) #berat user in no
weight = st.number_input("enter your weight (in kg)",min_value=10,max_value=200,value=65)

st.write(f"Your Height: {height} in cm")
st.write(f"Your weight: {weight} in kg")

if st.button("calculate bmi"):
    h_m = height/100 #convert cm to meters
    bmi = weight / (h_m ** 2)
    st.success(f"your bmi is **{bmi:.2f}**")

    if bmi < 18.5:
        category = "underweight 😅"
        color = "#F5E427"

    elif 18.5 <bmi < 25:
        category = "normal 😄 "
        color = "#6FF527"

    elif 25 <=bmi < 30:
        category = "Overweight 🫣"
        color = "#F59527"

    else:
        category = "Oh No! You are Obese 🙀"
        color = "#F54927"
        
st.markdown(
       f"""
       <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
       <h3>Your BMI Category : {category}</h3>
       </div>
       """,
        unsafe_allow_html=True
        )

st.write(category)
