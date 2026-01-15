import streamlit as st
import pandas as pd
import altair as alt

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
        "Васил": 0,
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

colors_df = pd.DataFrame(
    list(st.session_state.colors.items()),
    columns=["Оценка", "Брой"]
)

color_scale = alt.Scale(
    domain=["2", "3", "4", "5", "6"],
    range=["red", "orange", "yellow", "blue", "green"]
)

chart_colors = alt.Chart(colors_df).mark_bar().encode(
    x="Оценка",
    y="Брой",
    color=alt.Color("Оценка", scale=color_scale)
)

st.altair_chart(chart_colors, use_container_width=True)

sports_df = pd.DataFrame(
    list(st.session_state.sports.items()),
    columns=["Ученик", "Брой"]
)

chart_students = alt.Chart(sports_df).mark_bar().encode(
    x="Ученик",
    y="Брой"
)

st.altair_chart(chart_students, use_container_width=True)
