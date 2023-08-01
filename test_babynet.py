from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

browser.get('http://192.168.2.100:8000/')
time.sleep(3)
browser.maximize_window()
time.sleep(3)

body_pagina = browser.find_element(By.TAG_NAME, 'body')

for item in (1,2,3,4,5):
    body_pagina.send_keys(Keys.PAGE_DOWN)



#### TESTE 1 - CLICAR NOS 4 PRIMEIROS ITENS DA LISTA
# botoes = [1, 2, 3, 4] # itera nos xpaths dos botões

# for item in botoes:
    
#     elemento = browser.find_element(By.XPATH, f'/html/body/section[3]/div/div[{item}]/div/a')

#     # Destacar o elemento alterando o estilo com JavaScript
#     browser.execute_script("arguments[0].style.border='3px solid red';", elemento)
#     time.sleep(1)
#     elemento.click()
#     time.sleep(2)
#     browser.back()
#     time.sleep(1)
    
#### TESTE 2 - REGISTRAR 10 COMPRAS SEGUIDAS DE UM ITEM

elemento = browser.find_element(By.XPATH, '/html/body/section[3]/div/div[2]/div/a')
browser.execute_script("arguments[0].style.border='3px solid red';", elemento)
time.sleep(2)
elemento.click()
time.sleep(2)


for i in range(1,12):

    nome_presente = browser.find_element(By.ID, 'id_nome_presente' )
    quantidade = browser.find_element(By.ID, 'id_quantidade_presenteada' )
    doador_presente = browser.find_element(By.ID, 'id_nome_pessoa' )
    btn_cadastrar = browser.find_element(By.TAG_NAME, 'button')
    select = Select(nome_presente)
    lista_doadores = ['eliel', 'andreia', 'marina', 'maria', 'junia', 'marcia', 'izaquel', 'isabela', 'lucas', 'bruno', 'marli', 'agna']

    select.select_by_value('2')
    quantidade.send_keys('1')
    
    doador_presente.send_keys(f'{lista_doadores[i]}')
    time.sleep(2)
    btn_cadastrar.click()
    time.sleep(2)


browser.quit()
