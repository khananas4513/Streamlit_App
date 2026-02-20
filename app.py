import streamlit as st
import pandas as pd
import numpy as np

#Displaying the title of the app
st.title("My First Streamlit App")
st.write("Welcome to my first Streamlit app!. Hello!!! Anas")
st.text("This is a simple app to demonstrate the capabilities of Streamlit.")  

#Creating charts using Pandas & Numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

#Sidebar, Image & Video
st.sidebar.header("Navigation")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
st.caption("Streamlit Logo")
st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")

#file csv upload
st.header("Upload a CSV file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# Taking user input
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to Streamlit.")

#Text & Markdown Formatting
st.header("Text & Markdown Formatting")
st.subheader("This is a subheader")
st.markdown("**This is bold text**")
st.markdown("*This is italic text*")
st.markdown("~~This is strikethrough text~~")
st.code("print('Hello, Streamlit!')", language="python")

st.text_input("Enter your name", key="name_input")
st.text_area("Enter your message", key="message_input")
st.number_input("Enter a number", min_value=0, max_value=100, key="number_input")
st.slider("Select a value", min_value=0, max_value=100, key="slider_input")
st.selectbox("Choose an option", options=["Campus", "Abros", "Calcetto"], key="selectbox_input")
st.multiselect("Select color", options=["Blue", "Green", "Red"], key="multiselect_input")
st.radio("Choose a gender", options=["Male", "Female", "Other"], key="radio_input")
st.checkbox("I agree to the terms and conditions", key="checkbox_input")


# Matplotlib Integration
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
st.pyplot(fig)