import streamlit as st
import pandas as pd
import datetime

# Naslov aplikacije
st.title("⚖️ Moj Pratioc Težine")

# Inicijalizacija baze podataka (jednostavna tablica)
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Datum", "Težina (kg)", "lokacja"])

# --- UNOS PODATAKA ---
with st.sidebar:
    st.header("Novi unos")
    tezina = st.number_input("Unesi težinu (kg):", min_value=10.0, max_value=300.0, step=0.1)
    datum = st.date_input("Datum:", datetime.date.today())
    lokacija = st.text_input("Lokacija:")
    
    if st.button("Spremi"):
        novi_unos = pd.DataFrame({"Datum": [datum], "Težina (kg)": [tezina]})
        st.session_state.data = pd.concat([st.session_state.data, novi_unos], ignore_index=True)
        st.success("Podatak spremljen!")

# --- PRIKAZ PODATAKA ---
if not st.session_state.data.empty:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Povijest mjerenja")
        st.write(st.session_state.data)

    with col2:
        st.subheader("Grafikon napretka")
        st.line_chart(st.session_state.data.set_index("Datum"))
else:
    st.info("Još nema unesenih podataka. Koristi bočnu traku za prvi unos.")