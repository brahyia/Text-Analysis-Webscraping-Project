import pandas as pd
import sqlite3
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())



s = Service('/opt/homebrew/Caskroom/chromedriver/104.0.5112.79/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get('https://patient.info/forums/discuss/16-year-old-scared-of-colon-cancer-681901')
question = driver.find_element(By.XPATH, "//*[@class = 'moderation-conent']")
question = question.get_attribute('value')

dates = driver.find_elements(By.XPATH, "//*[@class = 'fuzzy']")
dates = [date.get_attribute('datetime') for date in dates]
stripped_dates = [date[0:10] for date in dates]

Topics = driver.find_elements(By.XPATH, "//*[@class = 'u-h1 post__title']")
Topics = [Topic.text for Topic in Topics]
len(Topics)


answers = driver.find_elements(By.XPATH, "//*[@itemprop = 'text']/input")
answers = [answer.get_attribute('value') for answer in answers]


authors = driver.find_elements(By.CLASS_NAME, 'author__name')
authors = [author.text for author in authors]

recipients = driver.find_elements(By.CLASS_NAME, 'author__recipient')
recipients = [author.text for author in recipients]
len(recipients)

df1 = pd.DataFrame({
    'author': authors,
    'recipient': [''] + recipients,
    'post': [question] + answers,
    'date': stripped_dates,
    'Title':
})
df2 = pd.DataFrame({
    'Title': Topics
})
# df = pd.DataFrame.from_dict(df1, orient='index')
# df = df.transpose()

df1['post'] = df1['post'].astype('|S')



# +31 682 339 682 Jan Janiszewski

conn = sqlite3.connect('depforumSpiderdb.sqlite')
cur = conn.cursor()
df1.to_sql('tablename10', con=conn, if_exists='replace')
df2.to_sql('tablename10', con=conn, if_exists='append')

pd.read_sql('Select * FROM "tablename6"', con=conn)
