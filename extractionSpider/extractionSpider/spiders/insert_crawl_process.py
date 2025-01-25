from scrapy.crawler import CrawlerProcess
from extractionSpider.extractionSpider.spiders.first_scraping_jogadores import JogadoresSpider
from extractionSpider.extractionSpider.spiders.first_scraping_estatisticas import EstatisticasSpider
import time

def exec_spider(spider1, spider2):
    print("Iniciando o spider")
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "INFO",  # Altere para "DEBUG" se quiser ver mais detalhes
    })
    process.crawl(spider1)
    process.crawl(spider2)
    process.start()
    print("Spider finalizado")
    
exec_spider(EstatisticasSpider, JogadoresSpider)