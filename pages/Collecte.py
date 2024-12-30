import streamlit as st
from logic.collecte import collecter,get_stats
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(
    page_title="Prediction temperature",
    page_icon="🌦️",
)


st.title("Collecte des donnees :")
if "longitude" in st.session_state:
    lat,long=st.columns(2)
    with lat:
        with st.container(border=True):
            st.write(f"Latitude : :blue[{st.session_state.latitude:.2f}]")
    with long:
        with st.container(border=True):
            st.write(f"Longitude : :blue[{st.session_state.longitude:.2f}]")
    with st.spinner("Entrain de collecter"):
        data=collecter(st.session_state.latitude,st.session_state.longitude)
    st.subheader("Data frame:", divider="blue")
    st.write(data)
    st.session_state.data=data
    st.subheader("Data frame description:", divider="blue")
    st.write(get_stats(data))
    st.subheader("Data frame visualisation:", divider="blue")
    tab1, tab2,tab3 = st.tabs(["Temperature par date", "Humidite par date","Precipitation par date"])
    with tab1:
        st.line_chart(data, x="Date", y="Temperature moyenne (°C)",height=600)
    with tab2:
        st.line_chart(data, x="Date", y="Humidite moyenne (%)",height=600)
    with tab3:
        st.line_chart(data, x="Date", y="Precipitation (mm)",height=600)
    st.subheader("Data frame correlation matrix:", divider="blue")
    fig = px.imshow(data.drop('Date',axis=1,inplace=False).corr(), text_auto=True, aspect="auto")
    st.plotly_chart(fig, theme="streamlit")
    st.subheader("Tester les modeles", divider="blue")
    col1,col2=st.columns(2)
    with col1:
        if st.button("Regression linéaire"):
            st.switch_page("pages/Regression lineaire.py")
    with col2:
        if st.button("Random forest"):
            st.switch_page("pages/Random forest.py")
else:
    if st.button("Choisir localisation"):
        st.switch_page("pages/Location.py")