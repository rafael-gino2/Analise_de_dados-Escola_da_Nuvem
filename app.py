import streamlit as st
import pandas as pd
import plotly.express as px

# Paleta de cores personalizada
PALETA_CORES = [ '#04c0df', '#ccd5dc', '#417183', '#0478aa']

# =================== FUNÇÃO DE CARGA PRINCIPAL ===================
def carregar_dados_dashboard(path_csv):
    df = pd.read_csv(path_csv)
    df['Data de Desistência do Curso'] = pd.to_datetime(df['Data de Desistência do Curso'], dayfirst=True, errors='coerce')
    df['Hora da modificação'] = pd.to_datetime(df['Hora da modificação'], dayfirst=True, errors='coerce')

    total_matriculas = len(df)
    desistentes = df["Data de Desistência do Curso"].notna().sum()
    ativos = df["Data de Desistência do Curso"].isna().sum()

    status_map = {
        "Aprovado": ["Aprovado", "Passou", "Passed"],
        "Reprovado": ["Não passou", "Reprovado", "NoShow", "Reprovado por falta", "Desistente"]
    }

    def classificar_resultado(valor):
        valor = str(valor).lower()
        for aprov in status_map['Aprovado']:
            if aprov.lower() in valor:
                return "Aprovado"
        return "Reprovado"

    cert_data = {}
    for cert in ["AWS Certified Cloud Practitioner", "AWS Certified Solutions Architect Associate"]:
        if cert in df.columns:
            raw = df[cert].dropna()
            classificado = raw.apply(classificar_resultado)
            contagem = classificado.value_counts().to_dict()
            cert_data[cert] = contagem

    desistencias = df[(df['Estágio'] == 'Desistência') | (df['Estágio'] == 'Sem interesse')].copy()
    desistencias['Data Desistência'] = desistencias['Data de Desistência do Curso'].fillna(desistencias['Hora da modificação'])
    desistencias['Mês/Ano'] = desistencias['Data Desistência'].dt.to_period('M')
    desistencias = desistencias[desistencias['Mês/Ano'] >= '2024-10']
    desistencias_mes = desistencias['Mês/Ano'].value_counts().sort_index().reset_index()
    desistencias_mes.columns = ['Mês/Ano', 'Desistências']
    desistencias_mes['Mês/Ano'] = desistencias_mes['Mês/Ano'].astype(str)

    aws_ccp = df[['Hora da modificação', 'AWS Certified Cloud Practitioner']].dropna()
    aws_ccp['Resultado'] = aws_ccp['AWS Certified Cloud Practitioner'].apply(classificar_resultado)
    aws_ccp['Mês'] = aws_ccp['Hora da modificação'].dt.strftime('%b')
    evolucao = aws_ccp.groupby(['Mês', 'Resultado']).size().reset_index(name='Quantidade')

    motivos_raw = df["Motivo da Desistência"].dropna()
    motivos = motivos_raw.value_counts().reset_index()
    motivos.columns = ['Motivo', 'Quantidade']
    motivos = motivos.head(5)

    return {
        "total_matriculas": total_matriculas,
        "desistentes": desistentes,
        "ativos": ativos,
        "certificacoes": cert_data,
        "desistencias_mes": desistencias_mes,
        "evolucao_certificacao": evolucao,
        "motivos_desistencia": motivos
    }

# =================== CONFIG LAYOUT ===================
st.set_page_config(page_title=" Exploração dos dados da Escola da Nuvem", layout="wide")
st.sidebar.markdown(
    """
    <h2 style='color: #04c0df; text-align: center;'>📊  Exploração dos dados da Escola da Nuvem </h2>
    """,
    unsafe_allow_html=True
)

# Logo ou imagem institucional
st.sidebar.image("logo_1.png", use_container_width=True)

# Separador visual
st.sidebar.markdown("---")

# Menu principal com ícones
menu = st.sidebar.selectbox(
    "🔍 Navegue pelo conteúdo:",
    ["🏠 Início", "📋 Processo seletivo", "📊 Análise de Matrículas", "🎓 Análise de Alunos"]
)

# Separador visual
st.sidebar.markdown("---")

# Pequena frase de impacto ou institucional
st.sidebar.markdown(
    """
    <div style='text-align: center; color: #ccd5dc; font-size: 13px;'>
        Desenvolvido com ❤️ por João, Kayque, Rafael e Samantha<br>
        Powered by Streamlit & Plotly
    </div>
    """,
    unsafe_allow_html=True
)

# Configuração de cor da sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #041433;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st

import streamlit as st

if menu == "🏠 Início":
    st.markdown("<h1 style='color: #04c0df;'>🏠 Bem-vindo ao Painel de Análise da Escola da Nuvem</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        # Container com scroll interno
        st.markdown(
            """
            <div style='max-height: 85vh; overflow-y: auto; padding-right: 10px;'>
            <p><b>Projeto:</b> Análise exploratória da Escola da Nuvem dividida em três áreas: Processo Seletivo, Matrículas e Perfil dos Alunos. Visualização com Streamlit e Plotly.</p>

            <p>🎯 <b>Objetivo</b>: Entender o comportamento dos alunos no processo seletivo, curso e pós-certificação para identificar melhorias, reduzir desistências e potencializar resultados.</p>

            <hr>

            <p><b>1. Etapas de Desqualificação</b></p>
            <ul>
                <li>Identificar as etapas com maior desqualificação de candidatos.</li>
                <li>Visualizar status dos processos.</li>
            </ul>

            <hr>

            <p><b>2. Análise de Matrículas</b></p>
            <ul>
                <li>Evolução das certificações por mês.</li>
                <li>Principais razões de desistência.</li>
                <li>Quantidade de desistências ao longo dos meses.</li>
            </ul>

            <hr>

            <p><b>3. Análise de Alunos</b></p>
            <ul>
                <li>Localização geográfica.</li>
                <li>Faixa etária média.</li>
                <li>Origem dos alunos.</li>
                <li>Nível de escolaridade.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.image("teste1.png", use_container_width=True)

    # CSS para evitar scroll da página e limitar altura
    st.markdown(
        """
        <style>
        /* Limita a altura total da página e remove scroll */
        .main.css-1v3fvcr {
            height: 95vh;
            overflow: hidden;
        }
        /* Container padrão do streamlit padding menor */
        .css-18e3th9 {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        </style>
        """, unsafe_allow_html=True
    )

# =================== VISUALIZAÇÃO: Análise de Matrículas ===================
if menu == "📊 Análise de Matrículas":
    st.title("📊 Análise de Matrículas")
    path_csv = "Matriculas_pii_none.csv"
    with st.spinner("Carregando dados..."):
        dados = carregar_dados_dashboard(path_csv)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Matrículas", dados["total_matriculas"])
    col2.metric("Total de Desistentes", dados["desistentes"])
    col3.metric("Total de Ativos", dados["ativos"])

    row1_left, row1_col1, row1_col2, row1_col3, row1_right = st.columns([0.05, 0.3, 0.3, 0.3, 0.05])

    cert1 = list(dados["certificacoes"].items())[0] if len(dados["certificacoes"]) > 0 else None
    if cert1:
        cert_name, valores = cert1
        fig1 = px.pie(
            names=list(valores.keys()),
            values=list(valores.values()),
            title=cert_name,
            height=250,
            color_discrete_sequence=PALETA_CORES
        )
        row1_col1.plotly_chart(fig1, use_container_width=True)

    cert2 = list(dados["certificacoes"].items())[1] if len(dados["certificacoes"]) > 1 else None
    if cert2:
        cert_name, valores = cert2
        fig2 = px.pie(
            names=list(valores.keys()),
            values=list(valores.values()),
            title=cert_name,
            height=250,
            color_discrete_sequence=PALETA_CORES
        )
        row1_col2.plotly_chart(fig2, use_container_width=True)

    fig3 = px.bar(
        dados["desistencias_mes"],
        x="Mês/Ano",
        y="Desistências",
        color_discrete_sequence=PALETA_CORES,
        title="📉 Desistências por Mês",
        height=250
    )
    row1_col3.plotly_chart(fig3, use_container_width=True)

    row2_left, row2_col1, row2_col2, row2_right = st.columns([0.05, 0.45, 0.45, 0.05])

    fig4 = px.bar(
        dados["evolucao_certificacao"],
        x="Mês",
        y="Quantidade",
        color="Resultado",
        barmode="group",
        color_discrete_map={"Aprovado": "#04c0df", "Reprovado": "#041433"},
        title="📈 Evolução de Certificação AWS CCP por Mês",
        height=300
    )
    row2_col1.plotly_chart(fig4, use_container_width=True)

    fig5 = px.bar(
        dados["motivos_desistencia"],
        x="Motivo",
        y="Quantidade",
        color_discrete_sequence=PALETA_CORES,
        title="❌ Principais Motivos de Desistência",
        height=300
    )
    row2_col2.plotly_chart(fig5, use_container_width=True)

# =================== VISUALIZAÇÃO: Processo seletivo ===================
elif menu == "📋 Processo seletivo":
    st.title("📋 Processo seletivo")

    df = pd.read_csv("processos_seletivos_pii_none.csv")
    df.columns = df.columns.str.strip()

    df_etapas = df[['Etapa de Desqualificação']].dropna()
    df_etapas['Etapa de Desqualificação'] = df_etapas['Etapa de Desqualificação'].str.strip().str.title()
    contagem = df_etapas['Etapa de Desqualificação'].value_counts().sort_values(ascending=False)
    top5_df = contagem.head(5).reset_index()
    top5_df.columns = ['Etapa', 'Quantidade']

    fig6 = px.bar(
        top5_df,
        x='Etapa',
        y='Quantidade',
        color='Etapa',
        title='Top 5 Etapas de Desqualificação',
        color_discrete_sequence=PALETA_CORES,
        height=500
    )

    df['Etapa de Desqualificação'] = df['Etapa de Desqualificação'].astype(str).str.strip().str.title()
    df['Status do Processo'] = df['Status do Processo'].astype(str).str.strip().str.title()
    df_socio = df[df['Etapa de Desqualificação'] == 'Formulário Socioeconômico']

    status_counts = df_socio['Status do Processo'].value_counts().reset_index()
    status_counts.columns = ['Status do Processo', 'Quantidade']

    fig7 = px.pie(
        status_counts,
        names='Status do Processo',
        values='Quantidade',
        color_discrete_sequence=PALETA_CORES,
        height=500
    )

    left, col1, col2, right = st.columns([0.05, 0.45, 0.45, 0.05])

    with col1:
        st.plotly_chart(fig6, use_container_width=True)

    with col2:
        st.plotly_chart(fig7, use_container_width=True)

# =================== VISUALIZAÇÃO: Analise de alunos ===================
elif menu == "🎓 Análise de Alunos":
    st.title("🎓Análise de Alunos")

    try:
        df = pd.read_csv('alunos_pii_none.csv')

        # --- 1. Análise por Cidade ---
        st.header('🏙️ Estados com mais discrepância de alunos')
        if 'Cidade de Correspondência' in df.columns:
            alunos_por_cidade = df['Cidade de Correspondência'].value_counts().head(5)
            idade_media_cidade = df.groupby('Cidade de Correspondência')['Idade'].mean().loc[alunos_por_cidade.index]

            cidade_df = pd.DataFrame({
                'Número de Alunos': alunos_por_cidade,
                'Idade Média': idade_media_cidade
            })

            col1, col2, col3 = st.columns([1.2, 1.2, 2])
            with col1:
                st.subheader("📋 Tabela")
                st.dataframe(cidade_df)
            with col2:
                st.subheader("📊 Gráfico")
                st.bar_chart(alunos_por_cidade)
            with col3:
                st.subheader("🧠 Observação Analítica")
                st.markdown("""
                As cidades com maior número de alunos refletem a concentração populacional e econômica.  
                **São Paulo**, por exemplo, é um centro industrial e financeiro que atrai moradores e, consequentemente, mais matrículas escolares.  
                Essa concentração pode indicar melhor acesso à educação, mas também desafios como superlotação e desigualdade regional.
                """)

        # --- 2. Análise por Origem ---
        st.header('🌐 De qual mídia os alunos vieram?')
        if 'Origem' in df.columns:
            origem_contagem = df['Origem'].value_counts().head(5)
            idade_media_origem = df.groupby('Origem')['Idade'].mean().loc[origem_contagem.index]

            origem_df = pd.DataFrame({
                'Número de Alunos': origem_contagem,
                'Idade Média': idade_media_origem
            })

            col1, col2, col3 = st.columns([1.2, 1.2, 2])
            with col1:
                st.subheader("📋 Tabela")
                st.dataframe(origem_df)
            with col2:
                st.subheader("📊 Gráfico")
                st.bar_chart(origem_contagem)
            with col3:
                st.subheader("🧠 Observação Analítica")
                st.markdown("""
                As principais origens de descoberta do curso mostram o impacto de **mídias sociais, indicações e estratégias de marketing**.  
                Essa análise pode orientar investimentos em divulgação e reforçar os canais mais eficazes de captação de alunos.
                """)

        # --- 3. Análise por Escolaridade ---
        st.header('🎓 Distribuição por Escolaridade')
        if 'Escolaridade' in df.columns:
            escolaridade_contagem = df['Escolaridade'].value_counts()

            col1, col2, col3 = st.columns([1.2, 1.2, 2])
            with col1:
                st.subheader("📋 Tabela")
                st.dataframe(escolaridade_contagem)
            with col2:
                st.subheader("📊 Gráfico")
                st.bar_chart(escolaridade_contagem)
            with col3:
                st.subheader("🧠 Observação Analítica")
                st.markdown("""
                É importante destacar a presença significativa de alunos com **Ensino Superior Incompleto**.  
                Isso pode indicar um público que começou a graduação, mas não concluiu, o que pode ser sinal de dificuldades acadêmicas, financeiras ou de adaptação.  
                Reconhecer essa realidade é fundamental para desenvolver estratégias que **ajudem esses alunos a retomar e concluir seus estudos**.
                """)

        # --- 4. Análise por Faixa Etária ---
        st.header('🎯 Distribuição por Faixa Etária')
        if 'Idade' in df.columns:
            bins = [0, 18, 25, 35, 45, 60, 100]
            labels = ['0-18', '19-25', '26-35', '36-45', '46-60', '60+']
            df['Faixa Etária'] = pd.cut(df['Idade'], bins=bins, labels=labels, right=False)
            faixa_etaria_contagem = df['Faixa Etária'].value_counts().sort_index()

            col1, col2, col3 = st.columns([1.2, 1.2, 2])
            with col1:
                st.subheader("📋 Tabela")
                st.dataframe(faixa_etaria_contagem)
            with col2:
                st.subheader("📊 Gráfico")
                st.bar_chart(faixa_etaria_contagem)
            with col3:
                st.subheader("🧠 Observação Analítica")
                st.markdown("""
                A faixa etária dos alunos fornece insights sobre o **momento de vida e necessidades** do público.  
                Uma maioria entre 19 e 35 anos, por exemplo, pode indicar busca por qualificação para o mercado de trabalho.  
                Já uma distribuição mais ampla reforça a **diversidade etária** e a importância da educação ao longo da vida.
                """)

    except FileNotFoundError:
        st.error("Arquivo 'alunos_pii_none.csv' não encontrado no diretório atual.")

