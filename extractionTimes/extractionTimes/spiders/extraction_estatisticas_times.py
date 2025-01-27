from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.hash.create_hash import hash_times
from db.querys_insert_update.insert_values import insert_estatisticas_times
from utils.db_utils.execute_query import query_insert_execute

class TimeEstatisticasSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def parse(self, url):
        driver = self.driver
        driver.get(url)
        
        table_parent = driver.find_element(By.CSS_SELECTOR, 'div.Table__ScrollerWrapper.relative.overflow-hidden')
        row_estatiscas = table_parent.find_elements(By.CSS_SELECTOR, 'tbody.Table__TBODY tr.Table__TR.Table__TR--sm.Table__even')
        
        for i, row in enumerate(row_estatiscas):
            id_ = hash_times(i)
            estatisticas = [td.text for td in row.find_elements(By.CSS_SELECTOR, 'td.Table__TD')]
            
            query = insert_estatisticas_times(id_, estatisticas)
            query_insert_execute(query)
    
    def close(self):
        self.driver.quit()
        
if __name__ == "__main__":
    spider = TimeEstatisticasSpider()
    try:
        spider.parse("https://www.espn.com.br/nba/estatisticas/time")
    finally:
        spider.close()