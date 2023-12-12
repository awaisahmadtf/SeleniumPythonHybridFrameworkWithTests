import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException


def click_element(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    element.click()


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://dev-ringoadmin.trailfive.com/auth/login")
driver.get("https://ringoadmin.trailfive.com/")

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@id='mui-1']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@id='mui-2']").send_keys("admin")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Sync History']").click()

no_of_pages = driver.find_element(By.XPATH,
                                  "(//button[@aria-label='Go to next page']/parent::li/preceding-sibling::li)[last()]").text
print(no_of_pages)

for i in range(1, int(no_of_pages) + 1):
    print(i)
    for j in range(1, 8):
        try:
            expand_icon_locator = By.XPATH, f"//tbody/tr[{j}]/td[1]/*[local-name()='svg']"
            artist_locator = By.XPATH, f"//tbody/tr[{j}]/td[2]//a"
            track_title_locator = By.XPATH, f"//tbody/tr[{j + 1}]/td[2]/div[1]"

            click_element(driver, expand_icon_locator)

            track_title_text = driver.find_element(*track_title_locator).text
            track_title = track_title_text.split(': ', 1)[-1].strip()

            click_element(driver, artist_locator)

            window_handles = driver.window_handles
            new_window_handle = window_handles[-1]
            driver.switch_to.window(new_window_handle)

            shazam_track_title = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@itemprop='name']"))
            ).text

            if track_title in shazam_track_title:
                pass
            else:
                print(track_title, "Shazam title track:  " + shazam_track_title)

            driver.close()
            original_window_handle = window_handles[0]
            driver.switch_to.window(original_window_handle)
            click_element(driver, expand_icon_locator)

        except Exception as e:
            print(f"Error on Page {i}, Record {j}: {str(e)}")

    try:
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()
    except NoSuchElementException:
        click_element(driver, expand_icon_locator)
        driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()

time.sleep(5)
