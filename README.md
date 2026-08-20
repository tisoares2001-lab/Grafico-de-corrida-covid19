# 📊 Bar Chart Race: Análise de Dados COVID-19 (WHO)


Este projeto tem como objetivo transformar um volume massivo de dados temporais brutos da OMS (Organização Mundial da Saúde) sobre a COVID-19 em uma visualização dinâmica e fluida. 

O principal desafio técnico do projeto foi contornar as restrições de ferramentas de design focadas em *storytelling* — como o Canva, que possui um limite de importação de apenas 1.024 linhas e colunas. Para superar essa barreira, utilizei **Python** como um motor de engenharia e processamento prévio, garantindo que a visualização final não travasse e fosse de fácil compreensão.

### ⚙️ Processamento e Solução Técnica
O *dataset* original continha registros longitudinais diários desde 2020. Para evitar uma corrida de barras poluída, apliquei as seguintes etapas de tratamento:

*   **Limpeza e Filtragem:** Utilizei a biblioteca **Pandas** para isolar ruídos e focar apenas nas colunas vitais (`Date_reported`, `Country`, `Cumulative_cases`).
*   **Transformação Estrutural:** Realizei a conversão cronológica de datas (*datetime*) e a **pivotagem** dos dados, transformando o formato "longo" original em um formato "largo", agregando os números por mês.
*   **Tratamento Temporal e de Idioma:** Criei chaves de ordenação personalizadas para garantir que os meses fossem exibidos em português e na sequência cronológica correta (evitando falhas de ordenação alfabética padrão do sistema).

### 🛠️ Competências Aplicadas
Este repositório serve como uma demonstração prática das seguintes habilidades em Análise de Dados:
*   Manipulação avançada de *DataFrames* com Python/Pandas.
*   Autonomia e resolução de problemas para contornar limitações de software através de *scripting*.
*   Visão de negócio para traduzir informações complexas em produtos visuais acessíveis para diferentes públicos.

### 🔗 Referências e Contato
*   **Fonte dos Dados:** [WHO COVID-19 Dashboard Data](https://data.who.int/dashboards/covid19/data)
*   **Inspiração e Tutoriais:** [Canal Usando Python](https://www.youtube.com/@usandopython)
*   **Contato:** Explore meus outros projetos ou conecte-se comigo pelo [LinkedIn](https://linkedin.com/in/tisoares2001).
