from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


def wait_for_conf_click():
    while True:
        try:
            print("I cant listen")
            driver.find_element_by_xpath("/html/body/div[2]/div/div")
            driver.implicitly_wait(60)
            continue
        except NoSuchElementException:
            print("Ok, now , i can listen")
            break


def wait_for_listen_button():
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div")
            break
        except NoSuchElementException:
            continue


def wait_for_homepage():
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/h6/img")
            break
        except NoSuchElementException:
            continue


def text_public():
    public_chat = driver.find_element_by_xpath('//*[@id="message-input"]')
    public_chat.send_keys("yes mam")
    public_chat.send_keys(Keys.ENTER)


def wait_class_end():

    while True:
        try:
            WebDriverWait(
                driver, 60).until(
                ec.presence_of_element_located((
                    By.XPATH, "/html/body/div/div/div/div/div/button")))
            break
        except TimeoutException:
            continue


def join_class():
    while True:
        for i in range(1, 10):
            try:
                driver.find_element_by_xpath("//div[" + str(i) + "]/div/div[2]/button[2]/span").click()

            except NoSuchElementException:
                continue
        try:
            class_started = WebDriverWait(driver, 1).until(ec.url_matches("https://alive.university/app/stream"))
            if class_started:
                break
        except (NoSuchFrameException, TimeoutException):
            continue


def login_system():
    driver.find_element_by_name("user_email").send_keys("USN")
    driver.find_element_by_name("user_password").send_keys("pass")
    driver.find_element_by_xpath("//div[@id='root']/div/div/div[2]/div/div/div/div/form/div[3]/button/span").click()
    # submit button because there is no input tag with unique ID


driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.maximize_window()
driver.get("https://alive.university/")
login_system()
wait_for_homepage()

while True:
    join_class()
    # print("Waiting 20 seconds for it to load up")
    # instead of waiting for x amount of time, pick an element and  the class to load
    print("iframe  retrieval")
    driver.switch_to.frame("embedd-bbb")
    print("clicking on listen")
    wait_for_listen_button()
    driver.find_element_by_xpath("//button[2]/span/i").click()
    wait_for_conf_click()
    # to type anything in the public chat and send it
    # text_public()
    print("click on hide chat button")
    driver.find_element_by_xpath("/html/body/div/main/section/div[1]/header/div/div[1]/div[1]/button").click()
    print("waits for the class to end by using wait_class_end()")
    wait_class_end()
    print(" after class ends")
    driver.switch_to.parent_frame()
    print("clicking on home after class ends.")
    driver.find_element_by_xpath("//div[@id='root']/div/div/header/div/div[2]/button/span").click()
    print('Phew! Class ended')

# driver.close()
