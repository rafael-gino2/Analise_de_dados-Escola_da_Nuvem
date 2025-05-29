import pandas as pd

def carregar_dados_dashboard(path_csv):
    df = pd.read_csv(path_csv)

    # Pré-tratamento
    df['Data de Desistência do Curso'] = pd.to_datetime(df['Data de Desistência do Curso'], dayfirst=True, errors='coerce')
    df['Hora da modificação'] = pd.to_datetime(df['Hora da modificação'], dayfirst=True, errors='coerce')

    # Métricas gerais
    total_matriculas = len(df)
    desistentes = df["Data de Desistência do Curso"].notna().sum()
    ativos = df["Data de Desistência do Curso"].isna().sum()

    # Certificações (CCP e SAA)
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

    # Desistências por mês (a partir de Out/2024)
    desistencias = df[(df['Estágio'] == 'Desistência') | (df['Estágio'] == 'Sem interesse')].copy()
    desistencias['Data Desistência'] = desistencias['Data de Desistência do Curso'].fillna(desistencias['Hora da modificação'])
    desistencias['Mês/Ano'] = desistencias['Data Desistência'].dt.to_period('M')
    desistencias = desistencias[desistencias['Mês/Ano'] >= '2024-10']
    desistencias_mes = desistencias['Mês/Ano'].value_counts().sort_index().reset_index()
    desistencias_mes.columns = ['Mês/Ano', 'Desistências']
    desistencias_mes['Mês/Ano'] = desistencias_mes['Mês/Ano'].astype(str)

    # Evolução de Certificação AWS CCP por mês
    aws_ccp = df[['Hora da modificação', 'AWS Certified Cloud Practitioner']].dropna()
    aws_ccp['Resultado'] = aws_ccp['AWS Certified Cloud Practitioner'].apply(classificar_resultado)
    aws_ccp['Mês'] = aws_ccp['Hora da modificação'].dt.strftime('%b')
    evolucao = aws_ccp.groupby(['Mês', 'Resultado']).size().reset_index(name='Quantidade')

    # Motivos de Desistência
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
