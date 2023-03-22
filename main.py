import streamlit as st
import openai

openai.api_key = st.secrets["APIKEY"]
txt = st.text_input(
    'Where would you like to see an ant?',
    help='Eg. "on an ice cream cone" or "in front of big ben"'
)
#st.write(f"a  ant in {txt} ")

option = st.selectbox(
    'What type of image would you like',
    ('None', 'Cartoon'))

btn = st.button('Create')

if btn:

    if option != "None":
        txt = f"ant {txt} in {option} style"
    else:
        txt = f"ant {txt}"

    response = openai.Image.create(
        prompt=txt,
        n=3,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    for i in response['data']:
        #print(i['url'])
        st.image(i['url'])
