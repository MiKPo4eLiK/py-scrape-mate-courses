from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dataclasses import dataclass
from typing import List
import time

BASE_URL = "https://mate.academy/"

@dataclass
class Course:
    name: str
    short_description: str
    duration: str

def get_all_courses() -> List[Course]:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)
    time.sleep(5)

    courses = []
    course_blocks = driver.find_elements(By.CSS_SELECTOR, "div.card")

    for block in course_blocks:
        name = block.find_element(By.CSS_SELECTOR, "h3").text
        desc = block.find_element(By.CSS_SELECTOR, "p").text
        dur = block.find_element(By.CSS_SELECTOR, "span").text
        courses.append(Course(name=name, short_description=desc, duration=dur))

    driver.quit()
    return courses


if __name__ == "__main__":
    all_courses = get_all_courses()
    for c in all_courses:
        print(c)
