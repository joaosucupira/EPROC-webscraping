import yaml # type: ignore
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from driver_setup import initialize_driver
from openpyxl import Workbook


class Scraper(ABC):
    def __init__(self, config_file):
        self.driver = initialize_driver()
        self.config = self.carregar_config(config_file)
        # self.driver = None
    
    def carregar_config(self, config_file) :
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)
    
    @abstractmethod
    def processar_config(self):
        self.term = self.config.get('search_term', '')

    @abstractmethod
    def buscar(self):
        pass
    
    def executar(self):
        try:
            self.buscar()
        except Exception as e:
            print(f"Erro de execução do scraper: {e}")
        finally:
            self.encerrar()
    
    @abstractmethod
    def encerrar(self):
        pass

