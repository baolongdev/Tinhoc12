import streamlit as st
from utils.Management import *
from utils.Dashboard import *
from exercises import *

from PIL import Image

def Sidebar(current_dir):
    banner = current_dir / "assets" / "img" / "logoDoan_Truong.png"
    banner = Image.open(banner)
    with st.sidebar:
        st.image(banner)
        st.title("12CTin | 21-24")
        selected_page = st.empty()
        
        st.divider()
        sidebar_container = st.container()

        st.title("Support")
        st.success(
            """
            For any issues using the app, contact: 
            longle12042006a@gmail.com
            """
        )
    
    page_names_to_funcs = {
        "✨Bài tập ma trận và định thức": {"func":matrices_determinants, "id": 0}, 
        "✨Maximun A Posteriori": {"func":maximun_a_posteriori, "id": 1}, 
        "📁File Management": {"func":Management, "id": 2},
    }
    def select_page():
        st.experimental_set_query_params(
            page=st.session_state.select_page
        )
        st.toast(f"Welcom to {st.session_state.select_page}")
        st.balloons()
        pass
    
    if "index_page" not in st.session_state:
        st.session_state["index_page"] = 0
    
    if "page" in st.experimental_get_query_params():
        page = str(st.experimental_get_query_params()["page"][0])
        if page in page_names_to_funcs:
            st.session_state.index_page = page_names_to_funcs[page]["id"]
            page_names_to_funcs[page]["func"](sidebar_container)
            with selected_page:
                st.selectbox(
                    "Select a page", 
                    page_names_to_funcs.keys(), 
                    key ="select_page", 
                    on_change=select_page,
                    index=st.session_state.index_page
                )
        else:
            st.warning(f"Page Not Found {st.experimental_get_query_params()['page'][0]}! ")
            with selected_page:
                if st.button("Go home!"):
                    st.experimental_set_query_params(
                        page="📁File Management"
                    )
    else:
        st.experimental_set_query_params(page="📁File Management")
        st.experimental_rerun()