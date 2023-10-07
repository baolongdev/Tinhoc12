from modules.database import *
import streamlit as st


def InitPageSetting(st, path, PAGE_NAME, PAGE_ICON, name_file_css=""):
    current_dir = path
    CSS_MAIN = current_dir / "assets" / "styles" / "main.css"
    st.set_page_config(PAGE_NAME, PAGE_ICON)
    if name_file_css:
        css_file = current_dir/"assets" / "styles" / name_file_css
        Custom_CSS(st, CSS_MAIN)
        Custom_CSS(st, css_file)
    else:
        Custom_CSS(st, CSS_MAIN)


def Custom_CSS(st, css_file):
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)


def Custom_Code(st, data):
    st.markdown(data, unsafe_allow_html=True)


def Custom_Title(st, title):
    st.subheader(title)
    st.markdown("#")
    
def download_button(label, file_path, key=None):
    with open(file_path, "rb") as f:
        file_contents = f.read()
    st.download_button(label, data=file_contents, file_name=file_path.split("/")[-1], key=key)