import scrapy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from utils.hash.create_hash import hash
from db.querys_insert_update.insert_values import insert_estatisticas_jogadores
from utils.db_utils.execute_query import query_insert_execute
import time

class EstatisticasSpider(scrapy.Spider):
    name = 'firsEstatisticas'
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def start_requests(self):
        urls = ['https://www.espn.com.br/nba/estatisticas/jogador']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'driver': self.driver})
            
    def parse(self, response):
        driver = self.driver
        driver.get(response.url)
        
        while True:
            try:
                botao = driver.find_element(By.CLASS_NAME, "AnchorLink.loadMore__link")
                botao.click()
                self.log('Botao "mostrar mais" clicado')
                time.sleep(3)
            except NoSuchElementException:
                self.log('Botao "mostrar mais" nao foi encontrado')
                break
        
        #numero para o hash
        i = 0
        
        table_parent = driver.find_element(By.CSS_SELECTOR, 'div.Table__ScrollerWrapper.relative.overflow-hidden')
        rows_estatiticas = table_parent.find_elements(By.CSS_SELECTOR, 'tbody.Table__TBODY tr.Table__TR.Table__TR--sm.Table__even')
        
        for row in rows_estatiticas:
            try:
                id_ = hash(i)
                estatisticas = [td.text for td in row.find_elements(By.CSS_SELECTOR, 'td.Table__TD')]
                
                query = insert_estatisticas_jogadores(id_, estatisticas)
                query_insert_execute(query)
                
                i += 1
            except NoSuchElementException:
                self.log(f'Informações incompletas para o jogador: {row.text}')
        
    def closed(self, reason):
        self.driver.quit()