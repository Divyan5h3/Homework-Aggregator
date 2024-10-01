from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

# # Only for testing purposes
# f = open("test_details.txt", "r")
# test_email = f.readline()
# test_passwrd = f.readline()


def scraper_login(email: str, passwrd: str, url: str) -> None:
    driver = create_webdriver()
    driver.get(url)

    # Entering email
    email_element_name = 'loginfmt'
    ignored_exceptions = (NoSuchElementException,
                          StaleElementReferenceException)
    timeout = 5
    email_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        expected_conditions.presence_of_element_located((By.NAME, email_element_name)))
    # login_input = driver.find_element(
    #     By.NAME, "loginfmt")
    email_element.send_keys(email, Keys.ENTER)
    time.sleep(1)
    # Entering password

    # passwrd_element_name = "passwd"
    # passwrd_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
    #     expected_conditions.presence_of_element_located((By.NAME, passwrd_element_name)))
    # passwrd_element.send_keys(passwrd, Keys.ENTER)
    password_input = driver.find_element(By.NAME, "passwd")
    password_input.send_keys(passwrd, Keys.ENTER)

    return driver


# Sets webdriver options and returns a webdriver object
def create_webdriver():
    # Setting chrome options so that browser doesn't close after function call ends

    chrome_options = Options()
    chrome_options.add_argument("headless")
    # chrome_options.add_experimental_option("detach", True)

    # Opening chrome browser
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def scrape_canvas(email: str, passwrd: str) -> dict:
    canvas_url = "https://canvas.illinois.edu/"

    # # Only for testing
    # email = test_email
    # passwrd = test_passwrd

    driver = scraper_login(email, passwrd, canvas_url)
    time.sleep(3)

    # Scraping Dashboard for assignment data
    dashboard_html = driver.page_source
    soup = BeautifulSoup(dashboard_html, 'html.parser')
    # planner_divs = soup.find_all("div", "PlannerItem-styles__details")

    # assignment_list = []
    # for div in assignment_divs:
    #     spans = div.find_all("span", recursive=True)
    #     for span in spans:
    #         if span.has_attr("class"):
    #             print(span["class"][0])
    #         assignment = {}
    #         if span.has_attr("class") and span["class"][0] == "enRcg_bGBk":
    #             print(span.text)
    #             assignment["course"] = span.text
    #         if span.has_attr("class") and span["class"][0] == "ergWt_bGBk":
    #             print(span.text)
    #             assignment["details"] = span.text
    #         if len(assignment) != 0:
    #             assignment_list.append(assignment)
    # print(assignment_list)

    # Trying another way of scraping
    planner_divs = soup.find_all("div", "Day-styles__root planner-day")
    asgmt_list = []
    curr_year = datetime.now().year
    for planner_div in planner_divs:
        # Extracting date
        date_div = planner_div.find("div", "Day-styles__secondary")
        date_txt = date_div.text
        date_txt = date_txt[date_txt.find(" ") + 1:] + f" {curr_year}"
        date_obj = datetime.strptime(date_txt, "%B %d %Y")
        date_formated_str = date_obj.strftime("%Y-%m-%d")

        # Extracting assignment details
        group_divs = planner_div.find_all("div", "Grouping-styles__root")
        for group_div in group_divs:

            # Finding class name
            class_div = planner_div.find("span", "Grouping-styles__title")
            class_name = class_div.text

            # Finding assignment name and link
            asgmt_divs = group_div.find_all(
                "div", "PlannerItem-styles__details")
            for asgmt_div in asgmt_divs:
                asgmt_link_div = asgmt_div.find("a")
                asgmt_link = ""
                if asgmt_link_div.has_attr("href"):
                    asgmt_link = canvas_url + asgmt_link_div["href"]
                asgmt_name_span = asgmt_link_div.find(
                    "span", {"aria-hidden": "true"})
                asgmt_name = asgmt_name_span.text
                asgmt_dict = {
                    "date": date_formated_str,
                    "class": class_name,
                    "asgmt_name": asgmt_name,
                    "asgmt_link": asgmt_link
                }
                asgmt_list.append(asgmt_dict)

    return asgmt_list
