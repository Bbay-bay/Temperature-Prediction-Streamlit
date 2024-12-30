import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd
import requests
import json

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Prédiction de Température",
        page_icon="🌦️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS pour améliorer le design
    st.markdown("""
        <style>
        /* Style personnalisé pour les conteneurs */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background-color: rgba(28, 131, 225, 0.1);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        
        /* Style pour les titres */
        h1 {
            background: linear-gradient(45deg, #1C83E1, #00B4D8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 0.5rem 0;
        }
        
        /* Style pour les cartes */
        .stCard {
            border: 2px solid rgba(28, 131, 225, 0.2);
            border-radius: 15px;
            transition: transform 0.3s ease;
        }
        .stCard:hover {
            transform: translateY(-5px);
        }
        
        /* Style pour les boutons */
        .stButton button {
            width: 100%;
            border-radius: 50px;
            font-size: 1.2em;
            font-weight: 600;
            padding: 0.8em 1.5em;
            background: linear-gradient(45deg, #1C83E1, #00B4D8);
            border: none;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        /* Style pour les tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }
        .stTabs [data-baseweb="tab"] {
            height: 4rem;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 4px;
            color: #fff;
            font-size: 1.2rem;
            font-weight: 400;
            border: none;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(28, 131, 225, 0.1);
        }
        
        /* Style pour le texte */
        .big-font {
            font-size: 1.5em !important;
        }
        .medium-font {
            font-size: 1.3em !important;
        }
        .gradient-text {
            background: linear-gradient(45deg, #1C83E1, #00B4D8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
    """, unsafe_allow_html=True)

    # En-tête avec animation
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <h1 style='font-size: 3.5em; margin-bottom: 0;'>
                Système de Prédiction de Température
            </h1>
            <p class='big-font' style='margin-top: 0;'>
                Intelligence Artificielle au Service de la Météorologie
            </p>
        """, unsafe_allow_html=True)
    with col2:
        # Animation Lottie pour la météo
        weather_lottie = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_trr3kqyu.json")
        if weather_lottie:
            st_lottie(weather_lottie, height=200)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Section Statistiques Rapides
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        metrics = [
            {"title": "Années de Données", "value": "10+", "icon": "📊"},
            {"title": "Précision", "value": "95%", "icon": "🎯"},
            {"title": "Modèles IA", "value": "2", "icon": "🤖"},
            {"title": "Mise à jour", "value": "24/7", "icon": "🔄"}
        ]
        
        for col, metric in zip([col1, col2, col3, col4], metrics):
            with col:
                st.container(border=True).markdown(f"""
                    <div style='text-align: center;'>
                        <h2 style='font-size: 2.5em; margin: 0;'>{metric['icon']}</h2>
                        <p class='medium-font gradient-text' style='margin: 0;'>{metric['value']}</p>
                        <p style='font-size: 1.1em; opacity: 0.8;'>{metric['title']}</p>
                    </div>
                """, unsafe_allow_html=True)

    # Fonctionnalités Principales avec des icônes modernes
    st.markdown("<h2 class='gradient-text' style='font-size: 2.5em; margin-top: 2rem;'>Fonctionnalités Principales</h2>", unsafe_allow_html=True)
    
    features_tab1, features_tab2, features_tab3 = st.tabs(["🌍 Collecte", "📊 Analyse", "🤖 Prédiction"])
    
    with features_tab1:
        st.container(border=True).markdown("""
            <div class='medium-font'>
                <h3>Collecte de Données Intelligente</h3>
                • Sélection interactive sur carte mondiale<br>
                • Données météorologiques sur 10 ans<br>
                • Mise à jour automatique quotidienne<br>
                • Validation et nettoyage automatique
            </div>
        """, unsafe_allow_html=True)
        
    with features_tab2:
        st.container(border=True).markdown("""
            <div class='medium-font'>
                <h3>Analyse Approfondie</h3>
                • Visualisations interactives<br>
                • Corrélations avancées<br>
                • Tendances temporelles<br>
                • Rapports détaillés
            </div>
        """, unsafe_allow_html=True)
        
    with features_tab3:
        st.container(border=True).markdown("""
            <div class='medium-font'>
                <h3>Prédiction IA</h3>
                • Régression linéaire optimisée<br>
                • Random Forest adaptatif<br>
                • Métriques de performance<br>
                • Ajustement automatique
            </div>
        """, unsafe_allow_html=True)

    # [Previous imports and CSS remain the same until the Process section]

    # Section détaillée du processus
    st.markdown("<h2 class='gradient-text' style='font-size: 2.5em; margin-top: 2rem;'>Guide Détaillé du Processus</h2>", unsafe_allow_html=True)
    
    # Étape 1: Sélection de Location
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 1: Sélection de Location 🎯</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
                <div class='medium-font'>
                <h4>Comment faire:</h4>
                • Accédez à l'onglet "Location"<br>
                • Utilisez la carte interactive mondiale<br>
                • Cliquez sur votre emplacement désiré<br>
                • Confirmez les coordonnées GPS<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='medium-font'>
                <h4>Détails techniques:</h4>
                • Utilisation de Folium pour la cartographie interactive<br>
                • Géocodage inverse pour identifier la ville/pays<br>
                • Précision des coordonnées à 0.01 degré<br>
                • Validation automatique des coordonnées<br>
                </div>
            """, unsafe_allow_html=True)

    # Étape 2: Collecte des Données
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 2: Collecte des Données 📥</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
                <div class='medium-font'>
                <h4>Sources de données:</h4>
                • API Open-Meteo pour données historiques<br>
                • 10 ans d'historique (2014-2024)<br>
                • Données météorologiques quotidiennes<br>
                • Mise à jour automatique<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='medium-font'>
                <h4>Paramètres collectés:</h4>
                • Température moyenne journalière (°C)<br>
                • Précipitations quotidiennes (mm)<br>
                • Humidité relative moyenne (%)<br>
                • Autres indicateurs météorologiques<br>
                </div>
            """, unsafe_allow_html=True)

    # Étape 3: Analyse IA
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 3: Analyse IA 🔍</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.markdown("""
                <div class='medium-font'>
                <h4>Prétraitement:</h4>
                • Nettoyage des données<br>
                • Normalisation<br>
                • Calcul des moyennes mobiles<br>
                • Gestion des valeurs manquantes<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='medium-font'>
                <h4>Visualisation:</h4>
                • Graphiques temporels<br>
                • Matrices de corrélation<br>
                • Analyses statistiques<br>
                • Détection des tendances<br>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
                <div class='medium-font'>
                <h4>Modélisation:</h4>
                • Sélection des caractéristiques<br>
                • Validation croisée<br>
                • Optimisation des paramètres<br>
                • Évaluation des modèles<br>
                </div>
            """, unsafe_allow_html=True)

    # Étape 4: Prédiction
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Étape 4: Prédiction 🎯</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div class='medium-font'>
                <h4>Régression Linéaire:</h4>
                • Modèle de base robuste<br>
                • Variables normalisées<br>
                • Métriques de performance:<br>
                &nbsp;&nbsp;- R² Score<br>
                &nbsp;&nbsp;- Erreur quadratique moyenne (MSE)<br>
                &nbsp;&nbsp;- Erreur absolue moyenne (MAE)<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='medium-font'>
                <h4>Random Forest:</h4>
                • 300 arbres de décision<br>
                • Optimisation des hyperparamètres<br>
                • Gestion avancée de la non-linéarité<br>
                • Métriques de performance:<br>
                &nbsp;&nbsp;- Précision des prédictions<br>
                &nbsp;&nbsp;- Importance des variables<br>
                </div>
            """, unsafe_allow_html=True)

    # Section Comparaison des Modèles
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h3 class='gradient-text' style='font-size: 2em;'>Comparaison des Modèles 📊</h3>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div class='medium-font'>
                <h4>Avantages Régression Linéaire:</h4>
                • Simplicité d'interprétation<br>
                • Rapidité d'exécution<br>
                • Performance stable<br>
                • Idéal pour les tendances linéaires<br>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div class='medium-font'>
                <h4>Avantages Random Forest:</h4>
                • Meilleure précision générale<br>
                • Gestion des relations complexes<br>
                • Robustesse au bruit<br>
                • Pas de problème de surapprentissage<br>
                </div>
            """, unsafe_allow_html=True)

    # Call-to-Action plus détaillé
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("""
            <div style='text-align: center;'>
                <h2 class='gradient-text' style='font-size: 2em;'>Commencez Votre Prédiction</h2>
                <p class='medium-font'>Suivez ces étapes simples pour obtenir des prédictions précises</p>
                <ol class='medium-font' style='text-align: left;'>
                    <li>Sélectionnez votre emplacement sur la carte</li>
                    <li>Attendez la collecte et l'analyse des données</li>
                    <li>Choisissez votre modèle de prédiction préféré</li>
                    <li>Obtenez vos prédictions de température</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Démarrer l'Analyse", type="primary"):
            st.switch_page("pages/Location.py")


    # Footer moderne
    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0; background: rgba(28, 131, 225, 0.1); border-radius: 10px;'>
            <p class='medium-font gradient-text'>Développé avec les Technologies les Plus Avancées</p>
            <p style='opacity: 0.8;'>Intelligence Artificielle • Big Data • Analyse Prédictive</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()