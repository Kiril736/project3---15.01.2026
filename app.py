import streamlit as st
import pandas as pd

st.title("Оценка на ученика")

if "colors" not in st.session_state:
    st.session_state.colors = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }

if "sports" not in st.session_state:
    st.session_state.sports = {
        "Мартин": 0,
        "Георги": 0,
        "Димитър": 0,
        "Иван": 0
    }

st.subheader("Избери любими неща")

color = st.selectbox("Оценка:", list(st.session_state.colors.keys()))
sport = st.selectbox("Ученици:", list(st.session_state.sports.keys()))

if st.button("Запази избора"):
    st.session_state.colors[color] += 1
    st.session_state.sports[sport] += 1
    st.success("Изборът е записан!")

st.divider()

st.subheader("📊 Резултати")

st.write("Оценка")
colors_df = pd.DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

st.write("Ученик")
sports_df = pd.DataFrame.from_dict(
    st.session_state.sports, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)
