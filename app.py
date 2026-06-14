import streamlit as st
from main import Bank

st.set_page_config(page_title="Bank Management System")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Delete Account"
    ]
)

# CREATE ACCOUNT
if menu == "Create Account":

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create Account"):

        info = {
            "name": name,
            "age": str(age),
            "email": email,
            "pin": int(pin),
            "accountnumber": Bank._Bank__generate_account_number(),
            "balance": 0
        }

        if age < 18:
            st.error("Age must be 18+")

        elif len(str(pin)) != 4:
            st.error("PIN must be 4 digits")

        else:
            Bank.data.append(info)
            Bank._Bank__update()

            st.success("Account Created Successfully")
            st.info(f"Account Number: {info['accountnumber']}")

# DEPOSIT
elif menu == "Deposit Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):

        userdata = [
            i for i in Bank.data
            if i["accountnumber"] == acc
            and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")

        else:
            userdata[0]["balance"] += amount
            Bank._Bank__update()

            st.success("Money Deposited Successfully")

# WITHDRAW
elif menu == "Withdraw Money":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):

        userdata = [
            i for i in Bank.data
            if i["accountnumber"] == acc
            and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")

        elif userdata[0]["balance"] < amount:
            st.error("Insufficient Balance")

        else:
            userdata[0]["balance"] -= amount
            Bank._Bank__update()

            st.success("Money Withdrawn Successfully")

# ACCOUNT DETAILS
elif menu == "Account Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):

        userdata = [
            i for i in Bank.data
            if i["accountnumber"] == acc
            and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")

        else:
            st.json(userdata[0])

# DELETE ACCOUNT
elif menu == "Delete Account":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):

        userdata = [
            i for i in Bank.data
            if i["accountnumber"] == acc
            and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")

        else:
            Bank.data.remove(userdata[0])
            Bank._Bank__update()

            st.success("Account Deleted Successfully")