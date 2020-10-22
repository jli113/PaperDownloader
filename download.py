import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from selenium import webdriver
from fake_useragent import UserAgent
import sys

'''
#Get the available address of scihub
from fake_useragent import UserAgent
from selenium import webdriver
import os
headers = {'User-Agent': UserAgent().random}
url = 'https://lovescihub.wordpress.com/'
abspath = os.path.abspath(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(executable_path=abspath)
browser.get(url)
findcurrentscihub = browser.find_element_by_xpath('//*[@id="post-22"]/div/p[2]/a[1]') 
findcurrentscihub = browser.find_element_by_xpath('//*[@id="post-22"]/div/p[2]/a[2]') 
findcurrentscihub = browser.find_element_by_xpath('//*[@id="post-22"]/div/p[2]/a[3]') 
findcurrentscihub = browser.find_element_by_xpath('//*[@id="post-22"]/div/p[2]/a[4]') 
scihub = findcurrentscihub.get_attribute('href')
browser.quit()'''

df = pd.read_csv('./1.csv')
n = len(df)
abspath = os.path.abspath(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

for i in range(0,n):
    headers = {'User-Agent': UserAgent().random}
    title = df.loc[i,'title']
    #if sys.getsizeof(title) < 255:        
    title = title.replace('?','').replace(':','：').replace('/','-').replace('a\c','ac').replace('S\~','S')
    file = title+'.pdf'
    if os.path.isfile(file) == True:
        print('File {} already downloaded'.format(i))
    elif len(os.getcwd()+'/'+file) > 250:
        print('File name is too long.\n'+title)
    else:
        browser = webdriver.Chrome(executable_path=abspath)
        url = df.loc[i,'url']
        print(title)
        browser.get(url)
        time.sleep(10)
        try:
            searchelement = browser.find_element_by_id('download-pdf-popover')                       
            searchelement.click()
            downloadoption = browser.find_element_by_xpath('//*[@id="popover-content-download-pdf-popover"]/div/div/a[1]')
            href = downloadoption.get_attribute('href')
            print('popover: '+href)
            pdf = requests.get(href, headers=headers, timeout=30)
            redirect = BeautifulSoup(pdf.content, 'html.parser')
            for redirect_message in tqdm(redirect.find_all(id="redirect-message")):
                click_url = redirect_message.find('a').get('href')
                click = requests.get(click_url, headers=headers, timeout=30)
                with open(title+'.pdf','wb') as output:
                    output.write(click.content)
        except:
            try:
                searchelement = browser.find_element_by_xpath('//*[@id="screen-reader-main-content"]/div/div[2]/a')
                href = searchelement.get_attribute('href')
                print('directLink: '+href)
                pdf = requests.get(href, headers=headers, timeout=30)
                redirect = BeautifulSoup(pdf.content, 'html.parser')
                for redirect_message in tqdm(redirect.find_all(id="redirect-message")):
                    click_url = redirect_message.find('a').get('href')
                    click = requests.get(click_url, headers=headers, timeout=30)
                    with open(title+'.pdf','wb') as output:
                        output.write(click.content)
            except:
                
                downloadoption = browser.find_element_by_xpath('//*[@id="doi-link"]/a[1]')
                doi = downloadoption.get_attribute('href')
                '''
                #print('No access, contact the library or try scihub.')
                browser.get('https://sci-hub.ee/')
                browser.find_element_by_xpath('//*[@id="input"]/form/input[2]').send_keys(doi)
                browser.find_element_by_xpath('//*[@id="open"]').click()
                time.sleep(30)
                href = browser.find_element_by_xpath('//*[@id="pdf"]').get_attribute('src')
                href = href.replace('#view=FitH','')
                '''
                with open('TBDFS.txt','w+') as file:
                    file.write(title+' '+doi+'\n')
        
        time.sleep(10)
        browser.quit()
    
