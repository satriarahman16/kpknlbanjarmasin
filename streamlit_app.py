import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 120%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
"""

load_css()

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")


col1, col2, col3 = st.columns(3)
col2.image(Image.open('djkn.png'))



st.header('KPKNL Banjarmasin')

st.info('Kantor Pelayanan Kekayaan Negara dan Lelang Banjarmasin merupakan kantor vertikal dari Unit Eselon I Direktorat Jenderal Kekayaan Negara (DJKN) yang berada di wilayah kerja Kantor Wilayah DJKN Kalimantan Selatan dan Tengah.')

icon_size = 20

st.markdown(page_bg_img, unsafe_allow_html=True)
st_button('doc', 'https://linktr.ee/wadaimanis', 'Layanan Pengelolaan Kekayaan Negara', icon_size)
st_button('doc', 'https://youtube.com/codingprofessor', 'Layanan Lelang', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Layanan Penilaian', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Layanan Piutang Negara', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
