from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.hash.create_hash import hash_times
from db.querys_insert_update.insert_values import insert_times
from utils.db_utils.execute_query import query_insert_execute

siglas_dict = {
    'Memphis Grizzlies': 'MEM',
    'Cleveland Cavaliers': 'CLE',
    'Denver Nuggets': 'DEN',
    'Boston Celtics': 'BOS',
    'New York Knicks': 'NY',
    'Sacramento Kings': 'SAC',
    'Oklahoma City Thunder': 'OKC',
    'Chicago Bulls': 'CHI',
    'Atlanta Hawks': 'ATL',
    'Indiana Pacers': 'IND',
    'Dallas Mavericks': 'DAL',
    'Milwaukee Bucks': 'MIL',
    'Houston Rockets': 'HOU',
    'Phoenix Suns': 'PHX',
    'Detroit Pistons': 'DET',
    'San Antonio Spurs': 'SA',
    'Los Angeles Lakers': 'LAL',
    'Toronto Raptors': 'TOR',
    'Utah Jazz': 'UTAH',
    'Golden State Warriors': 'GS',
    'Miami Heat': 'MIA',
    'Minnesota Timberwolves': 'MIN',
    'LA Clippers': 'LAC',
    'New Orleans Pelicans': 'NO',
    'Philadelphia 76ers': 'PHI',
    'Portland Trail Blazers': 'POR',
    'Washington Wizards': 'WSH',
    'Charlotte Hornets': 'CHA',
    'Brooklyn Nets': 'BKN',
    'Orlando Magic': 'ORL'
}

class TimesSpider:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, url):
        driver = self.driver
        driver.get(url)

        dados = [time.text for time in driver.find_elements(By.CSS_SELECTOR, 'a.AnchorLink')]
        resultado = [item for item in dados[37:97] if item != '']

        for i, time in enumerate(resultado):
            id_ = hash_times(i)
            nome_time = time
            sigla_time = siglas_dict.get(nome_time)
            
            query = insert_times(id_, nome_time, sigla_time)
            query_insert_execute(query)
            

    def close(self):
        self.driver.quit()


def coleta_times():
    spider = TimesSpider()
    try:
        spider.parse("https://www.espn.com.br/nba/estatisticas/time")
    finally:
        spider.close()