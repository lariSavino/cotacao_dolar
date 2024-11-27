from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from reportlab.pdfgen import canvas
from webdriver_manager.chrome import ChromeDriverManager
import time

# Função para capturar a cotação
def capturar_cotacao():
    # Configurar o Selenium
    service = Service(ChromeDriverManager().install())  # Ajuste o caminho do seu driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Executar sem abrir o navegador
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=service, options=options)

    # Acessar o site de cotação
    url = "https://www.google.com/search?q=cotação+dólar"
    driver.get(url)
    time.sleep(2)  # Aguardar carregamento

    # Capturar o valor da cotação
    cotacao = None
    try:
        elemento_cotacao = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
        cotacao = elemento_cotacao.text  # Acessa o atributo text corretamente
    except Exception as e:
        print("Erro ao capturar cotação:", e)
    finally:
        driver.quit()  # Sempre encerre o driver
    
    return cotacao

# Função para gerar o PDF
def gerar_pdf(cotacao):
    nome_arquivo = "cotacao_dolar.pdf"
    c = canvas.Canvas(nome_arquivo)
    c.drawString(100, 750, "Relatório de Cotação do Dólar")
    c.drawString(100, 700, f"Cotação atual do dólar: {cotacao}")
    c.drawString(100, 650, f"Data: {time.strftime('%d/%m/%Y %H:%M:%S')}")
    c.save()
    print(f"Relatório salvo como: {nome_arquivo}")

# Fluxo principal
if __name__ == "__main__":
    cotacao_dolar = capturar_cotacao()
    if cotacao_dolar:
        print(f"Cotação capturada: {cotacao_dolar}")
        gerar_pdf(cotacao_dolar)
    else:
        print("Não foi possível capturar a cotação.")
