import streamlit as st

def calculate_final_amount(P, n, r, t):
    A = P * (1 + r/n)**(n*t)
    return A

st.title("Compound Interest Calculator")

# Sidebar with input fields
P = st.sidebar.number_input("Enter Principal Amount:", min_value=0)
n = st.sidebar.number_input("Enter Number of Times Compounded per Year:", min_value=1)
r = st.sidebar.number_input("Enter Annual Interest Rate (as a decimal):", min_value=0.0)
t = st.sidebar.number_input("Enter Number of Years:", min_value=0.0)

# Calculate the final amount
final_amount = calculate_final_amount(P, n, r, t)

# Display the result
st.write(f"The final amount after {t} years is: ${final_amount:.2f}")
