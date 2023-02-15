import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import streamlit.components.v1 as components
        
load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('djkn.png'))

st.sidebar.header("Pilih Visualisasi")

st.header('KPKNL Banjarmasin')

st.markdown("<h3 style='text-align: center; color: black;'>Wani Barasih, Ikhlah Bagawi, Integritas Tanpa Batas</h3>", unsafe_allow_html=True)

icon_size = 20

st.sidebar.header("Configuration")
st_button('doc', 'https://linktr.ee/wadaimanis', 'Layanan Pengelolaan Kekayaan Negara', icon_size)
st_button('doc', 'https://youtube.com/codingprofessor', 'Layanan Lelang', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Layanan Penilaian', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Layanan Piutang Negara', icon_size)

st.markdown("<h5 style='text-align: center; color: black;'>Ikuti Kami</h5>", unsafe_allow_html=True)





components.html(
    """
        <a href="https://twitter.com/kpknl_bmasin" class="twitter-share-button" 
        data-text="Check my cool Streamlit Web-App🎈" 
        data-url="https://streamlit.io"
        data-show-count="false">
        data-size="Large" 
        data-hashtags="streamlit,python"
        Tweet
        </a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
)
