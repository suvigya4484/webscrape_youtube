import pandas as pd
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

def parse_video(video):
  #title,url, thumbnail url,channel, views,upload descriptiom
  title_tag= video.find_element(By.ID, "video-title")
  title = title_tag.text
  url= title_tag.get_attribute('href')
  thumbnail_tag=video.find_element(By.TAG_NAME,'img')
  thumbnail_url= thumbnail_tag.get_attribute('src')
  channel_class= video.find_element(By.CLASS_NAME,
  'ytd-channel-name')
  Channel_Name= channel_class.text
  description = video.find_element(By.ID,
  "description-text").text
  return{
  'title':title,
  'Url':url,
  'Thumbnail URL':thumbnail_url,
  'Channel Name': Channel_Name,
  'Description':description
  
  }
  
if __name__ == "__main__":
  print('creating driver')
  driver = get_driver()
  
  print("fetching trending videos")
  videos=get_videos(driver)
  print(f'found {len(videos)} videos')
  
  print ('parsigng top 50 videos')
  
  videos_data= [parse_video(video) for video in videos[:50]]
  #print(videos_data)

  print('save the data to csv')
  video_df = pd.DataFrame(videos_data)
  print(video_df)
  video_df.to_csv('top_10_trending.csv',index=None)
