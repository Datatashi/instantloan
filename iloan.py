import streamlit as st
import pandas as pd
import pickle

from PIL import Image

img = Image.open("./logoai.png")

st.set_page_config(page_title="iLoan",
                   page_icon=img,
                   layout= "wide")
st.sidebar.image(img, width= 200)

pickle_in = open('rf.sav', 'rb')

model = pickle.load(pickle_in)
# model = pickle.load(open("model.sav", "rb"))

def main():
    st.subheader("Welcome to iLoan Application with Artificial Intelligence.")
    html_temp = """
    <div style = "background-color:#5252ff;"><p style = "color:White;font-size:44px;text-align:center;">TESTING INSTANT LOAN APPLICATION</p></div>
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

st.header("Applicant Information.")
st.write(user_data)


loan = model.predict(user_data)

st.header("iLoan status")
result = st.button("SUBMIT")
if result:
    if loan[0]== 0:
        st.warning(":pray: Your loan is Rejected!!! You don't have credit card or your minimum saving of past six months is below NU. 2500.")
    else:
        st.success(":sunglasses: Congratulations!!! Your loan is approved by Bank of Bhutan. Please wait while your loan is being process.")










