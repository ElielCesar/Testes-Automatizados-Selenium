from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# setup inicial
browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8000/admin/app01/funcionario/add/')
time.sleep(1)
browser.maximize_window()
time.sleep(1)

######### fazer login no sistema
usuario = browser.find_element(By.ID,'id_username')
usuario.send_keys('admin')
password = browser.find_element(By.ID,'id_password')
password.send_keys('35435')
btn_acessar = browser.find_element(By.CSS_SELECTOR,'#login-form > div.submit-row > input[type=submit]')
btn_acessar.click()
time.sleep(1)

menu_funcionario = browser.find_element(By.XPATH, '//*[@id="nav-sidebar"]/div[1]/table/tbody/tr[2]/th/a')
menu_funcionario.click()

add_funcionario = browser.find_element(By.CSS_SELECTOR, '#content-main > ul > li > a')
add_funcionario.click()
time.sleep(2)

# cadastra 20 operadores de caixa
for i in range(0,20):
    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Laura', 'Carlos', 'Mariana', 'Lucas', 'Isabela', 'Gustavo', 'Manuela', 'Daniel', 'Sophia', 'Fernanda', 'Rafael', 'Juliana', 'Leonardo', 'Camila', 'Henrique', 'Larissa']

    emails = [
    "exemplo1@example.com", "exemplo2@example.com","exemplo3@example.com",
    "exemplo4@example.com","exemplo5@example.com","exemplo6@example.com",
    "exemplo7@example.com","exemplo8@example.com","exemplo9@example.com",
    "exemplo10@example.com","exemplo11@example.com","exemplo12@example.com",
    "exemplo13@example.com","exemplo14@example.com","exemplo15@example.com",
    "exemplo16@example.com","exemplo17@example.com","exemplo18@example.com",
    "exemplo19@example.com","exemplo20@example.com" ]

    senhas = [
    "7Hw9b3Yz","5rA1p0Js","2kC6u8Dq","9vX4j7Fg","1mB0o3Nl","4eZ5t6Wx",
    "3sD8i2Mh","6gF7k9Rc","8nL5x1Vb","0pQ2d4Ty","5aR6e3Bc","9jG2w1Kv",
    "2yX4h7Tq","7fW0z3Sm","3pL6x9Dg","6cB8m5Rn","1vF0k7Xj","8tY5g2Ws",
    "4qN3d1Zx","0hM9b6Ry"]

    nome = browser.find_element(By.ID, 'id_nome')
    email = browser.find_element(By.ID, 'id_email')
    senha = browser.find_element(By.ID, 'id_senha')
    cargo = Select(browser.find_element(By.TAG_NAME, 'select'))
    cargo.select_by_value('6')
    botao = browser.find_element(By.XPATH, "//input[@type='submit' and @value='Salvar e adicionar outro(a)' and @name='_addanother']")

    nome.clear()
    nome.send_keys(f'{nomes[i]}')
    time.sleep(0.5)

    email.clear()
    email.send_keys(f'{emails[i]}')
    time.sleep(0.5)

    senha.clear()
    senha.send_keys(f'{senhas[i]}')
    botao.click()
    time.sleep(1)


# cadastra 2 gerentes
for i in range(0,2):
    nomes = ['Waldemar', 'Samuel']
    emails = [ "waldemar@example.com", "samuel@example.com", ]
    senhas = [ "7Hw9b3Yz","5rA1p0Js"]

    nome = browser.find_element(By.ID, 'id_nome')
    email = browser.find_element(By.ID, 'id_email')
    senha = browser.find_element(By.ID, 'id_senha')
    cargo = Select(browser.find_element(By.TAG_NAME, 'select'))
    cargo.select_by_value('1')
    botao = browser.find_element(By.XPATH, "//input[@type='submit' and @value='Salvar e adicionar outro(a)' and @name='_addanother']")

    nome.clear()
    nome.send_keys(f'{nomes[i]}')
    time.sleep(0.5)

    email.clear()
    email.send_keys(f'{emails[i]}')
    time.sleep(0.5)

    senha.clear()
    senha.send_keys(f'{senhas[i]}')
    botao.click()
    time.sleep(1)

# cadastra 2 Entregadores
time.sleep(3)
for i in range(0,2):
    nomes = ['Juliano Matias', 'Eliselton']
    emails = [ "juliano@example.com", "eliselton@example.com", ]
    senhas = [ "7Hw9b3Yz","5rA1p0Js"]

    nome = browser.find_element(By.ID, 'id_nome')
    email = browser.find_element(By.ID, 'id_email')
    senha = browser.find_element(By.ID, 'id_senha')
    cargo = Select(browser.find_element(By.TAG_NAME, 'select'))
    cargo.select_by_value('3')
    botao = browser.find_element(By.XPATH, "//input[@type='submit' and @value='Salvar e adicionar outro(a)' and @name='_addanother']")

    nome.clear()
    nome.send_keys(f'{nomes[i]}')
    time.sleep(0.5)

    email.clear()
    email.send_keys(f'{emails[i]}')
    time.sleep(0.5)

    senha.clear()
    senha.send_keys(f'{senhas[i]}')

    botao.click()
    time.sleep(1)

time.sleep(5)
browser.quit()