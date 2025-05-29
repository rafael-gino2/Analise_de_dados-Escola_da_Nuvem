# ☁️ Análise de Dados - Escola da Nuvem

Este projeto consiste em uma análise exploratória dos dados da *Escola da Nuvem*, com foco em três áreas principais:

- Processo Seletivo  
- Matrículas  
- Perfil dos Alunos  

O trabalho foi realizado com *Python, utilizando **Pandas* para manipulação de dados, *Plotly* para visualizações interativas, e *Streamlit* para a criação de um dashboard web acessível e dinâmico.

---

## 🎯 Objetivo

O objetivo do projeto foi entender o comportamento dos alunos ao longo das etapas do processo seletivo, durante o curso e após as certificações. Com isso, buscamos:

- Identificar pontos de melhoria
- Reduzir taxas de desistência
- Potencializar os resultados da Escola da Nuvem
- Fornecer insights estratégicos que apoiem a tomada de decisões e a melhoria contínua das ações educacionais e operacionais

---

## 📊 Principais Análises e Insights

### 1. 📋 Análise do Processo Seletivo

#### 📌 Insight 1: Etapas com mais desclassificações
A análise revelou que a etapa do *Formulário Socioeconômico* é a que mais elimina candidatos, sugerindo:

- Dificuldades no preenchimento
- Critérios de seleção que podem não estar claros
- Falta de suporte a candidatos em situação de vulnerabilidade

#### 📌 Insight 2: Perfil dos reprovados e desinteressados
Ao cruzar os dados de *status no processo* com a *renda familiar*, observou-se que:

- Muitos reprovados ou desistentes estão em situação socioeconômica delicada
- O desinteresse pode estar ligado à *falta de apoio ou motivação*, não necessariamente à falta de capacidade

#### ⚠️ Reflexão Crítica
Candidatos com potencial estão sendo perdidos por barreiras que não são de mérito. É uma oportunidade para:

- Reavaliar critérios de desqualificação
- Criar ações inclusivas e acolhedoras
- Ouvir os desinteressados antes de rotulá-los como inaptos

---

### 2. 📊 Análise de Matrículas

#### 🔍 Foco do grupo
Nosso grupo focou principalmente na relação entre *reprovações nos cursos AWS* e a *quantidade de desistências*.

- Os gráficos mostram que *a maioria dos alunos que fazem os cursos AWS são reprovados*
- O mês com mais reprovações (Outubro) coincidiu com o mês com *maior número de desistências*
- Um dos principais *motivos de desistência* relatados foi: *Motivos de Saúde/Pessoais*

#### 📌 Insight
A *alta reprovação* parece gerar *desmotivação* e contribui diretamente para a *evasão*. Isso destaca a necessidade de:

- Suporte emocional e psicológico aos alunos
- Estratégias pedagógicas para evitar frustrações e desistências

---

### 3. 🎓 Análise do Perfil dos Alunos

Fizemos uma análise do público-alvo da Escola da Nuvem com foco nos seguintes aspectos:

- *Localização Geográfica*: Identificação das regiões com mais alunos
- *Faixa Etária Média*: Perfil etário predominante
- *Origem dos Alunos*: Como chegaram até a escola (indicação, redes sociais etc.)
- *Nível de Escolaridade*: Escolaridade antes do ingresso

Essas informações permitem *personalizar ações de comunicação, seleção e formação* mais eficientes.

---

## 🛠️ Tecnologias Utilizadas

- *Python*
- *Pandas* – Manipulação e análise de dados
- *Plotly* – Visualizações interativas
- *Streamlit* – Criação da interface web
- *VS Code / Jupyter Notebook*

---

## 📈 Funcionalidades do Dashboard

- Filtros por curso, mês, status, localidade e outros
- Tabelas dinâmicas com busca e ordenação
- Gráficos de linha, barras, pizza e mapas geográficos
- Destaque de insights com base nos filtros aplicados

---

## 📁 Estrutura do Projeto

├── __pycache__/
├── venv/
├── alunos_pii_none.csv
├── alunos_pii_none.xlsx
├── app.py # Aplicativo streamlit
├── carregar_dados_dashboard.py
├── logo_1.png
├── logo_2.png
├── Matriculas_pii_none.csv
├── Matriculas_pii_none.xlsx
├── processos_seletivos_pii_none.csv
├── processos_seletivos_pii_none.xlsx
├── teste1.png


## ▶️ Como acessar o projeto?
Para rodar o dashboard localmente, siga os passos abaixo:
- Clone ou baixe este repositório
- Instale as bibliotecas necessárias no terminal: pip install streamlit pandas plotly
- Execute o aplicativo com o Streamlit: streamlit run app.py
- O dashboard será aberto automaticamente no navegador (geralmente em http://localhost:8501).


