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

# ad_title = driver.find_element(By.XPATH, "(//table//tr//a)[2]").text
# driver.find_elements(By.XPATH, "//table//tr//td[3]")
# ad_title_links = driver.find_elements(By.XPATH, "//table//tr//td[3]")


no_of_pages = driver.find_element(By.XPATH, "(//button[@aria-label='Go to next page']/parent::li/preceding-sibling::li)[last()]").text
print(no_of_pages)


for i in range(1, int(no_of_pages)+1):
    for i in range (1,8):
        ad_title_locator = By.XPATH, "//tbody/tr[" + str(i) + "]/td[3]/a"
        try:
            ad_title = driver.find_element(*ad_title_locator)
            ad_title_text = ad_title.text
            print(ad_title_text)
            driver.execute_script("arguments[0].click();", ad_title)

        except StaleElementReferenceException:
            print("Stale element reference. Retrying...")
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ad_title_locator))
            ad_title_text = element.text
            driver.execute_script("arguments[0].click();", element)
        try:
            window_handles = driver.window_handles
            new_window_handle = window_handles[-1]
            driver.switch_to.window(new_window_handle)

            driver.find_element(By.XPATH, "//a[@role='tab']//span[contains(text(),'Info')]").click()
            ad_name = driver.find_element(By.XPATH, "//td[@itemprop='name']").text
            print("Ad Name in New Window:", ad_name)

            assert ad_name.__contains__(ad_title_text), "Assertion failed ad_name: " +ad_name+ "does not contain Ad Title: "+ ad_title_text
        except:
            pass

        driver.close()

        original_window_handle = window_handles[0]
        driver.switch_to.window(original_window_handle)
    driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']").click()

time.sleep(5)
