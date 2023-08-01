'''
Objetivo: inserir avaliacões de 4 jurados diferentes para apenas um candidato
especificado no final da url e no id_participante
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

# mudar numero da url conforme candidato
browser.get('http://127.0.0.1:8000/fantasy/julgamento/5') 
browser.maximize_window()
time.sleep(3)



for i in (1, 2, 3, 4):
    # mudar num conforme candidato
    id_participante = '5' 

    participante = Select(browser.find_element(By.ID, 'id_participante'))
    participante.select_by_value(id_participante)
    time.sleep(1)

    jurado = Select(browser.find_element(By.ID, 'id_jurado'))
    jurado.select_by_value(str(i))

    estetica = [0, 6, 6, 6, 7]
    criatividade = [0, 3, 3, 3, 9]
    performance = [0, 5, 5, 5, 8]

    nota_estetica = browser.find_element(By.ID, 'id_nota_estetica')
    nota_criatividade = browser.find_element(By.ID, 'id_nota_criatividade')
    nota_performance = browser.find_element(By.ID, 'id_nota_performance')

    nota_estetica.send_keys(estetica[i])
    nota_criatividade.send_keys(criatividade[i])
    nota_performance.send_keys(performance[i])

    salvar = browser.find_element(By.ID, 'salvar')
    salvar.click()
    time.sleep(7)










