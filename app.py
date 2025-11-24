import streamlit as st

# ====================================
# CONFIGURAÇÃO
# ====================================
st.set_page_config(
    page_title="Martin",
    layout="wide",
    page_icon="📘"
)

# CSS azul — sem formas decorativas
st.markdown("""
    <style>
    body {
        background-color: #0A0A0A;
    }
    .sidebar .sidebar-content {
        background-color: #000A1A !important; /* azul bem escuro */
    }
    .main {
        background-color: #0D0D1A; /* leve tom azul escuro */
    }
    h1, h2, h3, p, li, label {
        color: #A8C7FF !important; /* azul claro */
    }
    .css-1d391kg, .css-1avcm0n {
        color: #A8C7FF !important;
    }
    .card {
        padding: 20px;
        background-color: #0F1A33; /* azul escuro */
        border-radius: 0px; /* remove formas arredondadas */
        box-shadow: none; /* remove sombras */
        margin-bottom: 20px;
        border: 1px solid #1A2D4C; /* linha azul suave */
    }

    /* Remove emojis de botões da sidebar */
    .sidebar .stButton>button {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)


# ====================================
# CONTROLE DE NAVEGAÇÃO
# ====================================
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page):
    st.session_state.page = page


# ====================================
# SIDEBAR
# ====================================
st.sidebar.title("Martin — Conteúdos")
st.sidebar.markdown("---")

menu_items = {
    "Home": "Início",
    "Decisão e Repetição": "Decisão e Repetição",
    "Vetores e Matrizes": "Vetores e Matrizes",
    "Funções e Bibliotecas": "Funções e Bibliotecas",
    "Registros": "Registros",
    "Arquivos em Disco": "Arquivos em Disco",
    "Recursividade": "Recursividade",
    "Big O": "Complexidade (Big O)",
    "APIs externas": "Uso de APIs externas",
}

for key, label in menu_items.items():
    if st.sidebar.button(label, use_container_width=True):
        go_to(key)

st.sidebar.markdown("---")
st.sidebar.write("Feito por Martin")


# ====================================
# PÁGINAS — CONTEÚDOS COMPLETOS
# ====================================

# ---------- HOME ----------
def home():
    st.title("Martin — Plataforma de Estudos")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    Projeto desenvolvido para estudo de:
    - Algoritmos
    - Estrutura de Dados
    - Análise de Complexidade
    - Recursividade
    - Vetores e Matrizes
    - Arquivos
    - APIs

    Use o menu lateral para navegar.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- DECISÃO E REPETIÇÃO ----------
def decisao():
    st.title("Estruturas de Decisão e Repetição")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Estruturas de Decisão (if/elif/else)")
    st.write("A tomada de decisão executa código conforme condições.")
    st.code("""
x = 10
if x > 5:
    print("Maior que 5")
else:
    print("Menor ou igual a 5")
""")

    st.subheader("Estruturas de Repetição (for/while)")
    st.code("""
for i in range(1, 6):
    print("Número:", i)

contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1
""")

    st.subheader("Teste interativo")
    numero = st.number_input("Digite um número:", value=5)
    if st.button("Testar"):
        st.write(f"O dobro de {numero} é {numero * 2}")

    st.subheader("Exercício")
    st.write("""
    Peça 5 números e exiba:
    - Soma total  
    - Maior valor  
    - Média  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- VETORES ----------
def vetores():
    st.title("Vetores e Matrizes")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Vetores são listas; matrizes são listas de listas.")
    st.code("""
vetor = [10, 20, 30]

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
""")

    st.subheader("Soma de Vetor")
    valores = st.text_input("Digite valores (ex: 1,2,3,4):", "1,2,3,4")
    if st.button("Somar"):
        lista = [int(x) for x in valores.split(",")]
        st.write("Soma =", sum(lista))

    st.subheader("Exercício")
    st.write("Some a diagonal principal de uma matriz 3x3.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FUNÇÕES ----------
def funcoes():
    st.title("Funções e Bibliotecas")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.code("""
def soma(a, b):
    return a + b
""")

    st.subheader("Teste")
    a = st.number_input("A:")
    b = st.number_input("B:")
    if st.button("Somar"):
        st.write("Resultado =", a + b)

    st.subheader("Exercício")
    st.write("Faça uma função que retorna o menor elemento de uma lista.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- REGISTROS ----------
def registros():
    st.title("Registros (Structs)")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Python usa classes para simular registros.")
    st.code("""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
""")

    st.subheader("Teste")
    nome = st.text_input("Nome:")
    idade = st.number_input("Idade:", value=18)
    if st.button("Criar Pessoa"):
        st.write(f"Pessoa criada: {nome}, {idade} anos")

    st.subheader("Exercício")
    st.write("Crie um registro com nome, notas e média automática.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- ARQUIVOS ----------
def arquivos():
    st.title("Arquivos em Disco")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.code("""
with open("dados.txt", "w") as f:
    f.write("Olá mundo!")
""")

    texto = st.text_input("Texto para salvar:")
    if st.button("Salvar arquivo"):
        with open("saida.txt", "w") as f:
            f.write(texto)
        st.success("Arquivo salvo!")

    st.subheader("Exercício")
    st.write("Leia um arquivo e conte suas linhas.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- RECURSIVIDADE ----------
def recursividade():
    st.title("Recursividade")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.code("""
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)
""")

    n = st.number_input("Calcular fatorial de:", value=5)

    def fatorial(n):
        if n <= 1:
            return 1
        return n * fatorial(n-1)

    if st.button("Calcular"):
        st.write("Resultado =", fatorial(n))

    st.subheader("Exercício")
    st.write("Faça uma função recursiva que soma os números de 1 a N.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- BIG O ----------
def big_o():
    st.title("Complexidade (Big O)")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    Medida de crescimento de algoritmos:
    - O(1)
    - O(n)
    - O(n²)
    - O(log n)
    """)

    st.code("""
for i in range(n):  # O(n)
    print(i)
""")

    st.subheader("Exercício")
    st.write("Classifique dois loops aninhados.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- APIs ----------
def apis():
    st.title("Uso de APIs Externas")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.code("""
import requests
r = requests.get("https://api.github.com/users")
print(r.json())
""")

    if st.button("Consultar API pública"):
        import requests
        r = requests.get("https://api.agify.io/?name=martin")
        st.write(r.json())

    st.subheader("Exercício")
    st.write("Crie um programa que exibe a temperatura atual via API.")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================================
# ROTEAMENTO
# ====================================
pages = {
    "Home": home,
    "Decisão e Repetição": decisao,
    "Vetores e Matrizes": vetores,
    "Funções e Bibliotecas": funcoes,
    "Registros": registros,
    "Arquivos em Disco": arquivos,
    "Recursividade": recursividade,
    "Big O": big_o,
    "APIs externas": apis
}

pages[st.session_state.page]()
