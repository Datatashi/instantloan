import streamlit as st
import pandas as pd
import pickle

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from PIL import Image

img = Image.open("./logoai.png")


st.sidebar.image(img, width= 200)

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)
# df = pd.read_csv("./il.csv")

# df['LOAN_STATUS'] = (
#                 (df['AGE'].gt(17))
#                 &(df['CREDIT_CARD'].eq(1))
#                 &(df['CURR_BAL'].gt(2500))
#             ).astype(int)

# X = data_ml.iloc[0:764,0:3]
# y = data_ml.iloc[0:764,3]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# model = DecisionTreeRegressor(random_state=1)
# model.fit(X_train, y_train)


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





