# 📊 Gráfico de Corrida de Barras Animado: Análise de Dados da COVID-19

## 🚀 O que este projeto faz?
Nesse projeto, eu utilizo dados públicos da COVID-19 (WHO - World Health Organization Data) para criar uma animação do tipo *Bar Chart Race* no aplicativo de design *Canva*(gráfico de corrida de barras), onde os países "correm" na linha do tempo (Eixo Y - Countries) conforme o número de casos acumulados aumenta ao longo dos meses e anos (Eixo x - Deaths).

---

## 🛠️ Como o projeto foi desenvolvido?

1. **Obtenção dos Dados:** Eu fiz a coleta de dados públicos e globais de saúde da COVID-19 (disponibilizados pela OMS / Kaggle) pelo próprio site, baixei em formato .CSV para começar os trabalhos.
2. **Preparação do Ambiente:** Fiz a Instalação e uso da biblioteca **Pandas** no Python e no computador para manipulação e estruturação dos dados. O Pandas é a biblioteca de código aberto mais popular do Python para análise e manipulação de dados, por isso eu escolhi usar essa biblioteca.
3. **Checklist: Tratamento de Dados com Python (Pandas):**
   * Carregamento do arquivo bruto em formato CSV (`pd.read_csv`).
   * Seleção estratégica apenas das colunas essenciais que são relevantes para tal análise (`Date_reported`, `Country`, `Cumulative_cases`) para otimização da performance.
   * Conversão da coluna de datas para o formato *datetime* (`pd.to_datetime`), garantindo a integridade cronológica dos eventos.
   * **Tratamento Temporal e de Idioma:** Ajuste do formato das datas para o português ("Mês de Ano") e criação de chaves de ordenação para impedir que o computador misture a sequência cronológica por ordem alfabética.
   * **Pivotagem de Dados:** Transformação do formato "longo" original do dataset em um formato "largo" (com os meses nas colunas e os países nas linhas), atendendo exatamente às exigências de ferramentas de animação.
   * Exportação de um arquivo limpo e otimizado (`dados_organizados.csv`).
4. **Superando Limitações de Ferramentas:** Como o Canva possui um limite rígido de linhas e colunas para importação de planilhas (máximo de 1.024 linhas/colunas), utilizei o Python como o meu "motor" de limpeza e agregação mensal para adequar o volume de dados perfeitamente à ferramenta de design.
5. **Criação no Canva:** Utilização do aplicativo de gráficos (*Bar Charts*) dentro do Canva configurado para o modo de corrida de barras (*Bar Chart Race*), transformando dados brutos em um vídeo dinâmico.

---

## 💡 Na Prática: Engenharia e Tratamento de Dados para *Storytelling* Visual
Na área de Dados, dificilmente trabalhamos com um arquivo bruto logo na primeira tentativa. Este projeto colocou em prática um fluxo real de engenharia de dados:

* **Coleta de Dados Reais:** Manipulação de dados longitudinais (série temporal) reais, exatamente o tipo de volume analítico exigido por empresas e governos.
* **Limpeza e Filtragem:** Substituição de planilhas pesadas por código em Python para isolar ruídos e focar apenas nas métricas vitais.
* **Transformação Estrutural:** Reorganização matemática do formato matricial dos dados para visualizações narrativas.
* **Produto Final Visual:** Entrega de um resultado comunicativo e atraente.

---

## ⭐ Por que este projeto é excelente para o meu Portfólio?
Muitos analistas iniciantes limitam-se a entregar apenas gráficos estáticos em relatórios engessados. Ao desenvolver este projeto de **Gráfico de Corrida de Barras Animado**, demonstro habilidades fundamentais:

* Capacidade sólida de tratar, filtrar e estruturar dados utilizando **Python**.
* Domínio de regras de formatação temporal, manipulação de strings e modelagem estrutural com **Pandas**.
* Habilidade de entregar um produto final voltado à **narrativa de dados (*Storytelling*)**, combinando programação com design no Canva — ideal para apresentação em portfólios, posts no LinkedIn, GitHub e processos seletivos.


Fonte:
https://data.who.int/dashboards/covid19/data
https://www.youtube.com/@usandopython
