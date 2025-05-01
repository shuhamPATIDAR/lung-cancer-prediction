import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from imblearn.over_sampling import ADASYN
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, f1_score
import joblib
df = pd.read_csv("lungcancerdataset.csv")

le=preprocessing.LabelEncoder()
df['GENDER']=le.fit_transform(df['GENDER'])
df['SMOKING']=le.fit_transform(df['SMOKING'])
df['YELLOW_FINGERS']=le.fit_transform(df['YELLOW_FINGERS'])
df['ANXIETY']=le.fit_transform(df['ANXIETY'])
df['PEER_PRESSURE']=le.fit_transform(df['PEER_PRESSURE'])
df['CHRONIC DISEASE']=le.fit_transform(df['CHRONIC DISEASE'])
df['FATIGUE ']=le.fit_transform(df['FATIGUE '])
df['ALLERGY ']=le.fit_transform(df['ALLERGY '])
df['WHEEZING']=le.fit_transform(df['WHEEZING'])
df['ALCOHOL CONSUMING']=le.fit_transform(df['ALCOHOL CONSUMING'])
df['COUGHING']=le.fit_transform(df['COUGHING'])
df['SHORTNESS OF BREATH']=le.fit_transform(df['SHORTNESS OF BREATH'])
df['SWALLOWING DIFFICULTY']=le.fit_transform(df['SWALLOWING DIFFICULTY'])
df['CHEST PAIN']=le.fit_transform(df['CHEST PAIN'])
df['LUNG_CANCER']=le.fit_transform(df['LUNG_CANCER'])

#Note: Male =1 AND Females = 0

#Splitting the Independent And Dependent features
X=df.drop('LUNG_CANCER',axis=1)
Y=df['LUNG_CANCER']

#Fixing the imbalance dataset using the ADASYN technique
adasyn = ADASYN(random_state=42)
X,Y=adasyn.fit_resample(X,Y)

#Logestic Regression 

#splitting the dataset for training and testing
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
#Here random_state =0 state that the split will be same every time you run the code

#fitting the data to the model

lr_model=LogisticRegression(random_state=0)
lr_model.fit(X_train,Y_train)

#predicting the result using the test data
Y_lr_predict=lr_model.predict(X_test)
#Y_lr_predict

#Saving the model to pickle file
joblib.dump(lr_model, 'lung_cancer_model.pkl')
#Model Accuracy

#lr_cr=classification_report(Y_test,Y_lr_predict)
#print(lr_cr)