import streamlit as st
import pickle
import pandas as pd
import numpy as np


model=pickle.load(open("LinearRegression.sav",'rb'))
data=pd.read_csv("clean_car_data.csv")





def car_price_prediction(input_data):
    

    y_pred=model.predict(pd.DataFrame([input_data]))
    print("preiction: ",y_pred)

    

def main():

    st.title("Car price prediction Application")

    name=data['name'].unique()
    company=data['company'].unique()
    fuel_type=data['fuel_type'].unique()  
    year=data['year'].unique() 
    kms_driven=data['kms_driven']


    name=st.selectbox("name of car:",name)
    company=st.selectbox("name of car company mfg:",company)
    year=st.slider("year:",2001,2020,2001)
    kms_driven=st.text_input("kilometer driven")
    fuel_type=st.selectbox("fuel type",fuel_type)


    price_prediction=""

    if st.button("predict_price"):
      price_prediction = car_price_prediction([name,company,year,kms_driven,fuel_type])

    st.subheader(f"est price:{price_prediction}")
    # st.success(price_prediction)



if __name__=='__main__':
    main()


