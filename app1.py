import streamlit as st

# Configuração da página para uma melhor experiência visual
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Minha Primeira Calculadora em Streamlit")
st.write("Bem-vindo ao mundo do **Vibe Coding**! Use os campos abaixo para realizar seus cálculos de forma rápida e elegante.")

# Criação de um layout em colunas para organizar os inputs de forma limpa
col1, col2 = st.columns(2)

with col1:
    # 2. Primeiro campo de entrada numérica com valor padrão 0.0
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    # 2. Segundo campo de entrada numérica com valor padrão 0.0
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("---")

# 4. Botão de ação com o texto "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    # Lógica para cada tipo de operação selecionada
    resultado = None
    erro = False
    
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        # 5. Tratamento de divisão por zero
        if num2 == 0:
            erro = True
            st.error("⚠️ Ops! Não é possível realizar uma divisão por zero. Tente outro número.")
        else:
            resultado = num1 / num2

    # Se o cálculo for válido, mostre o resultado em grande destaque
    if not erro and resultado is not None:
        st.success("Cálculo realizado com sucesso! 🎉")
        st.metric(label="Resultado Final", value=f"{resultado:.4f}")
