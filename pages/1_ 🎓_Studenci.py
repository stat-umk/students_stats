
import streamlit as st
import pandas as pd
import numpy as np
from functools import reduce
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components

##-------------------------------------------------
st.set_page_config(
    page_title="Studenci",
    page_icon="🎓",
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

stac = pd.read_excel(r'Dane/stacjonarne.xlsx', index_col = [0, 1, 2], header = [0, 1])
nstac = pd.read_excel(r'Dane/niestacjonarne.xlsx', index_col = [0, 1, 2], header = [0, 1])
razem = pd.read_excel(r'Dane/razem.xlsx', index_col = [0, 1, 2], header = [0, 1])

data_dict = {'Ogółem': razem, 'Stacjonarne': stac, 'Niestacjonarne': nstac}


##-----------LICZBA KIERUNKÓW

title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Oferta programowa UMK</b></p>'
st.markdown(title, unsafe_allow_html=True)  
left_co, cent_co,last_co = st.columns([.1, .8, .1])
with cent_co:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Liczba kierunków studiów oferowanych na UMK w latach 2009-2023</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/kierunki.png')
    
##------------UMK A UCZELNIE PUBLICZNE

title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>UMK a inne uczelnie publiczne</b></p>'
st.markdown(title, unsafe_allow_html=True)    
right, left = st.columns(2)
with right:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Udział UMK w liczbie uczestników studiów na uczelniach publicznych w Polsce w latach 2014-2022</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/UMK_publiczne_PL.png')
with left:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Liczba uczestników studiów na UMK oraz na pozostałych uczelniach publicznych w województwie kujawsko-pomorskim w latach 2014-2022</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/UMK_publiczne.png')

##------------LICZBA STUDENTÓW
    
title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba studentów</b></p>'
st.markdown(title, unsafe_allow_html=True) 
right, left = st.columns(2)
with right:    
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Liczba studentów studiów stacjonarnych na UMK w latach 2017-2022</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/studia_stacjonarne.png')
with left:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Liczba studentów studiów niestacjonarnych na UMK w latach 2017-2022</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/studia_niestacjonarne.png')


#-------------LICZBA STUDENTÓW W PODZIALE NA WYDZIAŁY
title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba studentów w podziale na wydziały</b></p>'
st.markdown(title, unsafe_allow_html=True) 

lata = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
kolor = {'fioletowy':'rgb(170,40,150)','niebieski':'rgb(0,175,250)','zielony':'rgb(0,165,80)','oliwkowy':'rgb(170,210,60)','pomarańczowy':'rgb(255,130,30)','czerwony':'rgb(250,20,20)'}
kolwyd1 = {'Nauk Biologicznych i Weterynaryjnych (od 2019)':kolor['oliwkowy'],'Biologii i Ochrony Środowiska (2012-2018)':kolor['zielony'],'Filologiczny (2010-2018)':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny (2010-2018)':kolor['niebieski'],'Humanistyczny (od 2019)':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych (od 2019)':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi (2012-2018)':kolor['zielony'],'Nauk Pedagogicznych (2010-2018)':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych (2010-2018)':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej (od 2019)':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie (od 2019)':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem':'rgb(0,80,170)','Ogółem UMK':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi (2010-2011)':kolor['zielony']}
kolwyd = {'Nauk Biologicznych i Weterynaryjnych':kolor['zielony'],'Biologii i Ochrony Środowiska':kolor['zielony'],'Filologiczny':kolor['niebieski'],
           'Chemii':kolor['oliwkowy'],'Humanistyczny':kolor['niebieski'],'Fizyki, Astronomii i Informatyki Stosowanej':kolor['oliwkowy'],
          'Filozofii i Nauk Społecznych':kolor['fioletowy'],'Matematyki i Informatyki':kolor['oliwkowy'],'Nauk Ekonomicznych i Zarządzania':kolor['fioletowy'],
          'Nauk Historycznych':kolor['niebieski'],'Nauk o Ziemi':kolor['zielony'],'Nauk Pedagogicznych':kolor['fioletowy'],'Politologii i Studiów Międzynarodowych':kolor['fioletowy'],
          'Nauk o Ziemi i Gospodarki Przestrzennej':kolor['oliwkowy'],'Nauk o Polityce i Bezpieczeństwie':kolor['fioletowy'],'Prawa i Administracji':kolor['fioletowy'],'Sztuk Pięknych':kolor['pomarańczowy'],
          'Teologiczny':kolor['zielony'],'Lekarski':kolor['czerwony'],'Farmaceutyczny':kolor['czerwony'],'Nauk o Zdrowiu':kolor['czerwony'],'Ogółem UMK':'rgb(0,80,170)','Ogółem':'rgb(0,80,170)',
	 'Interdyscyplinarne Centrum Nowoczesnych Technologii':kolor['oliwkowy'],'Biologii i Nauk o Ziemi':kolor['zielony'],'Nauk Politologii i Studiów Międzynarodowych':kolor['fioletowy'],}


q1, q2 = st.columns(2)
kat34 = q1.selectbox('Proszę wybrać tryb studiów: ',['Ogółem','Studia stacjonarne','Studia niestacjonarne'])

DF7 = pd.read_pickle(r'Dane/pick/L_kier_stud.pickle')
DF7['Rok'] = DF7['Rok'].astype('str')
DF8 = pd.read_pickle(r'Dane/pick/N-wni.pickle')
DF8['Rok'] = DF8['Rok'].astype('int')
DF9 = pd.read_pickle(r'Dane/pick/Z-czni.pickle')
DF9['Rok'] = DF9['Rok'].astype('int')
DF10 = pd.read_pickle(r'Dane/pick/Stacjonarne.pickle')
DF10['Rok'] = DF10['Rok'].astype('int')
DF10['Wydział'] = DF10['Wydział'].replace(['Ogółem'],'Ogółem UMK')
DF11 = pd.read_pickle(r'Dane/pick/Niestacjonarne.pickle')
DF11['Rok'] = DF11['Rok'].astype('int')
DF11['Wydział'] = DF11['Wydział'].replace(['Ogółem'],'Ogółem UMK')
DF12 = pd.read_pickle(r'Dane/pick/doktoranci.pickle')
DF12['Rok'] = DF12['Rok'].astype('int')
DF12['Wydział'] = DF12['Wydział'].replace(['Ogółem'],'Ogółem UMK')
DF13 = pd.read_pickle(r'Dane/pick/Podyplomowe.pickle')
DF13['Rok'] = DF13['Rok'].astype('int')
DF14 = pd.read_pickle(r'Dane/pick/Ogółem.pickle')
DF14['Rok'] = DF14['Rok'].astype('int')

DF15 = pd.read_pickle(r'Dane/pick/Stud_og.pickle')
DF15['Rok'] = DF15['Rok'].astype('int')
DF15['Wydział'] = DF15['Wydział'].replace(['Ogółem'],'Ogółem UMK')

DF17 = pd.read_pickle(r'Dane/pick/Absolwenci.pickle')
DF17['Rok'] = DF17['Rok'].astype('int')
DF17['Rodzaj'] = DF17['Rodzaj'].replace(['Ogółem'],'Ogółem UMK')
DF17a = pd.read_pickle(r'Dane/pick/Absolwenci1.pickle')
DF17a['Rok'] = DF17a['Rok'].astype('int')

fig = px.bar(DF13,x='Rok',y='Liczba',width=1500,height=500).update_xaxes(dtick=1).update_yaxes(rangemode='tozero',
            tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,
            showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>',
            textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
fig1 = px.bar(DF14,x='Rok',y='Liczba',width=1500,height=500).update_xaxes(dtick=1).update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray').update_traces(hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>',textfont=dict( size=14),marker_color='rgb(0,70,180)',texttemplate="%{y:}",textposition='inside').update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black"))
if kat34 == 'Studia stacjonarne':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
    st.plotly_chart(px.bar(DF10[DF10['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
        .update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
        .update_xaxes(dtick=1)
        .update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
        .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
elif kat34 == 'Studia niestacjonarne':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
    st.plotly_chart(px.bar(DF11[DF11['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
        .update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
        .update_xaxes(dtick=1)
        .update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
        .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
elif kat34 == 'Ogółem':
    wydzial34 = q2.selectbox('Wybierz wydział : ',DF12['Wydział'].unique(),index=0)
    st.plotly_chart(px.bar(DF15[DF15['Wydział']==wydzial34],x='Rok',y='Liczba',width=1500,height=500)
        .update_traces(marker_color=kolwyd1[wydzial34],texttemplate="%{y:}",textposition='inside',textfont=dict( size=14),hovertemplate = '<br>Liczba uczestników: <b>%{y:}</b><br>')
        .update_xaxes(dtick=1)
        .update_yaxes(rangemode='tozero',tickformat=" ",title='Liczba uczestników',showline=False,showgrid=True,showticklabels=True,linewidth=2,linecolor='black',gridwidth=1,gridcolor='gray')
        .update_layout(plot_bgcolor='white',font=dict(family='Lato',size=18,color="Black")),use_container_width=True)
    

##------------STUDENCI ZAGRANICZNI
    
title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Studenci zagraniczni na UMK</b></p>'
st.markdown(title, unsafe_allow_html=True)  
left_co, cent_co,last_co = st.columns([.1, .8, .1])
with cent_co:
    title = '<p style="font-family:lato; color:#0050AA; font-size: 20px;"><b>Udział studentów z zagranicy w ogóle uczestników studiów na UMK [%]</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    st.image(r'Wykresy/studenci_zagraniczni.png')    
    
    
##------------GENERATOR


new_title = '<p style="font-family:lato; color:#0050AA; font-size: 30px;"><b>Liczba studentów na wybranym kierunku na UMK w latach 2017-2022<b></p>'
st.markdown(new_title, unsafe_allow_html=True)

file = st.selectbox(
    'Proszę wybrać tryb studiów',
    ('Ogółem', 'Stacjonarne', 'Niestacjonarne'))

if file == 'Ogółem':
    addon = 'łącznie'
else:
    addon = 'studia {}'.format(file.lower())

kier = st.selectbox(
    'Proszę wybrać kierunek',

    (['Ogółem'] + [name for name in data_dict[file].index.levels[0] if name != 'Ogółem']))


if kier != 'Ogółem':
    repls = {'l, 3.0': 'studia pierwszego stopnia', 
    'm, 2.0': 'studia drugiego stopnia', 
    'm, 5.0': 'studia jednolite magisterskie pięcioletnie', 
    'm, 1.5': 'studia drugiego stopnia trzysemestralne',
    'z, 3.5': 'studia pierwszego stopnia inżynierskie',
    'm, 5.5': 'studia jednolite magisterkie 11 semetrów',
    'm, 6.0': 'studia jednolite magisterskie sześcioletnie'}

    unrep = {}
    for rep in repls.keys():
        unrep[repls[rep]] = rep

    stop = st.selectbox(
        'Proszę wybrać stopień studiów',
        (['Ogółem'] + [reduce(lambda a, kv: a.replace(*kv), repls.items(), ', '.join(name)) for name in stac.loc[(kier)].index.tolist()]))
    if stop != 'Ogółem':
        stp, stp1 = unrep[stop].split(', ')
        y_plot = [data_dict[file].loc[(kier, stp, stp1), (year, 'studenci studiów ogółem')] for year in range(2017, 2023)]
    else:
        y_plot = [data_dict[file].loc[(kier), (year, 'studenci studiów ogółem')].sum() for year in range(2017, 2023)]

    title = "Liczba studentów na kierunku {}<br>({}, {})".format(kier.lower(), stop.lower(), addon.split(' ')[-1])
else:
    y_plot = [data_dict[file].loc[(kier), (year, 'studenci studiów ogółem')].sum() for year in range(2017, 2023)]

    title = "Ogólna liczba studentów ({})".format(addon)
        
left_co, cent_co,last_co = st.columns([.2, .6, .2])
with cent_co:        
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=list(list(range(2017, 2023))),
                   y=y_plot,
                   name=kier,
                   line=dict(color="#0050AA"))) 
    fig.update_layout(
        font_family="Lato",
        font_color="black",
        yaxis = dict(tickformat = "000")
    )

    fig.update_yaxes(range=[0, 1.2*max(y_plot)])

    fig.update_layout(title_text= title)

    st.plotly_chart(fig)

