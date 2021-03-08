import streamlit as st
from pickle import dump
import pandas as pd
import numpy as np

st.title('Machine Learning Model')
col1 = st.text_input("enter an value:")
col2 = st.text_input("enter an value")
df2=np.array([col1,col2]).reshape(1,-1)
def standardization (df2):
    from sklearn.preprocessing import StandardScaler
    standardized_data = StandardScaler().fit_transform(df2)
def predict(df2):
    dump(standardized_data,open('standardizer.pkl','rb'))
    dump(classifier,open('random_.pkl','rb'))
    prediction = classifier.predict(df2)
click = st.button('SUBMIT')
if click:
    def main():

        standardization(df2)
        predict(df2)
    if click:
        def main():

            standardization(df3)
            predict(df4)
        if predict==0:
            st.write('0 ')
        # elif predict==1:
        else:
            st.write('1')
        # else:
        #     st.write('None')

    # else:
    #     st.write('None')
