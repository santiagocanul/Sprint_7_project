import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us_small.csv")

st.write("Columnas del dataset:")
st.write(df.columns)
st.write(df.head())

df = df[(df['price'] >= 500) & (df['price'] <= 100000)]
df = df.dropna(subset=['year', 'price'])

st.title("Análisis de anuncios de vehículos en EE.UU.")

st.write(
    """
    Esta aplicación permite explorar un conjunto de datos de anuncios de autos
    mediante visualizaciones interactivas.
    """
)

if st.button("Mostrar histograma de precios"):
    st.write("Distribución de precios de los vehículos")

    fig_hist = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Histograma de precios"
    )

    st.plotly_chart(fig_hist)

if st.button("Mostrar gráfico Precio vs Año"):
    st.write("Relación entre el precio y el año del vehículo")

    fig_scatter = px.scatter(
        df,
        x="year",
        y="price",
        title="Precio vs Año",
        opacity=0.4
    )

    st.plotly_chart(fig_scatter)