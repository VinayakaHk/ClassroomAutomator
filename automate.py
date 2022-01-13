import traceback

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import sys


class AnyEC:
    def __init__(self, *args):
        self.ecs = args

    def __call__(self, driver):
        for f in self.ecs:
            try:
                res = f(driver)
                if res:
                    return res

            except:
                pass


def print_time():
    return str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)


def wait_for_conf_click():
    print('wait_for_conf_click. Time: ' + str(print_time()))
    while True:
        try:
            WebDriverWait(
                driver,60).until(
                ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div")))
            continue
        except (NoSuchElementException, TimeoutException):
            print("I can listen. Time: " + str(print_time()))
            break


def wait_for_listen_button():
    print('wait_for_listen_button. Time: ' + str(print_time()))
    while True:
        try:
            WebDriverWait(
                driver,60).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "button.jumbo--Z12Rgj4:nth-child(2)")))
            print("Located Listen button. time: " + str(print_time()))
        except (NoSuchElementException,TimeoutException):
            continue
        try:
            driver.find_element_by_css_selector("button.jumbo--Z12Rgj4:nth-child(2)").click()
            print("Clicked on Listen button. time: " + str(print_time()))
            break
        except (NoSuchElementException,TimeoutException):
            continue


def wait_for_homepage():
    print('wait_for_homepage. Time: ' + str(print_time()))
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/h6/img")
            print("Homepage located, time : " + str(print_time()))
            break
        except NoSuchElementException:
            continue

def text_public():
    print('Text Public. Time: ' + str(print_time()))
    public_chat = driver.find_element_by_xpath('//*[@id="message-input"]')
    public_chat.send_keys("yes mam")
    public_chat.send_keys(Keys.ENTER)


def wait_class_end():
    print('wait_class_end. Time: ' + str(print_time()))
    while True:
        try:
 
            WebDriverWait(
                driver, 60).until(
                 ec.presence_of_element_located((
                     By.XPATH, "/html/body/div/div/div/div/div/button")))
            print("Class ended " + str(print_time()))
            break
        except TimeoutException:
            continue


def join_class():
    print('Searching for classes to Join.join_class() Time: ' + str(print_time()))
    while True:
        for i in range(1, 10):
            try:
                driver.find_element_by_xpath("//div[" + str(i) + "]/div/div[2]/button[2]/span").click()

            except NoSuchElementException:
                continue
        try:
            class_started = WebDriverWait(driver, 1).until(ec.url_matches("https://alive.university/app/stream"))
            if class_started:
                print("Class started , time : ", str(print_time()))
                break
        except (NoSuchFrameException, TimeoutException):
            continue


def hide_chat():
    print('hide_chat. Time: ' + str(print_time()))
    while True:
        try:
            WebDriverWait(
                driver, 60).until(
                    ec.presence_of_element_located((
                        By.XPATH, "/html/body/div[1]/main/section/div[4]/header/div/div[1]/div[1]/button/span[1]/i")))
        except TimeoutException:
            continue
    while True:
        try:
            driver.find_element_by_xpath(
                "/html/body/div[1]/main/section/div[4]/header/div/div[1]/div[1]/button/span[1]/i").click()
            print("Hide chat button located and clicked, time : " + str(print_time()))
            break
        except NoSuchElementException:
            continue



def login_system():
    print("Logging in login_system(). Time: " + str(print_time()))
    driver.find_element_by_name("user_email").send_keys("username")
    driver.find_element_by_name("user_password").send_keys("password")
    submit_btn = driver.find_element_by_css_selector(".MuiButtonBase-root")
    submit_btn.click()
    print("Logged in. Time: " + str(print_time()))


def main():
    try:
        init()

    except KeyboardInterrupt:
        print("Error: Program execution interrupted.", file=sys.stderr)

    except WebDriverException as err:
        print("Error: Webdriver error: " + str(err), file=sys.stderr)

    except Exception as err:
        print("Traceback: " + ''.join(traceback.format_tb(err.__traceback__)), file=sys.stderr)
        print("Error: " + str(err), file=sys.stderr)

    finally:
        print("Terminating program.")
        driver.close()
        driver.quit()


def init():
    print("Program started at : " + str(print_time()))
    #  Open Firefox and alive.university
    global driver
    driver = webdriver.Firefox(executable_path="C://MLCourse//MLCourse//geckodriver.exe")
    driver.maximize_window()
    driver.get("https://alive.university")
    print("Site opened.")
    login_system()
    
    wait_for_homepage()

    while True:
        join_class()
        print("iframe  retrieval : " + str(print_time()))
        driver.switch_to.frame("embedd-bbb")
        print("Switched to frame, clicking on listen , time : " + str(print_time()))
        
        wait_for_listen_button()
        print("waits for the class to end by using wait_class_end(). Time:" + str(print_time()))
        wait_class_end()
        print("Class has ended, Time: " + str(print_time()))
        driver.switch_to.parent_frame()
        driver.get("https://alive.university/app/main")
        print('Phew! Class ended. Time: ' + str(print_time()))
        print ('\n__________________________________________________________\n')


if __name__ == "__main__":
    main()
