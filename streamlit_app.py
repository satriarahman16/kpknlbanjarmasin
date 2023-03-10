import streamlit as st
from st_functions import st_button, load_css, st_buttonmed
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title='KPKNL Banjarmasin', page_icon='🏢', layout="centered", initial_sidebar_state="auto", menu_items=None)
load_css()





test = st.sidebar.radio("Pilih Visualisasi",["Home","Pengeloaan Kekayaan Negara","Lelang","Penilaian","Piutang Negara"])

if test == "Home":
 col1, col2, col3 = st.columns(3)
 col2.image(Image.open('djkn.png'))

 st.header('KPKNL Banjarmasin')

 st.markdown("<h3 style='text-align: center; color: black;'>Wani Barasih, Ikhlah Bagawi, Integritas Tanpa Batas</h3>", unsafe_allow_html=True)

 icon_size = 20
 # st.sidebar.header("Configuration")
 st_button('doc', 'https://linktr.ee/wadaimanis', icon_size, 'Layanan Pengelolaan Kekayaan Negara')
 st_button('doc', 'https://youtube.com/codingprofessor', icon_size, 'Layanan Lelang' )
 st_button('doc', 'https://data-professor.medium.com/',  icon_size, 'Layanan Penilaian')
 st_button('doc', 'https://twitter.com/thedataprof/', icon_size, 'Layanan Piutang Negara')

 # st.markdown("<h5 style='text-align: center; color: black;'>Ikuti Kami</h5>", unsafe_allow_html=True)

 # st_button('instagram', 'https://www.instagram.com/kpknlbanjarmasin/', '@kpknlbanjarmasin', icon_size)
 # st_button('facebook', 'https://www.facebook.com/kpknl.banjarmasin/', 'KPKNL Banjarmasin', icon_size)
 # st_button('twitter', 'https://twitter.com/kpknl_bmasin', '@kpknl_bmasin', icon_size)

 col1_nest,col2_nest,col3_nest,col4_nest = col2.columns(4)
 with col2:
  with col1_nest:
   st_buttonmed('instagram', 'https://www.instagram.com/kpknlbanjarmasin/', icon_size)
  with col2_nest:
   st_buttonmed('facebook', 'https://www.facebook.com/kpknl.banjarmasin/', icon_size)
  with col3_nest:
   st_buttonmed('twitter', 'https://twitter.com/kpknl_bmasin', icon_size)
  with col4_nest:
   st_buttonmed('youtube', 'https://www.youtube.com/@kpknlbanjarmasin/', icon_size)

 
if test == "Pengeloaan Kekayaan Negara":
 st.subheader("Ini Halaman untuk Pengelolaan Kekayaan Negara")
 
 
if test == "Lelang":
 st.subheader("Ini Halaman untuk Lelang")
 
if test == "Penilaian":
 st.subheader("Ini Halaman untuk Penilaian")

if test == "Piutang Negara":
 st.subheader("Ini Halaman untuk Piutang Negara")

# column1, column2, column3, column4 = st.columns(4)

# column1.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column2.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column3.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column4.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
