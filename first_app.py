import numpy as np
import pandas as pd
from utils import utils
import pickle
import streamlit as st 
import webbrowser

model = pickle.load(open("bg_reg.pkl", "rb"))

###### Just to get exactly the same columns as the one used in the model
data = pd.read_csv("https://raw.githubusercontent.com/SamuelD005/challenge-regression/development/Data8.csv", sep=",")
X = data.drop(["Price","Unnamed: 0","PriceperMeter"] , axis = 1)
columns = X.columns
#######


def main():
    st.title("Belgium Real Estate - Price prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"> Your favorite App to estimate the price of your good </h2>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader('Please enter general informations:')
    type_of_property = st.selectbox('Select', ["house", "apartment"])
    locality = st.number_input("Enter your locality", min_value= 1000, max_value = 9999)
    number_of_room = st.number_input("Enter the number of rooms", min_value= 0, max_value = 10)
    area = st.number_input("Enter the area of your house", min_value= 0, max_value = 1000)
    state_of_building = st.selectbox('What is the state of your house?', ["good", "medium", "to renovate", "new"])

    st.subheader('Please enter indoor informations:')
    fully_equipped_kitchen = st.selectbox('Is your Kitchen fully equipped?', ["No","Yes"])
    furnished = st.selectbox('Is your house is sell furnished?', ["No","Yes"])
    open_fire = st.selectbox('Do you have an open fire?', ["No","Yes"])

    st.subheader('Please enter outdoor informations:')
    
    terrace_area = st.number_input("Enter the area of your terrace", min_value= 0, max_value = 1000)
    garden_area = st.number_input("Enter the area of your garden", min_value= 0, max_value = 100000000)
    number_of_facades = st.selectbox('What is the number of facades?', [2, 3, 4])
    swimming_pool = st.selectbox('Do you have a swimming pool?', ["No","Yes"])
    surface_of_the_land = area + terrace_area + garden_area


    province = utils.change_to_province(locality)[:2][0]
    region = utils.change_to_province(locality)[:2][1]

    fully_equipped_kitchen = 1 if fully_equipped_kitchen == "Yes" else 0
    furnished = 1 if furnished == "Yes" else 0
    open_fire = 1 if open_fire == "Yes" else 0
    swimming_pool = 1 if swimming_pool == "Yes" else 0

    df = pd.DataFrame([[locality,
                        type_of_property,
                        number_of_room,area, 
                        fully_equipped_kitchen, 
                        furnished, 
                        open_fire, 
                        terrace_area,
                        garden_area,
                        surface_of_the_land,
                        number_of_facades,
                        swimming_pool,
                        state_of_building,
                        province,
                        region]], 
                        columns= columns)

    with st.sidebar:
        url = "https://github.com/yolannos/5-immo-eliza"
        st.header('Hello there!')
        st.subheader("Welcome to this brand new app")
        st.write("If you want to have the code, just go on Github")
        if st.button('Open Github'):
            webbrowser.open_new_tab(url)

    if st.button("Estimate the Price"):
        result= model.predict(df)
        st.success(f'The output is {np.expm1(result[0])}')
    if st.button("About"):
        st.text("Thanks for watching the presentation")

if __name__=='__main__':
    main()