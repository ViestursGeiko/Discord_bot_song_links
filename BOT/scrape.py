from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def discord_url(song_name):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--enable-chrome-browser-cloud-management")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.youtube.com/')
    time.sleep(2)

    #cookies
    driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div').click()
    time.sleep(1)
    #search bar click and send keys
    search = driver.find_element(By.NAME, "search_query").send_keys(song_name)
    driver.find_element(By.ID, 'search-icon-legacy').click()
    time.sleep(2)

    findurl = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
    findname = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
    
    song_name = findname.text
    link = findurl.get_attribute("href")

    return [song_name, link]

    driver.quit()
