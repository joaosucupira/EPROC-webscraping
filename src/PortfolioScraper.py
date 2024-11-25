
PATH = "https://processos.utfpr.edu.br/portfolio/index.php"


import time
from driver_setup import close_driver
from Scraper import Scraper, By, Keys, Workbook

class PortfolioScraper(Scraper):
    file = '../configs/config_portfolio.yml'

    def __init__(self, config_file=file):
        self.path = 'https://processos.utfpr.edu.br/portfolio/index.php'
        super().__init__(config_file)
        self.term = ""
        self.titulos = []
        self.executar()
        self.encerrar()

    def processar_config(self):
        self.term = self.config.get('search_term', '')
    
    def buscar(self):
        self.driver.get(self.path)
        element = self.driver.find_element(By.XPATH, self.config.get('title_xpath'))
        text = element.text
        print(text)
        
        time.sleep(3)

    def executar(self):
        self.processar_config()
        self.buscar()

    def encerrar(self):
        close_driver(self.driver, wait_time=5)