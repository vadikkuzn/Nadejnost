import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import xlsxwriter

driver = webdriver.Chrome(ChromeDriverManager().install())
workbook = xlsxwriter.Workbook('parse_result.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

money = workbook.add_format({'num_format': '$#,##0'})

worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)
worksheet.write('C1', 'Features', bold)

url = 'https://iotvega.com/product'
driver.get("https://iotvega.com/product")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('a', class_='main-container')
row = 1
col = 0

for n, i in enumerate(items, start=1):
    itemName = i.find('div', class_='product-name').text.strip()
    itemPrice = i.find('span', class_='price_item').text.strip()
    itemFeatures = i.find('ul').text
    worksheet.write(row, col, itemName)
    worksheet.write(row, col + 1, itemPrice, money)
    worksheet.write(row, col + 2, itemFeatures)
    row += 1
    print(f'{n}:  {itemPrice} за {itemName} функции: {itemFeatures}')

workbook.close()