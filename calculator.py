import streamlit as st
import math as m

# Define the main function to build the calculator
def main():
    st.title("🧮 Simple Arithmetic Calculator")

    # Get user input for the two numbers
    num1 = st.number_input("Enter the first number:",step=0)
    num2 = st.number_input("Enter the second number:",step=0)

    operation = st.radio("Select an operation to perform:",
                        ("➕", "➖", "✖️", "➗","sin", "cos", "tan", "√"),index= None)
    ans = 0
    
    def calculate():
        if operation == "➕":
            ans = num1 + num2
        elif operation == "√":
            ans = m.sqrt(num1)
        elif operation == "sin":
            ans = m.sin(num1)
        elif operation == "cos":
            ans = m.cos(num1)
        elif operation == "tan":
            ans = m.tan(num1)
        elif operation == "➖":
            ans = num1 - num2
        elif operation == "✖️":
            ans = num1 * num2
        elif operation=="➗" and num2!=0:
            ans = num1 / num2
        else:
            st.warning("Please enter a non-zero number.")
            ans = "Not defined"
    
        st.success(f"Answer = {ans}")


    if st.button("Calculate result"):
        calculate()

if __name__ == "__main__":
    main()