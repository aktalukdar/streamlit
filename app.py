import streamlit as st 
import spacy
from spacy import displacy
import wiki
nlp = spacy.load("en_core_web_sm")

HTML_WRAPPER = """<div style="overflow-x: auto; padding: 1rem">{}</div>"""

st.title("Welcome to Streamlit app")

st.subheader("Named Entity Recognition")
input_data = st.text_area("Enter Wikipedia Title Here","")
if st.button("Enter"):

    title=wiki.getData(input_data)
    docx = nlp(title)
    html = displacy.render(docx,style="ent")
    st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
    st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)


