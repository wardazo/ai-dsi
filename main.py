import streamlit as st
import openai

openai.api_key = ""
txt = st.text_input('Where would you like to see an ant?')
st.write(f"a  ant in {txt} ")

option = st.selectbox(
    'What type of image would you like',
    ('None', 'Cartoon'))

btn = st.button('Create')

if btn:

    st.write(f" {option} ")

    if option != "None":
        txt = f"ant in {txt} in {option} style"
    else:
        txt = f"ant in {txt}"

    response = openai.Image.create(
        prompt=txt,
        n=5,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    for i in response['data']:
        print(i['url'])
        st.image(i['url'])
