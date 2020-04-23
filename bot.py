from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# configurando chromedriver para heroku

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument = ('--headless')
chrome_options.add_argument = ('--disable-dev-shm-usage')
chrome_options.add_argument = ('--no-sandbox')
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options) 

# dados do leilao e login

id_leilao = 39571
login = 'LA 22K'
senha = '21466635'

# login

browser = webdriver.Chrome('/home/ggpedro/selenium/chromedriver')
browser.get('https://www.lance24h.com.br/Login.php')
select = browser.find_element_by_id('Log_Email')
select.click()
select.send_keys(login)
select = browser.find_element_by_id('Log_Senha')
select.click()
select.send_keys(senha)
select.send_keys(Keys.ENTER)
time.sleep(2)

# pagina do leilao

browser.get(f'https://www.lance24h.com.br/Detalhes.php?Codigo={id_leilao}')

while browser.find_element_by_id(f'L_BotaoA_{id_leilao}') != 'Arrematado':
    dez_s = browser.find_element_by_id(f'L_ContDown_1_{id_leilao}').text
    uni_s = browser.find_element_by_id(f'L_ContDown_2_{id_leilao}').text
    seg = int(dez_s + uni_s)

    if seg == 1:
        time.sleep(0.6)
        if seg == 1:
            botao = browser.find_element_by_id(f'L_BotaoA_{id_leilao}')
            botao.click()
            time.sleep(2)
            
        else:
            pass
    else:
        pass
    
browser.close