import requests
import pandas as pd


"""
Single Prediction
"""
df_test = pd.read_csv("C://Users//rafae//Desktop//UNI//SRCIM//T2//test.csv")
X_test  = df_test.iloc[1,2:-1]
payload = X_test.to_json()

response = requests.post('http://127.0.0.1:5000/modelprediction', json=payload).json()

if response == 0:
    print(' Your machine is ok')
elif response == 1:
    print('Maintenance')
else:
    print('Unkonow response sorry :(')
