from scrapy.crawler import CrawlerProcess
from extractionSpider.extractionSpider.spiders.update_spider_jogadores import UpdateJogadoresSpider
from extractionSpider.extractionSpider.spiders.update_spider_estatisticas import UpdateEstatisticasSpider
import time
import schedule

def exec_spider(spider1, spider2):
    print("Iniciando os spiders...")
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "INFO",  # Altere para "DEBUG" se quiser ver mais detalhes
    })
    process.crawl(spider1)
    process.crawl(spider2)
    process.start()
    print("Spiders finalizados.")

# Agendando para toda segunda-feira às 06:00
schedule.every().monday.at("06:00").do(exec_spider, UpdateJogadoresSpider, UpdateEstatisticasSpider)

print("Aguardando o horário para executar os spiders")

# Loop infinito para manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(1)