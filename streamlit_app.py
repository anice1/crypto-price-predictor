import streamlit as st
from Engine import Predictor


# Instantiate Predictor
def run():
    pred = Predictor()

    st.title('Crypto prediction Model')
    st.write('''
    ### The main objective of this project is to produce a workable model that will be able to predict the closing price of crypto currencies.
    ''')

    coin_name = st.selectbox('Select a crypto coin', [coins for coins in pred.get_coin_symbols(pred.df)])
    date = st.date_input('Enter Year')
    open = st.number_input('Enter Opening Price for the day')
    lowest = st.number_input('Enter Lowest Price for the day')
    high = st.number_input('Enter Highest Price for the day')
    volume = st.number_input('Volume of transaction for the day')
    marketcap = st.number_input('Market capitalization in USD')

    predict_btn = st.button('Predict price')

    if predict_btn:
        input_data = pred.get_input_data_ready(coin_name, date, high, lowest, open, volume, marketcap)
        prediction = pred.predict(input_data)
        st.write(f'### Predicted Closing price for {coin_name}')
        st.success(prediction)


if __name__ == "__main__":
    run()