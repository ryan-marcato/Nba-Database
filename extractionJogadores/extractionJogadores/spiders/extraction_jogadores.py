import scrapy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from utils.hash.create_hash import hash_jogadores
from db.querys_insert_update.insert_values import insert_jogadores
from utils.db_utils.execute_query import query_insert_execute
import time

class JogadoresSpider(scrapy.Spider):
    name = 'extractionJogadores'
    
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
        
        rows_jogador = driver.find_elements(By.CLASS_NAME, 'athleteCell__flag')
        
        for row in rows_jogador:
            try:
                id_ = hash_jogadores(i)
                nome_jogador = row.find_element(By.CSS_SELECTOR, 'a.AnchorLink').text
                time_jogador = row.find_element(By.CSS_SELECTOR, 'span.pl2.ns10.athleteCell__teamAbbrev').text
                
                if '/' in time_jogador:
                    time_jogador = None
                    
                query = insert_jogadores(id_, nome_jogador, time_jogador)
                query_insert_execute(query)
                    
                i += 1
            except NoSuchElementException:
                self.log(f'Informações incompletas para o jogador: {row.text}')
    
    def closed(self, reason):
        self.driver.quit()