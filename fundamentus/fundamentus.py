import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

url = 'https://www.fundamentus.com.br/resultado.php'

driver.get(url)

table_path = '/html/body/div[1]/div[2]/table'

element = driver.find_element('xpath', table_path)

table_html = element.get_attribute('outerHTML')

table = pd.read_html(str(table_html), thousands = '.', decimal = ',')[0]

table = table.set_index('Papel')

table = table[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses']]

table['ROIC'] = table['ROIC'].str.replace('%', "")
table['ROIC'] = table['ROIC'].str.replace('.', "")
table['ROIC'] = table['ROIC'].str.replace(',', ".")
table['ROIC'] = table['ROIC'].astype(float)

table = table[table['Liq.2meses'] > 1000000]
table = table[table['EV/EBIT'] > 0]
table = table[table['ROIC'] > 0]

table['ranking_ev_ebit'] = table['EV/EBIT'].rank(ascending=True)
table['ranking_ev_ebit'] = table['ROIC'].rank(ascending=False)
table['ranking_total'] = table['ranking_ev_ebit'] + table['ranking_ev_ebit']

table = table.sort_values('ranking_total')

print(table.head(10))