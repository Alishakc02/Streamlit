import streamlit as st 
st.title('Hello world!!')
st.subheader('This is a subheader')
st.text("Welcome to your first interactive app!!")
st.write('Choose your favourite variety of coffee.')
coffee=st.selectbox('Your favourite coffee:',['cappucino','americano','espresso'])
st.write(f"You choose {coffee}. Excellent choice")
st.success('Your coffee has been brewed.')

#Now for the programming language
st.title("Programming language picker")
st.write("Choose your favourite programming language:")
programming=st.selectbox("Your favourite: ", ['C','C++','Python','Javascript','Java','C#'])
st.write(f'You have chosen {programming}. Nice work.')
st.success(f"You have great interest in {programming}")
