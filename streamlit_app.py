import streamlit as st
from st_functions import st_button, load_css, st_buttonmed
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title='KPKNL Banjarmasin', page_icon='🏢', layout="centered", initial_sidebar_state="auto", menu_items=None)
load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('djkn.png'))


st.sidebar.radio("Pilih Visualisasi",["Pengeloaan Kekayaan Negara","Lelang","Penilaian","Piutang Negara"])


st.header('KPKNL Banjarmasin')

st.markdown("<h3 style='text-align: center; color: black;'>Wani Barasih, Ikhlah Bagawi, Integritas Tanpa Batas</h3>", unsafe_allow_html=True)

icon_size = 20
st.sidebar.header("Configuration")
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

  
 

# column1, column2, column3, column4 = st.columns(4)

# column1.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column2.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column3.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)
# column4.markdown(“[![Title](<'instagram.png'>)](<'https://www.instagram.com/kpknlbanjarmasin/'>)”)




import json

with open('kota.geojson') as file_json:
    data = json.load(file_json)

data["features"] = [x for x in data["features"] if x["properties"]["NAME_1"] == "Kalimantan Selatan"]

import pandas as pd
df_ok = pd.read_csv("kotakabupaten_kalselok.csv")


from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Jumlah Penduduk Kota/Kabupaten pada Kalimantan Selatan Berdasarkan Rentang Usia'),
    html.P("Pilih Rentang Usia:"),
    dcc.RadioItems(
        id='candidate', 
        options=["Usia(0-30)","Usia(31-60)","Usia(>60)"],
        value="Usia(0-30)",
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):
    df = df_ok # replace with your own data source
    geojson = data
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="Kota_Kabupaten", featureidkey="properties.NAME_2",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


app.run_server(debug=True)
