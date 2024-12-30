import folium as fl
from streamlit_folium import st_folium
import streamlit as st
from geopy.geocoders import Nominatim

def get_pos(lat, lng)->list:
    return lat, lng
st.set_page_config(
    page_title="Prediction temperature",
    page_icon="🌦️",
)
st.title('Choix de localisation:')
m = fl.Map(location=[0, 0],
    zoom_start=2,
    max_bounds=True,)
m.options['maxBounds'] = [[-90, -180], [90, 180]]
m.add_child(fl.LatLngPopup())
map = st_folium(m, height=350, width=700)
data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
geolocator = Nominatim(user_agent="folium_app") 

if data is not None :
    lat,long=st.columns(2)
    with lat:
        with st.container(border=True):
            st.write(f"Latitude :  :blue[{data[0]:.2f}]")
    with long:
        with st.container(border=True):
            st.write(f"Longitude :  :blue[{data[1]:.2f}]")
    try:
        location = geolocator.reverse((data[0], data[1]), exactly_one=True)
        if location:
            address = location.raw.get('address', {})
            city = address.get('city', address.get('town', address.get('village', 'Unknown City')))
            country = address.get('country', 'Unknown Country')
            c1,c2=st.columns(2)
            with c1:
                with st.container(border=True,height=100):
                    st.write(f"Pays: :blue[{country}]")
            with c2:
                with st.container(border=True,height=100):
                    st.write(f"Ville: :blue[{city}]")
    except:
        pass

if st.button('Valider'):
    if data:
        st.session_state.latitude=data[0]
        st.session_state.longitude=data[1]
        st.success(f"Localisation prise : {data}",icon="✅")
        st.switch_page("pages/Collecte.py")
    else:
        st.error("Veuiller choisir une localisation ",icon="🚨")
