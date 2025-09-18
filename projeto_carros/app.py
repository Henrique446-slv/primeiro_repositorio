import streamlit as st
# st.video("https://www.youtube.com/watch?v=cC12XRzMH28")





import streamlit as st
st.sidebar.title("Henrique'carros")
st.sidebar.image("logo.png")

carros = ['ferrari', 'bmw', 'porsche', 'lamborghini']

opçao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.title(' - Aluguel de Carros de Luxo✨🏎️')

st.image(f'{opçao}.png')
st.markdown(f'## Você alugou o modelo de luxo:{opçao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opçao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opçao}?')
## diaria dos carros
if opçao == 'porsche':
    diaria = 30000

elif opçao == 'bmw':
    diaria = 70000

elif opçao == 'lamborghini':
    diaria = 90000

elif opçao == 'ferrari':
    diaria = 110000

### calcular
if st.button('calcular'):
    dias = int(dias)
    km = float(km)


    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opçao} por {dias} dias e rodou {km}km. O valor total a pagar é R$:{aluguel_total:.2f}')
