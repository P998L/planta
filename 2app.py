import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Título de la aplicación
st.title("🌱 Canciones que mencionan plantas")

# Descripción de la plataforma
st.write("Encuentra canciones donde se mencionen plantas y accede a su contenido directamente desde YouTube.")

# Campo de entrada para buscar
search_query = st.text_input("Escribe el nombre de una planta o palabra clave:")

if st.button("Buscar canciones"):
    if search_query:
        st.write(f"🔍 Buscando canciones relacionadas con: **{search_query}**...")

        # Simulación de una búsqueda (puedes usar una API real como Genius o YouTube Data API)
        # Aquí se realiza una petición de ejemplo
        try:
            # URL de búsqueda (modificar para usar APIs reales)
            # Por ahora es un ejemplo simulado
            fake_results = [
                {
                    "title": "The Rose",
                    "artist": "Bette Midler",
                    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/e/ed/The_Rose_%28song%29.jpg",
                    "youtube_link": "https://www.youtube.com/watch?v=oR6okRuOLc8"
                },
                {
                    "title": "Every Rose Has Its Thorn",
                    "artist": "Poison",
                    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/4/42/Every_Rose_Has_Its_Thorn.jpg",
                    "youtube_link": "https://www.youtube.com/watch?v=j2r2nDhTzO4"
                }
            ]

            # Mostrar resultados
            for result in fake_results:
                st.subheader(result["title"])
                st.write(f"Artista: {result['artist']}")
                
                # Mostrar portada de la canción
                response = requests.get(result["thumbnail"])
                image = Image.open(BytesIO(response.content))
                st.image(image, caption=result["title"], use_column_width=True)
                
                # Link a YouTube
                st.markdown(f"[Escuchar en YouTube]({result['youtube_link']})")
                st.write("---")

        except Exception as e:
            st.error("Hubo un error al buscar canciones. Intenta nuevamente más tarde.")
    else:
        st.warning("Por favor, escribe una palabra clave para buscar.")
