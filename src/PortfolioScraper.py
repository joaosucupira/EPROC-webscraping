import time
from driver_setup import close_driver
from Scraper import Scraper, By, Keys, Workbook

class PortfolioScraper(Scraper):
    file = '../configs/config_portfolio.yml'

    def __init__(self, config_file=file):
        super().__init__(config_file)
        self.path = ""
        self.term = ""
        self.titulos = []
        self.executar()
        self.encerrar()

    def processar_config(self):
        self.path = self.config.get('web_path')
        self.term = self.config.get('search_term')
        self.driver.get(self.path)

    def buscar_titulo(self) :
        # element = self.driver.find_element(By.XPATH, self.config.get('title_xpath'))
        element = self.get_element_xpath('title_xpath')
        text = element.text
        print(text)
        time.sleep(3)

    def get_element_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, self.config.get(xpath))

    # def lista_arvore(self):
    #     for i in range(1,5):
    #         element = self.driver.find_element(By.XPATH, self.config.get(
    #             f'/html/body/div[2]/div[2]/ul[1]/ul/li[{i}]/a'
    #         ))
    #         if (element.text.isalpha): print(element.text)
    #         else : print(f'Elemento "{i}" nao é texto.')

    def buscar(self):
        element = self.get_element_xpath('tree1_xpath')
        print(element.text)
        time.sleep(3)


    def executar(self):
        self.processar_config()
        self.buscar()
        # self.lista_arvore()

    def encerrar(self):
        close_driver(self.driver, wait_time=5)