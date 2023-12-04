import streamlit as st
# create interactive web applications with Python.
from txtai.pipeline import Summary, Textractor
# perform text summarization using a pre-trained model.
from PyPDF2 import PdfReader
# extract text from PDF files.
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")
# Sets the layout of the page to be wide.

@st.cache_resource
# function uses the Hugging Face Transformers library's pre-trained summarization
# model to generate a summary of the input text.
def text_summary(text, maxlength=None):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

def extract_text_from_pdf(file_path):
# This function takes a file path to a PDF and extracts the text from the first
# page using `PyPDF2`.
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.radio("Select your choice", ["Summarize Text", "Summarize Document"])
# Displays a radio button for the user to choose between summarizing text or a document.

if choice == "Summarize Text":
# If the user chooses "Summarize Text":
    st.subheader("Summarize Text")
    input_text=''
    col1, col2 = st.columns([1,1])
    with col1:
        input_text = st.text_area("**Enter your text here**")
        #  Provides a text area for the user to input the text.
        if input_text is not None:
            if st.button("Summarize Text"):
                with col2:
                    if(len(input_text)<=0):
                        # it checks if the input text is not empty, and if not, it generates
                        # a summary using the `text_summary` function and displays the result.
                        st.error("Please enter text")
                    else:
                        st.markdown("**Summary Result**")
                        result = text_summary(input_text)
                        st.success(result)

    if(len(input_text)>0):
                    with st.expander("See input text"):
                        st.info(input_text)
                

elif choice == "Summarize Document":
    # If the user chooses "Summarize Document
    st.subheader("Summarize Document")
    input_file = st.file_uploader("Upload your document here", type=['pdf'])
    # Provides a file uploader for the user to upload a PDF document.
    if input_file is not None:
        if st.button("Summarize Document"):
        # If a file is uploaded and the "Summarize Document" button is clicked:
            with open("doc_file.pdf", "wb") as f:
                # It saves the uploaded file as "doc_file.pdf".
                f.write(input_file.getbuffer())
                st.info("File uploaded successfully")
            st.markdown("**Your Summary here**")
            text = extract_text_from_pdf("doc_file.pdf")
            # Extracts text from the PDF file using `extract_text_from_pdf`.
            doc_summary = text_summary(text)
            # Generates a summary using `text_summary`.
            st.success(doc_summary)
            with st.expander("See extracted text"):
                # Displays the document summary and the extracted text in an expander if the user clicks to expand.
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("**Extracted Text is Below:**")
                st.info(extracted_text)