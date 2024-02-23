import streamlit as st



##-------------------------------------------------
st.set_page_config(layout="wide")
left_co, cent_co,last_co = st.columns([.2, .6, .2])
with cent_co:
    st.image(r'Wykresy/logo-umk.png')


text1 = '<p style="font-family:lato; color:#000000; font-size: 16px;">Aplikacja zawiera dane dotyczące liczby studentów podejmujących naukę na Uniwersytecie Mikołaja Kopernika w Toruniu w latach 2017-2022 w podziale na kierunki oraz kandydatów i osób przyjętych na studia w latach 2020-2023. </p>'

st.markdown(text1, unsafe_allow_html=True)

text2 = '<p style="font-family:lato; color:#000000; font-size: 16px;">Dane do wizualizacji zostały uzyskane ze sprawozdań rocznych JM Rektora oraz systemu Internetowej Rejestracji Kandydatów. <br> Autorami wizualizacji są:  <ul><li style="font-family:lato; color:#000000; font-size: 16px;">mgr inż. Jakub Wojtasik (Ośrodek Analiz Statystycznych UMK),</li><li style="font-family:lato; color:#000000; font-size: 16px;">mgr inż. Krzystof Leki (Ośrodek Analiz Statystycznych UMK),</li><li style="font-family:lato; color:#000000; font-size: 16px;">inż. Tomasz Zieliński (WMiI UMK),</li><li style="font-family:lato; color:#000000; font-size: 16px;">dr Joanna Karłowska-Pik (Ośrodek Analiz Statystycznych UMK).</li></ul> </p>'

st.markdown(text2, unsafe_allow_html=True)

text3 = '<p style="font-family:lato; color:#000000; font-size: 16px;">Aplikacja składa się z trzech zakładek, poświęconych studentom, osobom przyjętym na studia oraz kandydatom na studia. Każda z nich zawiera opracowane wizualizacje oraz interaktywne narzędzia pozwalające na generowanie wykresów w oparciu o samodzielnie wskazany zakres danych.</p>'

st.markdown(text3, unsafe_allow_html=True)

text4 = '<p style="font-family:lato; color:#000000; font-size: 16px;">W przypadku pytań dotyczących działania aplikacji, zauważenia błędów lub innych niejasności, prosimy o kontakt mailowy na adres <b>stat@umk.pl</b>.</p>'

st.markdown(text4, unsafe_allow_html=True)