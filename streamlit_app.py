import streamlit as st
import random
import pandas as pd

# Titel des Web-Tools
st.title("Cthulhu Abenteuer & Würfel-Manager")

# Navigation
menu = st.sidebar.selectbox("Menü", ["Investigatoren", "Abenteuer", "Würfeln"])

# Datenbank für Investigatoren
if "investigatoren" not in st.session_state:
    st.session_state.investigatoren = pd.DataFrame(columns=["Name", "Beruf", "ST", "KO", "GR", "GE", "ER", "IN", "BI", "SAN", "TP", "Mythos", "Glück"])

# Menü Investigatoren
if menu == "Investigatoren":
    st.subheader("Investigatoren verwalten")
    with st.form("investigator_form"):
        name = st.text_input("Name")
        beruf = st.text_input("Beruf")
        st_val = st.number_input("Stärke (ST)", 1, 100)
        ko_val = st.number_input("Konstitution (KO)", 1, 100)
        gr_val = st.number_input("Größe (GR)", 1, 100)
        ge_val = st.number_input("Geschicklichkeit (GE)", 1, 100)
        er_val = st.number_input("Erscheinung (ER)", 1, 100)
        in_val = st.number_input("Intelligenz (IN)", 1, 100)
        bi_val = st.number_input("Bildung (BI)", 1, 100)
        san_val = st.number_input("Sanity (SAN)", 1, 100)
        tp_val = st.number_input("Trefferpunkte (TP)", 1, 100)
        mythos_val = st.number_input("Mythos-Wissen", 0, 100)
        glück_val = st.number_input("Glück", 1, 100)
        submit = st.form_submit_button("Investigator hinzufügen")
    
    if submit:
        new_inv = pd.DataFrame([[name, beruf, st_val, ko_val, gr_val, ge_val, er_val, in_val, bi_val, san_val, tp_val, mythos_val, glück_val]],
                               columns=st.session_state.investigatoren.columns)
        st.session_state.investigatoren = pd.concat([st.session_state.investigatoren, new_inv], ignore_index=True)
        st.success(f"{name} wurde hinzugefügt!")

    st.write(st.session_state.investigatoren)

# Menü Abenteuer
elif menu == "Abenteuer":
    st.subheader("Abenteuer-Verwaltung")
    abenteuer_name = st.text_input("Szenario-Name")
    abenteuer_beschreibung = st.text_area("Beschreibung")
    st.button("Abenteuer speichern")
    st.write(f"Aktuelles Abenteuer: {abenteuer_name}")
    st.write(abenteuer_beschreibung)

# Menü Würfelwürfe
elif menu == "Würfeln":
    st.subheader("Würfeln für Aktionen")
    würfeltyp = st.selectbox("Wähle einen Würfel", ["W100", "W20", "W10", "W8", "W6", "W4"])
    if st.button("Würfeln"):
        if würfeltyp == "W100":
            ergebnis = random.randint(1, 100)
        elif würfeltyp == "W20":
            ergebnis = random.randint(1, 20)
        elif würfeltyp == "W10":
            ergebnis = random.randint(1, 10)
        elif würfeltyp == "W8":
            ergebnis = random.randint(1, 8)
        elif würfeltyp == "W6":
            ergebnis = random.randint(1, 6)
        elif würfeltyp == "W4":
            ergebnis = random.randint(1, 4)
        st.success(f"Ergebnis: {ergebnis}")
