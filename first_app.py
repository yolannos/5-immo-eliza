import streamlit as st 
import pickle

# # load
xgb_model_loaded = pickle.load(open("xgb_reg.pkl", "rb"))


def main():
    st.title("Belgium Real Estate Price Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"> Your favorite App to estimate the price of your good </h2>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader('Please enter the required details:')
    locality = st.text_input("Postal Code","")
    area = st.text_input("Square-meter area","")

    result=""

    if st.button("Estimate the Price"):
        result=int(locality) * int(area )
    st.success(f'The output is {result}')
    if st.button("About"):
        st.text("Thanks for watching the presentation")

if __name__=='__main__':
    main()