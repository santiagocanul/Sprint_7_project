import streamlit as st
import pandas as pd
import plotly.express as px

url= "https://drive.google.com/uc?id=1_FxiFJ5WbN1qZp_lietBr6-KGX8-UVlm"
df = pd.read_csv(url)

st.write(df.columns)

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