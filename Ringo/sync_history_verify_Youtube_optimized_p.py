import re
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://dev-ringoadmin.trailfive.com/auth/login")
# driver.get("https://ringoadmin.trailfive.com/")

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("admin")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sync History']").click()

no_of_pages = driver.find_element(By.XPATH, "(//button[@aria-label='Go to next page']/parent::li/preceding-sibling::li)[last()]").text
print(no_of_pages)

for i in range(1, int(no_of_pages) + 1):
    print(i)
    if i > 172:
        for j in range(1, 8):
            try:
                expand_icon_locator = By.XPATH, f"//tbody/tr[{j}]/td[1]/*[local-name()='svg']"
                youtube_link_locator = By.XPATH, f"//tbody/tr[{j}]/td[8]/a"
                track_title_locator = By.XPATH, f"//tbody/tr[{j+1}]/td[2]/div[1]"

                expand_icon = wait.until(EC.presence_of_element_located(expand_icon_locator))
                expand_icon.click()

                track_title_text = driver.find_element(*track_title_locator).text
                split_text = re.split(' |;', track_title_text)
                len_split_text = len(split_text)
                track_title = ' '.join(split_text[len_split_text-1:]).strip()

                youtube_link = wait.until(EC.element_to_be_clickable(youtube_link_locator))
                driver.execute_script("arguments[0].click();", youtube_link)

                try:
                    window_handles = driver.window_handles
                    new_window_handle = window_handles[-1]
                    driver.switch_to.window(new_window_handle)
                    youtube_track_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='title']//yt-formatted-string[@class='style-scope ytd-watch-metadata']"))).text
                    if youtube_track_title.__contains__(track_title):
                        pass
                    else:
                        print(track_title, "youtube title tracK:  " + youtube_track_title)

                    driver.close()
                    original_window_handle = window_handles[0]
                    driver.switch_to.window(original_window_handle)
                    expand_icon = wait.until(EC.presence_of_element_located(expand_icon_locator))
                    expand_icon.click()
                except:
                    expand_icon = wait.until(EC.presence_of_element_located(expand_icon_locator))
                    expand_icon.click()
                    print("Youtube not opened")
            except TimeoutException:
                print(f"Timeout waiting for element on Page {i}, Record {j}")
                expand_icon = wait.until(EC.presence_of_element_located(expand_icon_locator))
                expand_icon.click()
                continue
            except:
                print(f"Exception on Page {i}, Record {j}")

        try:
            driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()
        except NoSuchElementException:
            pass
    else:
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()

time.sleep(5)
