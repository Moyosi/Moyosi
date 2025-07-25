import streamlit as st

def inverter(sentence):
    ans= ''
    import string
    for letter in sentence:
        if letter in string.ascii_lowercase:
            ans += letter.upper()
        elif letter in string.ascii_uppercase:
            ans += letter.lower()
        else:
            ans += letter
    return ans
    
    
st.title('Inverter')
st.header('This little puppy will invert upper and lower cases.')
needed = st.text_input('Input your sentence')
if st.button('Invert'):
    final = inverter(needed)
    st.write(final)
    


