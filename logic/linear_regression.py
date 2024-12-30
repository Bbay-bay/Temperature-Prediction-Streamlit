import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error


def preparer(data:pd.DataFrame):
    data['Date'] = pd.to_datetime(data['Date'])
    data['Jour'] = data['Date'].dt.day
    data['Mois'] = data['Date'].dt.month
    data['Temperature moyenne mobile'] = data['Temperature moyenne (°C)'].rolling(window=30).mean()
    data['Humidite moyenne mobile'] = data['Humidite moyenne (%)'].rolling(window=30).mean()
    data=data.dropna()
    return data

def scaler(data:pd.DataFrame):
    stand_scaler=StandardScaler()
    data_scaled=stand_scaler.fit_transform(data[['Precipitation (mm)','Humidite moyenne (%)','Temperature moyenne mobile','Humidite moyenne mobile']])
    data_scaled= pd.DataFrame(data_scaled,columns=['Precipitation (mm)','Humidite moyenne (%)','Temperature moyenne mobile','Humidite moyenne mobile'],index=data.index)
    data_scaled = pd.concat([data[['Date','Temperature moyenne (°C)','Jour','Mois']].reset_index(drop=True), data_scaled.reset_index(drop=True)], axis=1)
    return [data_scaled,stand_scaler]

def train_model(data):
    x = data.drop(['Temperature moyenne (°C)','Date'],axis=1,inplace=False)
    y = data['Temperature moyenne (°C)'].copy()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    return [mse,r2,mae,regr]

def predict(model,scaler,jour,mois,precipitation,humidite,temp_moyenne_mobile,hum_moyenne_mobile):
    train_features = ['Jour', 'Mois','Precipitation (mm)','Humidite moyenne (%)','Temperature moyenne mobile','Humidite moyenne mobile']
    input_data = {
    'Jour': jour,
    'Mois': mois,
    'Precipitation (mm)': precipitation,
    'Humidite moyenne (%)': humidite,
    'Temperature moyenne mobile': temp_moyenne_mobile,
    'Humidite moyenne mobile': hum_moyenne_mobile,
    }
    input_df = pd.DataFrame([input_data])
    input_df_scaled=scaler.transform(input_df[['Precipitation (mm)', 'Humidite moyenne (%)', 'Temperature moyenne mobile', 'Humidite moyenne mobile']])
    input_df_scaled= pd.DataFrame(input_df_scaled,columns=['Precipitation (mm)', 'Humidite moyenne (%)', 'Temperature moyenne mobile', 'Humidite moyenne mobile'],index=input_df.index)
    input_df_scaled = pd.concat([input_df[['Jour','Mois']].reset_index(drop=True), input_df_scaled.reset_index(drop=True)], axis=1)
    predicted_temperature = model.predict(input_df_scaled)
    return predicted_temperature