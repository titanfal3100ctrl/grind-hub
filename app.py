import pandas as pd
nomi_validi=['nizar','lion','alex','Nizar','Alex','Lion','nesti','Nesti']
import sqlite3 as sq
import streamlit as st
import os as os
from datetime import datetime
import base64
import time


def mostra_countdown_grindhub_live():
  placeholder = st.empty()

  while True:
    with placeholder.container():
      conn = sq.connect("grindhub.db")
      curs = conn.cursor()

      # 1. Abbiamo aggiunto 'utente' nella SELECT
      curs.execute(
          "SELECT utente, argomento, data_scadenza FROM scaletta_argomenti"
          " WHERE completato = 0"
      )
      missioni = curs.fetchall()
      conn.close()

      now = datetime.now()

      st.subheader("⏳ GRIND HUB - COUNTDOWN LIVE")

      if not missioni:
        st.info("Nessuna missione attiva al momento!")
      else:
        # 2. Estraiamo anche la variabile 'utente'
        for utente, argomento, data_scadenza_str in missioni:
          scadenza = datetime.strptime(data_scadenza_str, "%Y-%m-%d %H:%M:%S")
          rimanente = scadenza - now

          if rimanente.total_seconds() > 0:
            giorni = rimanente.days
            ore = rimanente.seconds // 3600
            minuti = (rimanente.seconds % 3600) // 60
            secondi = rimanente.seconds % 60

            # Formattazione pulita: [NOME] Argomento ➔ Tempo
            st.write(
                f"👤 **[{utente.upper()}]** {argomento} ➔ Mancano **{giorni}d"
                f" {ore}h {minuti}m {secondi}s**"
            )
          else:
            st.error(f"🚨 **[{utente.upper()}]** {argomento} ➔ TEMPO SCADUTO!")

      st.markdown("---")

    time.sleep(1)
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
    tab1,tab2,tab_Niz,tab_Alex,tab_timer=st.tabs(['Home','Ruoli','Programma di Nizar','Programma di Alex','Obiettivi settimanali'])
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
                  st.subheader('Lion')
                  with st.container(border=True):
                    st.write('1. Programmatore')
                    st.write('2. Marketing')
                    st.write('3. Analisi e crescita')
            with col2:
                st.subheader('Nizar')
                with st.container(border=True):
                    st.write('1. Social media manager')
                    st.write('2. Aiuto programmatore')
                    st.write('3. Grafica ')
            with col3:
                 st.subheader('Alex')
                 with st.container(border=True):
                    st.write('1. Programmatore main')       
                    st.write('2. Backend developer')
                    st.write('3. Sicurezza')
        with tab_Niz:
            col_argomenti,col_fonti=st.columns(2)
            st.header('Argomenti e Fonti per Nizar')
            with col_argomenti:
                st.subheader('questi sono gli argomenti di Nizar')
                st.markdown('le cose che devi imparare adesso, sono poche ma impareremo di più più avanti')
                with st.container(border=True):
                    st.write('''1. **HTML e CSS**: Creazione di Wireframe, Prototipi interattivi e D.''')
                    st.write('2. **canva**: Saper fare grafiche')
                    st.write('3. **Figma**: Creazione di Wireframe, Prototipi interattivi e Design System ')
                    st.write('4. **Framer/Webflow**')
            with col_fonti:
                st.subheader('Fonti per imparare')
                st.markdown('ogni numero nelle fonti equivale alla fonte di un argomento')
                with st.container(border=True):
                    st.write('1. "HTML and CSS full  course for free" di Bro Code o "HTML and CSS full course" di Super Simple dev e freecodecamp.org ')
                    st.write('2. Canva Design School')
                    st.write('3. Figma, il canale ufficiale youtube e learn.figma.com ')
                    st.write('4. Framer(canale ufficiale) e Webflow university entrambi su youtube')
        with tab_Alex:
            col_argomenti1,col_fonti1=st.columns(2)
            with col_argomenti1:
                st.subheader('Questi sono gli argomenti di Alex')
                st.markdown('le cose che devi imparare adesso, ne aggiungeremo di più più avanti')
                with st.container(border=True):
                    st.write('1. **Python**: devi finire Python')
                    with st.expander('argomenti di Python'):
                        with st.container(border=True):
                            st.write('1. Api: come comunicano server e computer')
                            st.write('2. Web scraping: ottenere informazioni da siti web')
                            st.write('3. Pandas e analisi: filtraggio CSV e JSON')
                            st.write('4. Database SQL')
                            st.write('5. webhooks: fastAPi')
                            st.write('6.Django')
                    with st.container(border=True):
                        st.write('2. Node.js (javascript/typescript)')
                        st.write('3. GO')
                        st.write('4. JWT & OAuth2')
                        st.subheader('questi qua gli dovrai imparare solo dopo aver masterato python')
            with col_fonti1:
                st.subheader('queste sono le fonti')
                st.markdown('ogni numero qua equivale al numero di argomento')
                with st.container(border=True):
                    st.write('1. Python')
                    with st.expander('clicca per vedere python'):
                        st.write('1. API: "request data using python" di Bro Code su youtube e automate the boring stuff') 
                        st.write('2. Web Scraping: automate the boring stuff e "Scraping Data from a Real website" di Alex the analyst su yt')
                        st.write('3. Pandas: "learn pandas in 30 minutes" di tech with tim e ti manderò anche io dei tutorial')
                        st.write('4. "Learn SQL beginner to advanced" di Alex the analyst o "Database SQLite con Python" di freecodecamp.org')
                        st.write('5. "fast APi course for beginners" di freecodecamp.org su yt')
                        st.write('6. "learn Django in 20 minutes" di Tech with Tim su yt')
                        st.warning('il resto te lo darò quando hai finito questi su che ci vogliono almeno 3 mesi')                 
        with tab_timer:
            
            st.subheader('Questa è la pagina degli obiettivi settimanali per stare sempre in ritmo')
            st.markdown('ecco gli argomenti da studiare per questa settimana:')
            with st.expander('visualizza gli argomenti da studiare:'):
                st.write('questi sono gli argomenti da studiare')
            st.markdown('ecco gli obiettivi settimanali di noi 3')
            st.write(f'tempo rimasto: {mostra_countdown_grindhub_live()}')
            col_ob_lion,col_ob_alex,col_ob_nizar=st.columns(3)
            from datetime import datetime

            with col_ob_lion:
                st.write('obiettivi, ecc')



                


