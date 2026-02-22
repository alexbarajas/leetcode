import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

ACCOUNT_EMAIL = "AlexBarajas1996@gmail.com"
ACCOUNT_PASSWORD = "finna hit ah licc"

chrome_driver_path = "/Users/alexbarajas/Development/chromedriver"
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)

number_of_jobs = [0]


def sign_in():
    driver.get(
        f"https://online.roberthalf.com/s/login?app=0sp3w000001UJH5&c=US&d=en_US&language=en_US&redirect=false"
    )
    time.sleep(5)  # 5 so you can get rid of the popups
    email_field = driver.find_element(By.XPATH, "/html/body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-rh-theme-layout/section[2]/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout/div/community_layout-section/div[3]/community_layout-column/div/c-ux-customer-signin/div/div[1]/div/div[3]/rhcl-text-field")
    email_field.click()
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = driver.find_element(By.XPATH, "/html/body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-rh-theme-layout/section[2]/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout/div/community_layout-section/div[3]/community_layout-column/div/c-ux-customer-signin/div/div[1]/div/div[4]/div/rhcl-password-field")
    password_field.click()
    password_field.send_keys(ACCOUNT_PASSWORD)
    sign_in_button = driver.find_element(By.XPATH, "/html/body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-rh-theme-layout/section[2]/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout/div/community_layout-section/div[3]/community_layout-column/div/c-ux-customer-signin/div/div[1]/div/div[6]/rhcl-button")
    sign_in_button.click()
    time.sleep(30)  # 30 so you can put in the code from the email you will receive
    search_jobs()


def search_jobs():
    search_jobs_button = driver.find_element(By.XPATH, "/html/body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-rh-theme-layout-curve/div/header/slot/c-u-x-client-task-based-header/div/div/rhcl-block-navigation/rhcl-navigation-item[4]")
    search_jobs_button.click()
    time.sleep(5)  # this needs to be 5 so that the page loads
    number_of_pages = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div/rhcl-pagination")
    total_jobs = int(number_of_pages.text.split()[-2])
    jobs_per_page = 25
    total_pages = math.ceil(total_jobs / jobs_per_page)
    url = "https://www.roberthalf.com/us/en/jobs/toms-river/all"
    page_number = 1

    while total_jobs:
        if total_jobs <= 0:
            print(f"yhu just applied to {number_of_jobs} niqqa")
            break
        time.sleep(3)  # so that the APPLIED thing pops up for the jobs
        jobs_on_current_page = min(jobs_per_page, total_jobs)
        jobs = driver.find_elements(By.CSS_SELECTOR, ".rh-pt-6x")
        for i in range(jobs_on_current_page):
            # print("page:", page_number, "job:", i)
            if i == 2 or i >= jobs_on_current_page:
                continue
            try:
                jobs[i].click()
            except selenium.common.StaleElementReferenceException or selenium.common.ElementClickInterceptedException:
                continue
            for _ in range(2):
                jobs[i].send_keys(Keys.PAGE_DOWN)
            apply(i)
        total_jobs -= jobs_on_current_page
        page_number += 1
        if page_number > total_pages:
            break
        driver.get(url + f"?pagenumber={page_number}")
        time.sleep(5)


def apply(i):
    check_if_applied = driver.find_elements(By.CSS_SELECTOR, ".rh-pt-6x")
    if check_if_applied[i].text.split()[0] == "APPLIED":
        return
    quick_apply_with_shadow_dom = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/rhcl-job-card")
    shadow_root_script = "return arguments[0].shadowRoot"
    shadow_root = driver.execute_script(shadow_root_script, quick_apply_with_shadow_dom)
    quick_apply = shadow_root.find_element(By.CSS_SELECTOR, "rhcl-button[slot='button']")
    try:
        quick_apply.click()
    except selenium.common.ElementClickInterceptedException or selenium.common.NoSuchElementException:
        quick_apply_with_shadow_dom.send_keys(Keys.PAGE_UP)
        try:
            quick_apply.click()
        except selenium.common.ElementClickInterceptedException:
            return
    print("1 mo niqqa")
    number_of_jobs[0] += 1
    time.sleep(3)


sign_in()
driver.quit()
