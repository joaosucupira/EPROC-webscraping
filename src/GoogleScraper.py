import time
from driver_setup import close_driver
from Scraper import Scraper, By, Keys, Workbook


class GoogleScraper(Scraper):
    file = '../configs/config_padrao.yml'

    def __init__(self, config_file=file):
        super().__init__(config_file)
        # self.term = term
        self.term = ""
        self.titulos = []
        self.executar()
        self.encerrar()

    def processar_config(self):
        self.term = self.config.get('search_term', '')

    def buscar(self):
        self.driver.get("https://google.com")
        search_box = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_box.send_keys(self.term + Keys.ENTER)
        time.sleep(3)
        # super.buscar()

    def filtra_titulos(self):
        resultados = self.driver.find_elements(By.TAG_NAME, "h3")

        for r in resultados:
            self.titulos.append(r.text)

    def mostra_titulos(self) :
        for titulo in self.titulos:
            print(titulo)

    def grava_titulos(self) :
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Resultados para " + self.term
        sheet.append(["Título"])

        for titulo in self.titulos:
            sheet.append([titulo])

        arquivo = f"resultados_{self.term}.xlsx"
        workbook.save(arquivo)
        print(f"Títulos salvos em '{arquivo}'.")

    def executar(self):
        self.processar_config()
        self.buscar()
        self.filtra_titulos()
        self.mostra_titulos()
        # self.grava_titulos()
    
    def encerrar(self):
        close_driver(self.driver, wait_time=5)


