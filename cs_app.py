import numpy as np
import pickle
import pandas as pd
import streamlit as st


clean_data=pd.read_csv('C:\\Users\\Siva\\Desktop\\ExcelR\\Project3\\new\\data_clean.csv')
classifier = pickle.load(open('C:\\Users\\Siva\\Desktop\\ExcelR\\Project3\\new\\final_model.pkl', 'rb'))

clean_data.drop(['Unnamed: 0', 'Dclust'], axis=1, inplace=True)

model = classifier.fit(clean_data)


# Creating a function
# Customer segmentation function
def segment_customers(input_data):
    # Prepare the input data for prediction
    encoded_data = [input_data[0], input_data[1], input_data[2], input_data[3], input_data[4], input_data[5],
                    input_data[6], input_data[7],
                    input_data[8],input_data[9]]

    data=pd.DataFrame([encoded_data], columns=['Income', 'NumWebVisitsMonth', 'CustomerAge','Children', 'MntTotalProducts', 'NumTotalPurchases', 'Education_Graduation','Education_PostGraduation','Education_UnderGraduation','Marital_Status_Married'])

    
    prediction=model.predict(data)

    pred_1 = ""

    if prediction[0] == 0:  # Access the first element of the prediction array
        pred_1 = 'cluster 0'
    elif prediction[0] == 1:
        pred_1 = 'cluster 1'
    elif prediction[0] == 2:
        pred_1 = 'cluster 2'
    elif prediction[0] == 3:
        pred_1 = 'cluster 3'
    elif prediction[0] == 4:
        pred_1 = 'cluster 4'

    return pred_1

st.title('Customer Personality Analysis')

st.header('User Input Parameters')
def main():
    Income = st.number_input("Type In The Household Income", key="income", step=1)
    NumWebVisitsMonth = st.number_input("Number of visits to company’s website in the last month", key="num_visits",step=1)
    CustomerAge = st.slider("Select Age", 18, 85, key="age")
    st.write("Customer Age is", CustomerAge)
    Children = st.number_input("Number of Children", key="num_childern",step=1)

    #Children = st.radio("Select Number Of Children", ('0', '1', '2', '3'))
    MntTotalProducts = st.number_input("Total Amount spent", key="mtp", step=1)
    NumTotalPurchases = st.number_input("Number of total purchases", key="ntp", step=1)
    Education = st.radio("Select Education", ("Undergraduate", "Graduate", "Postgraduate"))
    Marital_Status_Married = st.radio("Married?", ('No', 'Yes'))

    # Convert selected values to corresponding numerical values
    #education_mapping = {'Undergraduate': 2, 'Graduate': 0, 'Postgraduate': 1}
    marital_status_mapping = {'No': 0, 'Yes': 1}
    
    ###########################
    
    Education_Graduation=0
    Education_PostGraduation=0
    Education_UnderGraduation=0
    
    if (Education == "Postgraduate"):
        Education_Graduation=0
        Education_PostGraduation=1
        Education_UnderGraduation=0
    elif (Education == "Graduate"):
        Education_Graduation=1
        Education_PostGraduation=0
        Education_UnderGraduation=0
    else:
        Education_Graduation=0
        Education_PostGraduation=0
        Education_UnderGraduation=1
    
    
    ##################################

    #Education = education_mapping[Education]
    Marital_Status_Married = marital_status_mapping[Marital_Status_Married]

    result = ""

    # When 'Segment Customer' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        input_data = [Income, NumWebVisitsMonth, CustomerAge, Children, MntTotalProducts, NumTotalPurchases,
                      Education_Graduation, Education_PostGraduation, Education_UnderGraduation, Marital_Status_Married]
        result = segment_customers(input_data)

    st.success(result)


if __name__ == '__main__':
    main()
