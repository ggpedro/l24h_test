from bs4 import BeautifulSoup
from pandas.io.html import read_html
import requests

id_leiloes =[39495, 39429]

for id_leilao in id_leiloes:
    try:
        historico_leilao=requests.get(f'https://www.lance24h.com.br/DetalhesLances.php?Codigo={id_leilao}&Pagina=1')
        historico = BeautifulSoup(historico_leilao.content,'html.parser')

        # manipulando texto do ultimo lance para conseguir o numero de paginas dos lances
        maior_lance = historico.find_all('td')[1]
        maior_lance_txt = maior_lance.get_text()
        maior_lance_txt = maior_lance_txt.replace(" ", "")
        maior_lance_txt = maior_lance_txt.replace("," , ".")
        maior_lance_txt = maior_lance_txt[4:]
        maior_lance_txt = maior_lance_txt.strip()
        maior_lance = float(maior_lance_txt)

        # se o lance for numero inteiro, o numero de paginas sera o mesmo. caso nao, sera +1 o num inteiro do ultimo lance
        if maior_lance==int(maior_lance):
            num_paginas = int(maior_lance)
        else:
            num_paginas = int(maior_lance)+1

        # para cada pagina, de cada leilao, salvar as informacoes [id_leilao | pagina | data | valor | usuario]
        for pagina in range(1,num_paginas):
            
            tabela = read_html(f'https://www.lance24h.com.br/DetalhesLances.php?Codigo={id_leilao}&Pagina={pagina}', index_col=0, attrs={"class":"BoxTabela1"})
            file_name = './historico.csv'
            tabela[0].to_csv(file_name, sep='\t')
    
    except:
        pass