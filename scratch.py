import requests
from bs4 import BeautifulSoup

url="https://www.youtube.com/feed/trending"

#does not execute the javascript
r= requests.get(url)
print("status code",r.status_code)

with open('trending.html','w') as f:
 f.write(r.text)

soup = BeautifulSoup(r.text,"lxml")
print('Page title:',soup.title.text)

#find all the video divs
video_div = soup.find_all('div',class_="ytd-video-renderer")
print(f'found {len(video_div)} videos')










from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

url="https://www.youtube.com/feed/trending"

#make a function so we don't have to write it alawys

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless') 
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver):
  driver.get(url)
  Video_tag = "ytd-video-renderer"
  v=driver.find_elements(By.TAG_NAME, Video_tag)
  return v
  
if __name__ == "__main__":
  print('creating driver')
  driver = get_driver()
  
  print("fetching trending videos")
  videos=get_videos(driver)
  print(f'found {len(videos)} videos')
  
  print ('parsigng the first video')
  #title,url, thumbnail url,channel, views,upload descriptiom

  video=videos[0]
  title_tag= video.find_element(By.ID, "video-title")
  title = title_tag.text
  url= title_tag.get_attribute('href')
  thumbnail_tag=video.find_element(By.TAG_NAME,'img')
  thumbnail_url= thumbnail_tag.get_attribute('src')
  channel_class= video.find_element(By.CLASS_NAME,
  'ytd-channel-name')
  Channel_Name= channel_class.text
  description = video.find_element(By.ID,"description-text").text

  #view_class = "ytd-video-meta-block"
  View = video.find_element(By.CLASS_NAME,
  "style-scope ytd-video-meta-block")
  Views = View.text
  
  print('title:',title)
  print('url:',url)
  print('Thumbnail URL:',thumbnail_url)
  print('Channel Name:', Channel_Name)
  print('Description',description)
  print('Views and Uploaded time:',Views)