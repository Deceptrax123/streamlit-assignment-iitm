import streamlit as st 

def find_largest(a, b, c):
    largest = max(a, b, c)
    return largest

if __name__=='__main__':
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers:")
    a = st.number_input("Number 1", min_value=0)
    b = st.number_input("Number 2", min_value=0)
    c = st.number_input("Number 3", min_value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.write("The largest number is:", largest)