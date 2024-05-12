import streamlit as st

def hello_world():
    return "Olá Turma de Dados! Aula de Docker, fiz alteração no meu codigo"


def main():
    st.write(hello_world())


if __name__ == "__main__":
    main()