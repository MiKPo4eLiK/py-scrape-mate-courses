import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from typing import List

BASE_URL = "https://mate.academy/en/courses"


def get_all_courses() -> List[dict]:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BASE_URL)

    time.sleep(5)

    course_blocks = driver.find_elements(By.CSS_SELECTOR, "div.CareerPath_careerPathInfoContainer__FYKO5")

    courses = []
    for block in course_blocks:
        name = block.find_element(By.CSS_SELECTOR, "h2.typography_platformH2__0YzKL").text
        short_description = block.find_element(By.CSS_SELECTOR, "p.CareerPath_description__gNUVa").text
        duration = block.find_element(By.CSS_SELECTOR,
                                      "span.CareerPath_duration__someClass").text

        courses.append({
            "name": name,
            "short_description": short_description,
            "duration": duration,
        })

    driver.quit()
    return courses


if __name__ == "__main__":
    all_courses = get_all_courses()
    for course in all_courses:
        print(course)
