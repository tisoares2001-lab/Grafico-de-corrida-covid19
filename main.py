import pandas as pd

# Carregando o arquivo
df = pd.read_csv("data.csv")

# Selecionando apenas as colunas necessárias
df_subset = df[['Date_reported', 'Country', 'Cumulative_cases']].copy()

# Convertendo a coluna de datas para o tipo datetime
df_subset['Date_reported'] = pd.to_datetime(df_subset['Date_reported'])

# Dicionário para traduzir os meses para português
meses_pt = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June ', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

# Criando colunas auxiliares de Ano, Mês e o rótulo formatado por extenso
df_subset['Year'] = df_subset['Date_reported'].dt.year
df_subset['Month_Num'] = df_subset['Date_reported'].dt.month
df_subset['Month_Name'] = df_subset['Month_Num'].map(meses_pt)
df_subset['Period_Label'] = df_subset['Month_Name'] + ' of ' + df_subset['Year'].astype(str)

# Chave para ordenação cronológica correta (Ano-Mês)
df_subset['Sort_Key'] = df_subset['Date_reported'].dt.to_period('M')

# Agrupando por mês e pegando o valor máximo do período
monthly_cases = df_subset.groupby(['Sort_Key', 'Period_Label', 'Country'])['Cumulative_cases'].max().reset_index()
monthly_cases = monthly_cases.sort_values('Sort_Key')

# Filtrando apenas os top 10 países com mais casos no total geral
total_cases_by_country = df_subset.groupby('Country')['Cumulative_cases'].max()
top_10_countries = total_cases_by_country.sort_values(ascending=False).head(10).index
df_top_10 = monthly_cases[monthly_cases['Country'].isin(top_10_countries)]

# Criando a tabela pivô mantendo a ordem cronológica correta dos meses
pivot_data = df_top_10.pivot_table(index='Country', columns=['Sort_Key', 'Period_Label'], values='Cumulative_cases', aggfunc='last')

# Ajustando as colunas para exibirem apenas o nome por extenso (ex: "Janeiro de 2020")
pivot_data.columns = [col[1] for col in pivot_data.columns]

# Preenchendo valores vazios com 0 e salvando o novo arquivo organizado
pivot_data = pivot_data.fillna(0)
pivot_data.to_csv('dados_organizados.csv')

print("Arquivo gerado com sucesso! Os meses agora estão por extenso em ordem cronológica.")