import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image



st.set_page_config(
    page_title="Home",
    page_icon="👋",
)


form = st.form(key="my_form")
anun = form.text_input("anun","")
azganun = form.text_input("azganun","")
haeranun = form.text_input("haeranun","")
submit_button = form.form_submit_button(label="Submit")



if submit_button:
    st.markdown(f"## Data is being analyzed go to the analyze page to see the results")
    st.page_link("pages/1_analyze.py")
    st.page_link("pages/2_contacts.py", label="Contacts")
    st.session_state["anun"] = anun
    st.session_state["azganun"] = azganun
    st.session_state["haeranun"] = haeranun
