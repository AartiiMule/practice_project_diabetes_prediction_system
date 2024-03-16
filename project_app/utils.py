import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class Diabetic():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin 
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age
    
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)     

    def get_predicted_value(self):
        
        self.load_models()  
    
        
        test_array=np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.Glucose
        test_array[1]=self.BloodPressure
        test_array[2]=self.SkinThickness
        test_array[3]=self.Insulin
        test_array[4]=self.BMI
        test_array[5]=self.DiabetesPedigreeFunction
        test_array[6]=self.Age

        charges=self.model.predict([test_array])
        return charges
if __name__== "__main__":
    Glucose=148.000
    BloodPressure=50.000
    SkinThickness=35.000
    Insulin=0.000
    BMI=33.600
    DiabetesPedigreeFunction=0.627
    Age=50.000
    