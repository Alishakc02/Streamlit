import streamlit as st 
st.title('Coffee maker app')
if st.button('Make coffee'):
    st.success("Your coffee has been ready")


sugar=st.checkbox("Add sugar")

if sugar:
    st.write("Sugar has been added to your coffee.")
else:
    st.write("Sugar isn't available.")
    
    
type=st.radio("Select one of the following: ", ['cappucion', 'americano', 'espresso','black coffee'])
st.write(f'You have selected {type}. ', 'Thank you for the order.')

density= st.selectbox('Choose density of your coffee:', ['high','low','medium'])
st.write(f'You have selected {density} level.')


sugar_level=st.slider('sugar',0, 5, 3)
#Pure number

order=st.number_input("How many coffee?", min_value=4 , max_value=10, step=1)
st.write(f'You have ordered {order}')

#Pure text

name= st.text_input('Enter your name: ')
if name:
    st.write(f"Welcome {name}.", 'Your coffee is coming.')
else:
    st.write("We are out of stock for now.")


#Date of birth
dob= st.date_input("Select your date of birth:")
if dob:
    st.write(f'You were born on {dob}.')

