from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get(
    "https://https://www.amazon.com.br/Caibalion-Estudo-Filosofia-Herm%C3%A9tica-Antigo/dp/8531500710.com"
)


def clicar_no_botao_login():
    try:
        # 1ª Tentativa: A "Alma" (ID) - Rápido e direto
        print("Buscando pelo ID...")
        botao = driver.find_element(By.ID, "login_btn")
        botao.click()
        print("Sucesso via ID!")

    except NoSuchElementException:
        # Se cair aqui, o ID sumiu! Hora da Blindagem (XPath ou CSS)
        print("ERRO: ID não encontrado. Iniciando blindagem via XPath...")

        try:
            # 2ª Tentativa: Buscar pelo TEXTO do botão (Muito resiliente)
            # O XPath abaixo procura qualquer botão que contenha o texto 'Entrar'
            botao = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Entrar')]"
            )
            botao.click()
            print("Sucesso via XPath (Texto)!")

        except NoSuchElementException:
            # 3ª Tentativa: CSS Selector (Pela classe)
            print("ERRO: XPath falhou. Tentando CSS Selector...")
            botao = driver.find_element(By.CSS_SELECTOR, ".auth-button")
            botao.click()
            print("Sucesso via CSS!")


# Executa a função
clicar_no_botao_login()
