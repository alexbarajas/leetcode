from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "AlexBarajas1996@gmail.com"
ACCOUNT_PASSWORD = "rovrUc-juhqi5-xuhqin"
PHONE = "8482232064"

chrome_driver_path = "/Users/alexbarajas/Development/chromedriver"
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

current_job_Id = "3904262401"
keywords = "software engineer".replace(" ", "%20")
location = "new york city metropolitan area".title().replace(" ", "%20")
days = 0
days_formatted = "&f_TPR=r" + str(days * 86400)
seconds = 10800  # 86400 is for a day

number_of_jobs = [0]


def sign_in():
    driver.get(
        # f"https://www.linkedin.com/jobs/search/?currentJobId=3904262401&distance=25.0&geoId=90000070&keywords=software%20engineer%20NOT%20%22senior%22%20NOT%20%22staff%22%20NOT%20%22principal%22%20NOT%20%22lead%22&origin=HISTORY"
        # f"https://www.linkedin.com/jobs/search/?currentJobId={current_job_Id}&f_AL=true{days if days else ''}&f_TPR=r86400&geoId=90000070&keywords={keywords}&location={location}&refresh=true"
        f"https://www.linkedin.com/jobs/search/?currentJobId={current_job_Id}&f_AL=true{days if days else ''}&f_TPR=r{seconds}&geoId=90000070&keywords={keywords}%20NOT%20%22senior%22%20NOT%20%22staff%22%20NOT%20%22principal%22%20NOT%20%22lead%22&location={location}&refresh=true"
    )
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
    sign_in_button.click()
    email_field = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
    email_field.send_keys(ACCOUNT_EMAIL)
    password_field = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
    time.sleep(15)  # needs to be at 15 so you can solve captcha


def submit_application():
    following = driver.find_element(By.CSS_SELECTOR, 'label[for="follow-company-checkbox"]')
    following.click()
    submit = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    number_of_jobs[0] += 1
    print(submit.text, "submitted an application")
    submit.click()
    time.sleep(3)
    dismiss(False)


def dismiss(in_middle_of_application=True):
    close = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
    close.click()
    time.sleep(1)
    if in_middle_of_application:
        discard()
    return


def discard():
    discard_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
    discard_button.click()


def apply():
    easy_apply = driver.find_element(By.CLASS_NAME, "jobs-s-apply")
    if "Applied" in easy_apply.text or "Easy Apply" not in easy_apply.text:
        return
    # print(easy_apply.text, "easy_apply")
    easy_apply.click()
    time.sleep(3)

    # fill in the application fields
    phone_field = driver.find_element(By.CSS_SELECTOR, '.artdeco-text-input--input')
    if phone_field.get_attribute("value") == "":
        phone_field.send_keys(PHONE)
    check_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary span")
    # print(check_button.text, "check_button")

    if check_button.text == "Next":
        check_button.click()
        time.sleep(2)
        resume_button = driver.find_element(By.CSS_SELECTOR,
                                            ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
        resume_button_text = resume_button.find_element(By.CSS_SELECTOR, '.artdeco-button__text')
        # print(resume_button_text.text, "resume_button_text")
        original_style = resume_button.get_attribute("style")
        new_style = "border: 2px solid red; background-color: yellow; " + original_style
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", resume_button, new_style)
        if resume_button_text.text == "Review":
            resume_button.click()
            submit_application()
        elif resume_button_text.text == "Next":
            dismiss()
        time.sleep(1)
    elif "Submit" in check_button.text:
        submit_application()


def start_applying():
    all_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
    n = len(all_listings)
    for i in range(n):
        # print(f"\nApplying to job {i + 1} out of {n}.\n")
        time.sleep(1)
        all_listings[i].click()
        time.sleep(2)  # 1 was giving problems, so keep at 2
        apply()


def number_of_pages():
    pages_bar = driver.find_element(By.CLASS_NAME, "artdeco-pagination__pages.artdeco-pagination__pages--number")
    pages = pages_bar.find_elements(By.TAG_NAME, "li")
    total_pages = len(pages) - 1
    for i in range(1, total_pages + 1):
        print(f"page {i}")
        page = pages_bar.find_element(By.XPATH, f"./li[{i}]")
        page_button = page.find_element(By.TAG_NAME, "button")
        page_button.click()
        time.sleep(3)
        start_applying()


sign_in()
number_of_pages()

print(f"Yhu applied to {number_of_jobs[0]} jobs just now.")

# input("Press Enter to close the WebDriver...")

driver.quit()
