import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")

@st.cache_resource
def text_summary(text, maxlength=None):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.radio("Select your choice", ["Summarize Text", "Summarize Document"])

if choice == "Summarize Text":
    st.subheader("Summarize Text")
    input_text=''
    col1, col2 = st.columns([1,1])
    with col1:
        input_text = st.text_area("**Enter your text here**")
        if input_text is not None:
            if st.button("Summarize Text"):
                with col2:
                    if(len(input_text)<=0):
                        st.error("Please enter text")
                    else:
                        st.markdown("**Summary Result**")
                        result = text_summary(input_text)
                        st.success(result)

    if(len(input_text)>0):
                    with st.expander("See input text"):
                        st.info(input_text)
                

elif choice == "Summarize Document":
    st.subheader("Summarize Document")
    input_file = st.file_uploader("Upload your document here", type=['pdf'])
    if input_file is not None:
        if st.button("Summarize Document"):
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
                st.info("File uploaded successfully")
            st.markdown("**Your Summary here**")
            text = extract_text_from_pdf("doc_file.pdf")
            doc_summary = text_summary(text)
            st.success(doc_summary)
            with st.expander("See extracted text"):
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("**Extracted Text is Below:**")
                st.info(extracted_text)