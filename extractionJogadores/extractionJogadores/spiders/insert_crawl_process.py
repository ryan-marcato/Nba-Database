from scrapy.crawler import CrawlerProcess
from extractionJogadores.extractionJogadores.spiders.extraction_jogadores import JogadoresSpider
from extractionJogadores.extractionJogadores.spiders.extraction_estatisticas import EstatisticasSpider

def exec_spider(spider):
   print("Iniciando o spider")
   process = CrawlerProcess(settings={
      "LOG_LEVEL": "INFO",  # Altere para "DEBUG" se quiser ver mais detalhes
   })
   process.crawl(spider)
   process.start()
   print("Spider finalizado")

def coleta_jogadores():
   exec_spider(JogadoresSpider)

def coleta_estatisticas_jogadores():
   exec_spider(EstatisticasSpider)
