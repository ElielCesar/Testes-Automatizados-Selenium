from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# setup inicial
browser = webdriver.Chrome()
browser.get('http://192.168.2.100:8000/admin/login/?next=/admin/')
browser.implicitly_wait(5)
browser.maximize_window()


# fazer login
for i in range(0,21):
    # mapeamento
    campo_usuario = browser.find_element(By.ID, 'id_username')
    campo_senha = browser.find_element(By.ID, 'id_password')
    btn_input = browser.find_element(By.CSS_SELECTOR, '#login-form > div.submit-row > input[type=submit]')

    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Laura', 'Carlos', 'Mariana', 'Lucas', 'Isabela', 'Gustavo', 'Manuela', 'Daniel', 'Sophia', 'Fernanda', 'Rafael', 'Juliana', 'admin', 'Leonardo', 'Camila', 'Henrique', 'Larissa', 'admin']

    # acoes
    campo_usuario.clear()
    campo_usuario.send_keys(f'{nomes[i]}')
    
    campo_senha.clear()
    campo_senha.send_keys('35435')
    
    btn_input.click()
    time.sleep(1)

time.sleep(20)

