import time
from selenium.common.exceptions import StaleElementReferenceException
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
driver.get("https://dev-ringoadmin.trailfive.com/auth/login")

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("admin")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sync History']").click()

# driver.find_elements(By.XPATH, "//table//tr//td[3]")
# ad_title_links = driver.find_elements(By.XPATH, "//table//tr//td[3]")


no_of_pages = driver.find_element(By.XPATH, "(//button[@aria-label='Go to next page']/parent::li/preceding-sibling::li)[last()]").text
print(no_of_pages)

for i in range(1, int(no_of_pages)+1):
    print(i)
    for j in range(1, 8):
        try:
            expand_icon_locator = By.XPATH, "//tbody/tr[" + str(j) + "]/td[1]/*[local-name()='svg']"
            artist_locator = By.XPATH, "//tbody/tr[" + str(j) + "]/td[2]//a"
            track_title_locator = By.XPATH, "//tbody/tr[" + str(j+1) + "]/td[2]/div[1]"
            expand_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(expand_icon_locator))
            expand_icon.click()
            track_title_text = driver.find_element(*track_title_locator).text
            start_index = track_title_text.index(":") + 2
            end_index = len(track_title_text)
            track_title = track_title_text[start_index:end_index].strip()
            artist = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(artist_locator))
            driver.execute_script("arguments[0].click();", artist)

            window_handles = driver.window_handles
            new_window_handle = window_handles[-1]
            driver.switch_to.window(new_window_handle)
            wait = WebDriverWait(driver, 10)
            shazam_track_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@itemprop='name']"))).text
            if track_title.__contains__(shazam_track_title):
                pass
            else:
                print(track_title, "shazim title trac:  " + shazam_track_title)

            # assert shazam_track_title.__contains__(track_title), f"Assertion failed: shazam_track_title '{shazam_track_title}' does not contain track_title '{track_title}'"
            driver.close()

            original_window_handle = window_handles[0]
            driver.switch_to.window(original_window_handle)
            expand_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(expand_icon_locator))
            expand_icon.click()
        except:
            print(track_title , shazam_track_title)
    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()
    except:
        driver.close()
        original_window_handle = window_handles[0]
        driver.switch_to.window(original_window_handle)
        expand_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(expand_icon_locator))
        expand_icon.click()
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()



time.sleep(5)
