from bs4 import BeautifulSoup
import requests

""" Selenium

    driver = webdriver.Chrome(executable_path=r'/home/ggpedro/selenium/chromedriver')
    driver.get("https://www.lance24h.com.br/Leiloes_Arrematados.php")
    """
""" Padrões do Site

    Página do leilão: https://www.lance24h.com.br/Detalhes.php?Codigo=39435
    Histórico de lances do leilão: https://www.lance24h.com.br/DetalhesLances.php?Codigo=39435&Pagina=1

    ID_primeiro_leilao = 34238 / Ultimo: 39430
    """

# para cada leilao
for id_leilao in list(range(37240,38423)):
    
    try:
        p_leilao = requests.get(f'https://www.lance24h.com.br/Detalhes.php?Codigo={id_leilao}')
        leilao = BeautifulSoup(p_leilao.content, 'html.parser')
        
        titulo = leilao.find(class_='style1').get_text()
        vencedor = leilao.find(id=f'L_UltimoLogin_{id_leilao}').get_text()
        finalizou_em = leilao.find(class_='ExtText3B').get_text()
        lances_total = leilao.find(id=f'L_QtdLances_{id_leilao}').get_text()
        valor_premio = leilao.find_all(class_='ExtText3B')[1].get_text()
        
        print(f'{id_leilao}|{titulo}|{vencedor}|{finalizou_em}|{lances_total}|{valor_premio}')
    except: 
        pass



# obtem informacoes basicas
# obtem historico de lances