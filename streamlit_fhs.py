import streamlit as st
import joblib
import pandas as pd

model = joblib.load('fhs__model_dt.pkl')
st.write("#Financial Status Prediction")

fpl = st.selectbox("Enter your status",["high", "medium","low"])

col1, col2, col3 = st.columns(3)



FWBscore = col2.selectbox("What is your financial wellbeing score?",["-4"," -1"," 14","16","17","18","19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90","95"])
FWB1_1  = col3.selectbox("Can you handle a major unexpected expense",["-4","-1","1", "2", "3", "4","5"])
FWB1_2 = col1.selectbox("Do you believe that you are securing your financial future?",["1", "2", "3", "4","5"])
FWB1_3 = col1.selectbox("Do you believe that because of your financial status you will not have all you want in life?",["1", "2", "3", "4","5"])
FWB1_5 = col1.selectbox("Do you believe that you are just getting by financially?",["1", "2", "3", "4","5"])
FWB2_1  = col2.selectbox("will giving a gift put a strain on my finances for the month?",["1", "2", "3", "4","5"])
FWB2_2  = col3.selectbox(" Do you believe you will have money left over at the end of the month?",["1", "2", "3", "4","5"])
SAVEHABIT  = col3.selectbox("Is putting money into savings  a habit for you?",["1", "2", "3", "4","5"])
VALUERANGES  = col1.selectbox("If you were to sell your home today, what do you think it would be worth?",["-1","1", "2", "3", "4","5","6"])
PRODHAVE_4  = col2.selectbox("Do you have a Retirement Account?",["1","0"])

SNAP  = col3.selectbox("Did Any household member received SNAP Survey item benefits?",["-1","1","0"])

MATHARDSHIP_1    =   col1.selectbox("Worried whether food would run out before got money to buy more",["1","0"])
MATHARDSHIP_2    =  col2.selectbox("Food didn't last and didn't have money to get more",["1","0"])
ABSORBSHOCK   =     col3.selectbox("Confidence in ability to raise $2,000 in 30 days",["1","0"])
BENEFITS_1    =     col1.selectbox(" Do you have Health Insurance",["1","0"])
BENEFITS_2  =       col2.selectbox("Do you have 401(k) or Other Employer-Sponsored Retirement Savings Account",["1",'0'])
BENEFITS_3  =       col2.selectbox("Do you have Defined-Benefit Pension",["1",'0'])
PAREDUC   =         col1.selectbox("Highest level of education by person/people who raised respondent",["1","2","3","4","5"])
HHEDUC  =           col2.selectbox("Highest level of education of all household members ",["1","2","3","4","5"])
PPEDUC  =           col3.selectbox("Education (Highest Degree Received)",["1","2","3","4","5"])
PPINCIMP  =         col1.selectbox("Household Income",["1","2","3","4","5","6","7","8","9"])

  


df_pred = pd.DataFrame({
    
    'FWBscore': [FWBscore],
    'FWB1_1': [FWB1_1],
    'FWB1_2': [FWB1_2],
    'FWB1_3': [FWB1_3],
    'FWB1_5': [FWB1_5],
    'FWB2_1': [FWB2_1],
    'FWB2_2': [FWB2_2],
    'SAVEHABIT': [SAVEHABIT],
    'VALUERANGES': [VALUERANGES],
    'PRODHAVE_4': [PRODHAVE_4],
    'SNAP': [SNAP],
    'MATHARDSHIP_1': [MATHARDSHIP_1],
    'MATHARDSHIP_2': [MATHARDSHIP_2],
    'BENEFITS_1': [BENEFITS_1],
    'BENEFITS_2': [BENEFITS_2],
    'BENEFITS_3': [BENEFITS_3],
    'PAREDUC': [PAREDUC],
    'HHEDUC': [HHEDUC],
    'PPEDUC': [PPEDUC],
    'PPINCIMP': [PPINCIMP]
})

prediction = model.predict(df_pred)
st.write("Prediction:", prediction)

