import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🛒", layout="centered")

st.title("Calculadora de Compras")

precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão (1kg)": 8.50,
    "Leite (1L)": 4.90,
    "Café (500g)": 14.20,
    "Açúcar (1kg)": 4.30,
    "Óleo de Soja (900ml)": 6.80,
    "Pão de Forma": 7.50,
}

def calcular_preco_total(itens_selecionados):
    return sum(precos_itens[item] for item in itens_selecionados)

itens_selecionados = st.multiselect("Selecione os itens:", list(precos_itens.keys()))

if itens_selecionados:
    for item in itens_selecionados:
        st.write(f"- {item}: R$ {precos_itens[item]:.2f}")
    st.metric("Total da Compra", f"R$ {calcular_preco_total(itens_selecionados):.2f}")
else:
    st.info("Nenhum item selecionado.")
