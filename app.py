import pandas as pd
nomi_validi=['nizar','lion','alex','Nizar','Alex','Lion']
import streamlit as st
import os as os
from datetime import datetime as dt
import base64
if 'step' not in st.session_state:
    st.session_state.step=1
if st.session_state.step==1:
    utente={'nome':None,'codice':'grind'}
    with st.form(key='membro'):
            st.subheader('verifica informazioni utente')
            utente['nome']=st.text_input('inserisci il tuo nome vero').lower()
            utente['codice']='grind'
            codice=st.text_input('inserisci il codice fornito su whatsapp',type='password',help='mostra password').lower()
            submit_button=st.form_submit_button('verifica')
            if submit_button:
                if utente['nome'] in nomi_validi and codice==utente['codice']:
                    st.session_state.step=2
                    st.rerun()
                else:
                    st.warning('inserisci nome utente e codice validi')


def set_bg_hack(main_bg):
    main_bg_ext = "png"
    with open(main_bg, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{main_bg_ext};base64,{encoded}");
            background-size: cover;
            background-position: down;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
if 'step' not in st.session_state:
    st.session_state.step=1

elif st.session_state.step==2: #step 2. TUTTO CIò CHE VIENE DOPO LA NIGGA PASSOWRD
    st.markdown("""
    <style>
    /* Seleziona direttamente il testo di tutti i tab */
    .stTabs [data-baseweb="tab"] {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)   
    if st.sidebar.button('fai il log out'):
        st.session_state.step=1
        st.rerun()
    if st.sidebar.button('torna alla home'):
        if st.button("🏠 Torna alla Home", use_container_width=True):
            st.rerun()
    tab1,tab2=st.tabs(['Home','Ruoli'])
    with tab1:
        st.title('questo è il sito per grindare e raggiungere i nostri obiettivi!!')
        st.subheader('questo sito è stato creato da me per voi due')
        with st.expander('perchè hai creato questo sito?'):
                st.text('''Ho creato questo sito per esercitarmi con python e i miei progetti e perchè lo faremo espandere per imparare a creare SaaS.
                Potremmo pure usarlo e aggiungere funzionalità come quante ore abbiamo grindati, gli achievement raggiunti e gli argomenti da fare, posso pure crearvi mini lezioni.''')
                with st.expander("Come l'hai creato?"):
                    st.text('Ho creato questa versione molto iniziale e semplice del sito esclusivamente con Python, perciò immaginate cosa potremmo creare tra 1 anno in 3 se grinderemo e sapremo tante skills!')
                    with st.expander('NOTA'):
                        st.text('il sito è ancora in pre early beta alfa, insomma, appena iniziato, ma ci lavoreremo insieme perchè lo useremo per fare esperienza per quando creeremo i nostri SaaS')
                        st.text('''NON MOLLATE! i veri campioni non inventano scuse e trovano sempre tempo.
        Tutti abbiamo le stesse 24 ore, ma bisogna gestirle bene, io faccio calcio, scuola, palestra
        e ho ancora tempo per grindare solo perchè ho tolto le cose inutili''')
        st.image(os.path.join(os.getcwd(),'static','job_not.png'),width=750)
        st.markdown(
        """
        <style>
        /* 1. Sfondo generale della pagina (scuro per uniformità) */
        .stApp {
            background-color: #0d1117 !important;
            color: #ffffff !important;
        }

        /* 2. SCHEDA SCURA OPACA DIETRO I CONTENUTI PRINCIPALI (Contrasto perfetto) */
        [data-testid="stMainBlockContainer"] {
            background-color: rgba(10, 10, 12, 0.9) !important; /* Molto scuro ma opaco */
            padding: 30px !important;
            border-radius: 15px !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
        }

        /* 3. Forza tutti i testi dei titoli e paragrafi in BIANCO */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label {
            color: #ffffff !important;
        }

        /* 4. Colore degli Expander e Pulsanti (come nell'esempio) */
        .streamlit-expanderHeader {
            background-color: #1a1a1e !important;
            color: #ffffff !important;
        }
        .stButton > button {
            background-color: #ff5722 !important; /* Arancione Grind */
            color: orange !important;
            border-radius: 8px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        with tab2:
            st.title('questa è la pagina dei ruoli')
            st.header('ecco i ruoli di ciascuno noi nel grind:')
            col1,col2,col3=st.columns(3)
            with col1:
                  st.subheader('L')
                  with st.container(border=True):
                    st.write('1. Programmatore')
                    st.write('2. Marketing')
                    st.write('3. Analisi e crescita')
            with col2:
                st.subheader('N')
                with st.container(border=True):
                    st.write('1. Social media manager')
                    st.write('2. Aiuto programmatore')
                    st.write('3. Grafica ')
            with col3:
                 st.subheader('A')
                 with st.container(border=True):
                    st.write('1. Programmatore main')       
                    st.write('2. Backend developer')
                    st.write('3. Sicurezza')

