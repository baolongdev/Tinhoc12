from modules.FileManager import *
from pathlib import Path
import streamlit as st
from modules import *


def sidebarConfig(sidebar):
    with sidebar:
        pass

def customsGroup(current_dir):
    css__custom = f'{current_dir}/assets/styles/custom.css'
    Custom_CSS(st, css__custom)
    Custom_Code(st, """
            <div class="main__title"> 
                <h3> Maximun A Posteriori <h3>
            <div/>        
        """)

def main(sidebar):
    pass


def maximun_a_posteriori(sidebar):
    current_dir = Path(".")
    sidebarConfig(sidebar)
    customsGroup(current_dir)
    main(sidebar)