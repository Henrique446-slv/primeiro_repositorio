import streamlit as st

# Dados de exemplo
generos = ["Funk", "Trap", "Rap", "Pagode"]

# Dicionário relacionando gêneros aos seus livros
musica_por_genero = {
    "Funk": ["MC IG", "MC Menor Da VG", "MC Hariel"],
    "Trap": ["TZ Da Coronel", "Matue", "Kayblack"],
    "Rap": ["Snoop Dog", "50 cent", "Sabotage"],
    "Pagode": ["Ferrugem", "Péricles", "zeca pagodinho"]
}

# Selectbox para escolher o gênero    
st.sidebar.image('logo.png')            
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionado = st.sidebar.selectbox(
        "Selecione a mùsica:", 
        musica_por_genero[genero_selecionado]
    )

# mostrar apenas o artista selecionado
if genero_selecionado == "Funk" and musica_selecionado == "MC IG":
    st.title("MC IG\n")
    st.video ("https://youtu.be/J8kbUgAFq4s?si=L5hC5aUwX0WssuwT")


elif genero_selecionado == "Funk" and musica_selecionado == "MC Menor da VG":
    st.title("MC Menor da VG\n")
    st.video ("https://youtu.be/hBeMgyTcWGg?si=XvIN7Hj5MgJoM0TH")
    
elif genero_selecionado == "Funk" and musica_selecionado == "MC hariel":
    st.title("MC hariel\n")
    st.video ("https://youtu.be/W7JI_SQaXpU?si=04Qxp83MpI8RE116")


elif genero_selecionado == "Trap" and musica_selecionado == "TZ Da Coronel":
    st.title("TZ Da Coronel\n")
    st.video ("https://youtu.be/OpU9Q8xMYSs?si=bX_qTE8gy-4fm2Ox")

elif genero_selecionado == "Trap" and musica_selecionado == "Matue":
    st.title("Matue\n")
    st.video ("https://youtu.be/m226f2reF28?si=MwbQqFkbXor1AJZs")

elif genero_selecionado == "Trap" and musica_selecionado == "Kayblack":
    st.title("Kayblack\n")
    st.video ("https://youtu.be/sQzchBJ2KvM?si=0WGtvjY0BfXx4uBy")


elif genero_selecionado == "Rap" and musica_selecionado == "Snoop Dog":
    st.title("Snoop Dog\n")
    st.video ("https://youtu.be/UDApZhXTpH8?si=eDokZJoP8xFXReCY")

elif genero_selecionado == "Rap" and musica_selecionado == "50 cent":
    st.title("50 cent\n")
    st.video ("https://youtu.be/5qm8PH4xAss?si=qlIR0lfvAiZxci3T")

elif genero_selecionado == "Rap" and musica_selecionado == "Sabotage":
    st.title("Sabotage\n")
    st.video ("https://youtu.be/GA7LcSX8tYE?si=humTbUllH2LT2y9i")


elif genero_selecionado == "Pagode" and musica_selecionado == "Ferrugem":
    st.title("Ferrugem\n")
    st.video ("https://youtu.be/o3dknP3jclw?si=ZPsEyzy7GL40As5U")

elif genero_selecionado == "Pagode" and musica_selecionado == "Péricles":
    st.title("Péricles\n")
    st.video ("https://youtu.be/T3Y6RRSDm4o?si=6aof6QzvRpkfeZ3Z")

elif genero_selecionado == "Pagode" and musica_selecionado == "zeca pagodinho":
    st.title("zeca pagodinho\n")
    st.video ("https://youtu.be/oTREAvZbmME?si=5VKtqj94vyvLE1fh")
    

    