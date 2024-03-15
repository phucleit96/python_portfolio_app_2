import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photophuc.jpg", width=400)
with col2:
    st.title('Phuc Le')
    content = """
    Hello, I'm Phuc Le, a Vietnamese data enthusiast with 1.5 years of self-taught experience under my belt, I'm passionate about using Python and its frameworks (Django, Flask, FastAPI) to solve problems (web development, data automation, data science, ...). My skillset also extends to Figma, Powerpoint, Canva, SQL and PowerBI, HTML, CSS, JS. With a strong desire to learn, tackle challenges and record the process, I hope to become a valuable asset in any data-driven environment and play a pivotal role in any team.
    """
    st.write(content)

    st.markdown(
        "**Below you can find some of the apps I have built in Python and Source Code in Github, feel free to contact "
        "me!**")

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])

