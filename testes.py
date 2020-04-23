from pandas.io.html import read_html

tabela = read_html('https://www.lance24h.com.br/DetalhesLances.php?Codigo=39422', index_col=0)
file_name = './historico.csv'
tabela[0].to_csv(file_name, sep='\t')