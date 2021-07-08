# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    return browser



def get_feature_image():
    browser = init_browser()
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    html = browser.html
    image_soup = bs(html, 'html.parser')

    base_url = 'https://spaceimages-mars.com/'
    featured_image_url = image_soup.find_all('img')[1]['src']
    featured_image_url = base_url + featured_image_url
    browser.quit()
    return(featured_image_url)

def get_mars_table():

    df = pd.read_html('https://galaxyfacts-mars.com/')[0]
    df.columns = ['description', 'Mars', 'earth']
    df.set_index('description',inplace=True)
    df_html = df.to_html(classes = "table table-striped")
    return(df_html)



def get_hem_url():
    browser = init_browser()
    hem_url = 'https://marshemispheres.com/'
    browser.visit(hem_url)
    scrape_data = []
    html = browser.html
    hem_soup = bs(html, 'html.parser')
    browser.back()
    #print(hem_soup)
    for x in range(4):
        hem_title = hem_soup.find_all('h3')[x].text
        img = hem_soup.find_all('img', class_='thumb')
        full_image = img[x]['src']
        img_url = hem_url + full_image
        scrape_data.append({"title":hem_title,"image_url":img_url})
        
    return(scrape_data)



def scrape_all():
    browser = init_browser()
    mars_url = 'https://redplanetscience.com/'
    browser.visit(mars_url)

    html = browser.html
    mars_soup = bs(html, 'html.parser')
    news_title = mars_soup.find('div', class_='content_title').text
    news_p = mars_soup.find('div',class_="article_teaser_body").text
    browser.quit()

    mars_data = {
        'news_title': news_title,
        'news_article': news_p,
        'featured_image_url': get_feature_image(),
        'mars_table': get_mars_table(),
        'hemisphere_image_urls' : get_hem_url()
    }
    
    return mars_data



if __name__ == "__main__":
    scrape_all()
