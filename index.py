import streamlit as st

# Set page title and configuration
st.set_page_config(page_title="Simple Calculator", page_icon="🔢")

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Streamlit UI
def main():
    st.title("🔢 Simple Calculator")
    st.write("Welcome to the Simple Calculator App!")
    
    # Sidebar for operation selection
    st.sidebar.header("Select Operation")
    operation = st.sidebar.selectbox("Choose an operation:", ["Add", "Multiply"])
    
    # Input fields
    st.header("Enter Numbers")
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("First Number", value=0.0, step=1.0)
    
    with col2:
        num2 = st.number_input("Second Number", value=0.0, step=1.0)
    
    # Calculate button
    if st.button("Calculate", type="primary"):
        if operation == "Add":
            result = add(num1, num2)
            st.success(f"The sum of {num1} and {num2} is: **{result}**")
        elif operation == "Multiply":
            result = multiply(num1, num2)
            st.success(f"The product of {num1} and {num2} is: **{result}**")
    
    # Display some information
    st.divider()
    st.info("This app demonstrates basic arithmetic operations using Streamlit!")
    
    # Example calculations
    with st.expander("See Example Calculations"):
        st.write("**Addition Examples:**")
        st.write("• 5 + 3 = 8")
        st.write("• 10 + 7 = 17")
        st.write("")
        st.write("**Multiplication Examples:**")
        st.write("• 4 × 3 = 12")
        st.write("• 6 × 8 = 48")

# Run the app
if __name__ == "__main__":
    main()