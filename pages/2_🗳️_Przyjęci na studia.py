import streamlit as st
import pandas as pd
import numpy as np
from functools import reduce
import plotly.graph_objects as go

##-------------------------------------------------
st.set_page_config(
    page_title="Przyjęci na studia",
    page_icon="🗳️",
    layout="wide")


streamlit_style = """
<style>
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

html, body, [class*="css"]  {
font-family: 'Lato';
}
</style>
"""
st.markdown(streamlit_style, unsafe_allow_html=True)

data_irk = pd.read_parquet(r'Dane/data3.parquet')
to_plot = data_irk.query(f"czy_przyjety == 'admitted'")

to_plot.groupby(['rok', 'studia']).count()['czy_przyjety'].reset_index()

data_pl = pd.read_csv(r'Dane/all_candidates_pol_ex.csv', index_col = 0).dropna(axis=0, subset = ['wojewodztwo'])
data_pl = data_pl[data_pl['czy_przyjety'] == 'admitted']

##----------MAPKI OGÓŁEM

st.markdown('W poniższej części za przyjęcie na studia będziemy uznawać każdą rejestrację w systemie IRK, która została rozpatrzona pozytywnie.')
title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba osób przyjętych na studia na UMK z uwzględnieniem zamieszkiwanego województwa</b></p>'
st.markdown(title, unsafe_allow_html=True)    
left, cen, right = st.columns(3)
with left:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2022 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2022').query(f"czy_przyjety == 'admitted'").groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2022.png')
with cen:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2023 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2023').query(f"czy_przyjety == 'admitted'").groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2023.png')
    
with right:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Zmiana w roku 2023 względem 2022 [%]</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyrosty_przyjec_2023.png')

##----------MAPKI 1ST

title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba osób przyjętych na studia pierwszego stopnia na UMK z uwzględnieniem zamieszkiwanego województwa</b></p>'
st.markdown(title, unsafe_allow_html=True)    
left, cen, right = st.columns(3)

with left:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2022 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2022').query(f"czy_przyjety == 'admitted'").query('stopien == 1').groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2022_1st.png')
    
with cen:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2023 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2023').query(f"czy_przyjety == 'admitted'").query('stopien == 1').groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2023_1st.png')
    
with right:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Zmiana w roku 2023 względem 2022 [%]</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyrosty_przyjec_2023_1st.png')

##----------MAPKI 2ST

title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba osób przyjętych na studia drugiego stopnia na UMK z uwzględnieniem zamieszkiwanego województwa</b></p>'
st.markdown(title, unsafe_allow_html=True)    
left, cen, right = st.columns(3)

with left:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2022 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2022').query(f"czy_przyjety == 'admitted'").query('stopien == 2').groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2022_2st.png')
with cen:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>2023 (łącznie: {})</b></p>'.format(data_pl.query('rok == 2023').query(f"czy_przyjety == 'admitted'").query('stopien == 2').groupby('wydzial').count()['kampus'].reset_index().sum(numeric_only=True).values[0])
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyjecia_2023_2st.png')
    
with right:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Zmiana w roku 2023 względem 2022 [%]</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/przyrosty_przyjec_2023_2st.png')





















##------------GENERATOR


new_title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba osób przyjętych na studia na wskazanych kierunkach na UMK w latach 2020-2023</b></p>'
st.markdown(new_title, unsafe_allow_html=True)


left, cen = st.columns([0.33, 0.67])
with left:
    stopien =  st.selectbox(
        'Proszę wybrać stopień',
        ('Razem', 'Studia pierwszego stopnia i jednolite', 'Studia drugiego stopnia'))

    stopien_dict = {'Studia pierwszego stopnia i jednolite': 1, 'Studia drugiego stopnia': 2}

    if stopien != 'Razem':
        to_plot = to_plot.query(f"stopien == {stopien_dict[stopien]}")

    forma =  st.selectbox(
        'Proszę wybrać tryb',
        ('Razem', 'Studia stacjonarne', 'Studia niestacjonarne'))

    if forma != 'Razem':
        to_plot = to_plot.query(f"forma_studiow == '{forma.split(' ')[1]}'")

with cen:
    kierunki = st.multiselect('Proszę wybrać kierunki', sorted(list(to_plot['studia'].unique())))
    
left_co, cent_co,last_co = st.columns([.1, .8, .1])
with cent_co:
    ys = {}
    maxs = []
    fig2 = go.Figure()
    for kier in kierunki:
        ys[kier] = to_plot.query(f'studia == "{kier}"').groupby('rok').count()['kampus'].values
        maxs.append(max(ys[kier]))
        fig2.add_trace(
            go.Scatter(x=list(list(range(2020, 2024))),
                       y=ys[kier],
                       name=kier,
                       #line=dict(color="#0050AA")
                      )) 
        fig2.update_yaxes(range=[0, 1.2*max(maxs)])
    fig2.update_layout(
        font_family="Lato",
        font_color="black"
    )

    fig2.update_xaxes(type='category')

    #fig2.update_layout(title_text= title)

    st.plotly_chart(fig2)


###
new_title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Procentowa zmiana liczby osób przyjętych na studia na wskazanych kierunkach względem roku 2020</b></p>'
st.markdown(new_title, unsafe_allow_html=True)

left1, cen1 = st.columns([0.33, 0.67])
with left1:
    stopien_zmiana =  st.selectbox('Proszę wybrać stopień',
        ('Razem', 'Studia pierwszego stopnia i jednolite', 'Studia drugiego stopnia'), key = 'a')

    stopien_dict = {'Studia pierwszego stopnia i jednolite': 1, 'Studia drugiego stopnia': 2}

    if stopien_zmiana != 'Razem':
        to_plot = to_plot.query(f"stopien == {stopien_dict[stopien]}")

    forma_zmiana =  st.selectbox(
        'Proszę wybrać tryb',
        ('Razem', 'Studia stacjonarne', 'Studia niestacjonarne'), key = 'b')

    if forma_zmiana != 'Razem':
        to_plot = to_plot.query(f"forma_studiow == '{forma.split(' ')[1]}'")

with cen1:
    kierunki_zmiana = st.multiselect('Proszę wybrać kierunki', sorted(list(to_plot['studia'].unique())), key='c')
    
left_co, cent_co,last_co = st.columns([.1, .8, .1])
with cent_co:
    ys = {}
    maxs = []
    fig3 = go.Figure()
    for kier in kierunki_zmiana:
        df = to_plot.groupby(['rok', 'studia']).count()['czy_przyjety'].reset_index().query(f'studia == "{kier}"').reset_index(drop=True)
        plotting = []
        start = df.iloc[0,-1]
        for i, rok in enumerate(df['rok'].unique()):
            plotting.append(df.iloc[i, -1] / start*100)
        ys[kier] = plotting
        maxs.append(max(ys[kier]))
        fig3.add_trace(
            go.Scatter(x=list(list(range(2020, 2024))),
                       y=ys[kier],
                       name=kier,
                       #line=dict(color="#0050AA")
                      )) 
        fig3.update_yaxes(range=[0, 1.2*max(maxs)])
    fig3.update_layout(
        font_family="Lato",
        font_color="black"
    )
    fig3.update_layout(title_text= 'Procentowa zmiana liczby osób przyjętych na studia względem 2020 roku [%]')
    fig3.update_xaxes(type='category')

    st.plotly_chart(fig3)
