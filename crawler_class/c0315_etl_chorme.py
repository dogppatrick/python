from selenium.webdriver import Chrome
import p
import time
from pytube import Playlist
driver = Chrome("./chromedriver")
driver.get("https://www.youtube.com/view_all_playlists")


driver.find_element_by_id("identifierId").send_keys("dogpatrick.demo@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(3)
driver.find_element_by_class_name("whsOnd").send_keys(p.pwd())
driver.find_element_by_id("passwordNext").click()
time.sleep(7)
playlists = driver.find_elements_by_class_name("vm-video-title-text")
# .text -> .text
# ["href"] -> get_attribute("href")
for p in playlists:
    print(p.text, p.get_attribute("href"))
    pl = Playlist(p.get_attribute("href"), suppress_exception=True)
    pl.download_all('./youtube')
# sleep讓她處理完所有事情
time.sleep(3)
driver.close()