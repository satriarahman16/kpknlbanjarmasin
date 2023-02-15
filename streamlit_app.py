import streamlit as st
import base64
from st_functions import st_button, load_css
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title='KPKNL Banjarmasin', page_icon='🏢', layout="centered", initial_sidebar_state="auto", menu_items=None)
load_css()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.imgur.com/jLXXa3D.jpg");
background-size: 110%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

col1, col2, col3 = st.columns(3)
col2.image(Image.open('djkn.png'))

st.sidebar.header("Pilih Visualisasi")

st.header('KPKNL Banjarmasin')

st.markdown("<h3 style='text-align: center; color: black;'>Wani Barasih, Ikhlah Bagawi, Integritas Tanpa Batas</h3>", unsafe_allow_html=True)

icon_size = 20
st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.header("Configuration")
st_button('doc', 'https://linktr.ee/wadaimanis', 'Layanan Pengelolaan Kekayaan Negara', icon_size)
st_button('doc', 'https://youtube.com/codingprofessor', 'Layanan Lelang', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Layanan Penilaian', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Layanan Piutang Negara', icon_size)

st.markdown("<h5 style='text-align: center; color: black;'>Ikuti Kami</h5>", unsafe_allow_html=True)

# column1, column2, column3, column4 = st.columns(4)

# column1.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column2.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column3.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column4.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
