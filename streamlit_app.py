import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
        
load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('djkn.png'))

st.sidebar.header("Pilih Visualisasi")

st.header('KPKNL Banjarmasin')

st.markdown("<h1 style='text-align: center; color: red;'>'Wani Barasih, Ikhlah Bagawi, Integritas Tanpa Batas'</h1>", unsafe_allow_html=True)

icon_size = 20

st.sidebar.header("Configuration")
st_button('doc', 'https://linktr.ee/wadaimanis', 'Layanan Pengelolaan Kekayaan Negara', icon_size)
st_button('doc', 'https://youtube.com/codingprofessor', 'Layanan Lelang', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Layanan Penilaian', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Layanan Piutang Negara', icon_size)

if __name__ == __main__:
        main()
