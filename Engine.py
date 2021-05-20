import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_log_error, mean_absolute_error, r2_score
import numpy as np
import pickle

model = pickle.load(open('cryptopredictor.pkl', 'rb'))

# Create a class to containing all methods we need
class Predictor:

    # Read symbols and codes data
    df = pd.read_csv('Crypto data set/Symbols_and_code.csv')

    # Extract all symbols from symbols_and_code.csv
    symbols = [symbol.upper() for symbol in df['Symbols']]
    
    def __init__(self):
        pass

    def get_coin_symbols(self, df):
        """
        Loops through df and returns all coin symbols in df
        """
        try:
            return set(self.df['Symbols'])
        except Exception:
            return 'No symbol Found'

    def convert_symbol_to_codes(self, symbol):
        try:
            if symbol in self.symbols:
                return self.symbols.index(symbol)
        except Exception as e:
            return e
    
    def get_input_data_ready(self, symbol, date, high, low, open, volume, marketcap):
        symbol_code = self.convert_symbol_to_codes(symbol)
        return [symbol_code, high, low, open,volume, marketcap, date.year, date.month, date.day]

    def predict(self, data):
        prediction = model.predict([data])
        return prediction[0]

    def evaluate(self, y_true, y_pred):
        evaluations = {
            'Root Mean Squared Error': np.sqrt(mean_squared_log_error(y_true, y_pred)),
            'Mean Absolute Error': mean_absolute_error(y_true, y_pred),
            'R^2 Score': r2_score(y_true, y_pred)
        }
        return evaluations