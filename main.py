import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photophuc.jpg", width=600)
with col2:
    st.title('Phuc Le')
    content = """
    Hello, I'm Phuc Le, a VNese data enthusiast with 2 years of self-taught experience under my belt, I'm passionate about using Python and its frameworks (Django, Flask, FastAPI) to solve problems (web development, data automation, data science, ...). My skillset also extends to Figma, Powerpoint, Canva, SQL and PowerBI, HTML, CSS, JS. With a strong desire to learn, tackle challenges and record the process, I hope to become a valuable asset in any data-driven environment and play a pivotal role in any team.
    """
    st.info(content)
