import streamlit as st

def main():
    st.title("Clasificación de Plantas en Canciones")

    # Datos iniciales: lista de canciones y plantas mencionadas
    canciones = [
        {"cancion": "La Flaca - Jarabe de Palo", "planta": "rosa"},
        {"cancion": "Every Rose Has Its Thorn - Poison", "planta": "rosa"},
        {"cancion": "Lemon Tree - Fool's Garden", "planta": "limonero"},
        {"cancion": "Mandarina - Juan Luis Guerra", "planta": "mandarino"},
    ]

    # Mostrar las canciones disponibles
    st.header("Canciones y Plantas")
    st.write("Estas son las canciones que contienen menciones de plantas:")

    for item in canciones:
        st.write(f"- **{item['cancion']}**: {item['planta']}")

    # Búsqueda de plantas
    st.header("Buscar canciones por planta")
    planta_buscar = st.text_input("Escribe el nombre de una planta:")

    if planta_buscar:
        resultados = [c for c in canciones if planta_buscar.lower() in c['planta'].lower()]
        if resultados:
            st.write(f"Canciones que mencionan la planta '{planta_buscar}':")
            for res in resultados:
                st.write(f"- **{res['cancion']}**")
        else:
            st.write(f"No se encontraron canciones con la planta '{planta_buscar}'.")

    # Agregar nuevas canciones y plantas
    st.header("Agregar una nueva canción")
    nueva_cancion = st.text_input("Nombre de la canción:")
    nueva_planta = st.text_input("Nombre de la planta mencionada:")

    if st.button("Agregar Canción"):
        if nueva_cancion and nueva_planta:
            canciones.append({"cancion": nueva_cancion, "planta": nueva_planta})
            st.success(f"Se agregó la canción '{nueva_cancion}' con la planta '{nueva_planta}'.")
        else:
            st.error("Por favor, completa ambos campos para agregar una canción.")

if __name__ == "__main__":
    main()
