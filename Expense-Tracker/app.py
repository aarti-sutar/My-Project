import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Expense Tracker")

date = st.date_input("Enter Date")
category = st.selectbox("Category", ["Food", "Travel", "Shopping"])
amount = st.number_input("Amount", min_value=0)

if st.button("Add Expense"):
    new_data = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount]
    })

    try:
        old_data = pd.read_csv("expenses.csv")
        data = pd.concat([old_data, new_data])
    except:
        data = new_data

    data.to_csv("expenses.csv", index=False)
    st.success("Expense Added!")

try:
    data = pd.read_csv("expenses.csv")
    st.write(data)

    st.subheader("Expense Chart")
    chart_data = data.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    chart_data.plot(kind="bar", ax=ax)
    st.pyplot(fig)

except:
    st.warning("No data yet")