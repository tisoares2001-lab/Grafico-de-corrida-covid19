# 📊 Bar Chart Race: Análise de Dados COVID-19 (WHO)

### 🎯 Atenção: Desafiando as limitações técnicas de ferramentas de visualização
Ferramentas de design como o Canva são excelentes para *storytelling*, mas possuem restrições rígidas — como o limite de importação de 1.024 linhas e colunas. Como transformar um volume massivo de dados temporais brutos da OMS (Organização Mundial da Saúde) em um gráfico dinâmico e fluido sem travar o processo? Este projeto demonstra exatamente como utilizo **Python** para atuar como um motor de engenharia e processamento de dados, superando barreiras técnicas para entregar uma visualização de impacto.

---

### 🔍 Interesse: O desafio por trás da animação
O objetivo foi processar um *dataset* longitudinal da COVID-19 que continha registros diários desde 2020. Exibir dados diários em uma corrida de barras tornaria a visualização poluída e ininteligível. 

**A solução técnica aplicada:**
*   **Limpeza e Filtragem:** Utilizei a biblioteca **Pandas** em Python para isolar ruídos e focar nas colunas vitais (`Date_reported`, `Country`, `Cumulative_cases`).
*   **Transformação Estrutural:** Realizei a conversão cronológica de datas (*datetime*) e a **pivotagem** dos dados, transformando o formato "longo" original em um formato "largo" (agregado por mês).
*   **Tratamento Temporal e de Idioma:** Criei chaves de ordenação cronológica personalizadas, garantindo que os meses fossem exibidos em português e na sequência temporal correta (evitando falhas de ordenação alfabética).

---

### ✨ Desejo: Por que este projeto destaca meu perfil técnico?
Recrutadores e gestores de dados buscam profissionais capazes de transformar complexidade em clareza. Este portfólio evidencia três competências essenciais do meu perfil em Análise de Dados:

1.  **Domínio de Ferramentas e Linguagens:** Fluência em manipulação avançada de *DataFrames* com **Python/Pandas**.
2.  **Visão de Negócio e Storytelling:** Compreensão de que os dados precisam ser digeríveis para diferentes públicos. A integração do código com o Canva mostra que sei traduzir análises complexas em produtos visuais altamente comunicativos.
3.  **Autonomia e Resolução de Problemas:** Capacidade de contornar limitações de software através de scripting e tratamento prévio dos dados.

---

### 🚀 Ação: Vamos conectar?
Este repositório é uma demonstração prática de como transformo dados brutos em insights visuais e acionáveis. 

*   **Fonte dos Dados:** [WHO COVID-19 Dashboard Data](https://data.who.int/dashboards/covid19/data)
*   **Inspiração e Tutoriais:** [Canal Usando Python](https://www.youtube.com/@usandopython)
*   **Contato:** Sinta-se à vontade para explorar meus outros projetos no GitHub ou entrar em contato comigo pelo LinkedIn para discutirmos oportunidades na área de dados!

---
