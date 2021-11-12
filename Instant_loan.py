import streamlit as st
import pandas as pd
import pickle

from PIL import Image

img = Image.open("D:/AI/logoai.png")

st.set_page_config(page_title="8o8 Instant Loan",
                   page_icon=img,
                   layout= "wide")
st.sidebar.image(img, width= 200)

model = pickle.load(open("model.sav", "rb"))

def main():
    st.subheader("The Application with Artificial Intelligence.")
    html_temp = """
    <div style = "background-color:#5252ff;"><p style = "color:White;font-size:44px;text-align:center;">8o8 INSTANT LOAN APPLICATION</p></div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__=="__main__":
    main()

st.sidebar.header('Applicant Account details.')

def user_report():
    age = st.sidebar.slider("Age", 1,100,18)
    credit_card = st.sidebar.selectbox("Do you have Credit card?", (1, 0))
    balance_amount = st.sidebar.slider("Balance Amount in the Account", 0, 10000, 2500)


    user_report_data = {
        "age" :age,
        "credit_card": credit_card,
        "balance_amount": balance_amount
    }

    report_data = pd.DataFrame(user_report_data, index =[0])
    return report_data


user_data = user_report()

st.header("Applicant data")
st.write(user_data)


loan = model.predict(user_data)

st.header("Loan status")
result = st.button("SUBMIT")
if result:
    if loan[0]== 0:
        st.warning("you are NOT ELIGIBLE for the loan")
    else:
        st.success("you are ELIGIBLE for the loan")













# if Account_number == data["ACCTT_NO"]:
#     st.write()
#     st.write(data = {'Age': data["AGE"],'Credit_card': data["CREDIT_CARD"],'Current_Balance': data["CURR_BAL"]})
#
# def user_input_features():
#     Age = st.sidebar.slider("What is your age?", 1,100,18)
#     Credit_card = st.sidebar.selectbox('Do you have the Credit card?', (1,0))
#     Saving_Balance_Amount = st.sidebar.number_input("What is the Balance Amount in your account?")
#
#     df = {'Age': Age,
#             'Credit_card': Credit_card,
#             'Saving_Balance_Amount': Saving_Balance_Amount}
#     features = pd.DataFrame(df, index=[0])
#     return features
#
# df = user_input_features()
#
# st.subheader('Account Holder Input parameters')
# st.write(df)
#
# data = pd.read_csv("D:/AI/data_AI_IL.csv")

# X = data.iloc[0:764,0:3].values
# y = data.iloc[0:764,3].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
#
#
# # model = LogisticRegression()
# # model.fit(X_train, y_train)
#
# clf = RandomForestClassifier()
# clf.fit(X, y)
#
#
# #
# # prediction = clf.predict(df)
# # prediction_proba = clf.predict_proba(df)
#
# st.subheader('Parameters and the approval of corresponding Instant loan')
# st.write(df.INSTANT_LOAN)
#
# st.subheader('Prediction')
# st.write(df.INSTANT_LOAN[prediction])
# #st.write(prediction)
#
# st.subheader('Prediction Probability')
# st.write(prediction_proba)

#

# lr_prediction = model.predict(X_test)
#
# st.subheader('PREDICTION OF INSTANT LOAN')
# st.write(df["INSTANT_LOAN"])
#
# st.subheader('Prediction')
# st.write(df.INSTANT_LOAN[lr_prediction])
#
# st.write("Logistic Regression Accuracy:", metrics.accuracy_score(lr_prediction, y_test))
