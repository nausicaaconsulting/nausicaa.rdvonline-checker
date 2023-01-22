import logging
import time
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

import settings


logger = logging.getLogger(__name__)


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-data-dir=.config/google-chrome')

    if settings.WEB_CHROME_HEADLESS:
        chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)  # Always wait at least 3 seconds when trying to find an element
    return driver


def check_available_date(postal_code: str, distance: int, nb_persons: int):
    position = get_postal_code_info(postal_code)
    mairies = get_mairies(position, distance)

    with create_driver() as driver:
        if mairies:
            for mairie in mairies:
                text = 'Aucune reservation possible'
                try:
                    if next((reason for reason in mairie['reasons'] if (reason['name'] == 'Dépôt passeport')), None):
                        text = query_mairie(mairie, driver, nb_persons)
                        text = text.replace('\n', ' - ')
                except:
                    pass
                print(f"{mairie['name']} => {text}")


def query_mairie(mairie: dict, driver, nb_persons: int):
    ## FIRST SCREEN ##
    service = "Carte%20Nationale%20d%27Identité%20%28CNI%29%20et%20Passeport"
    url = f"https://rendezvousonline.fr/alias/{mairie['alias']}/prendre-rendez-vous?service={service}"
    #print(url)
    try:
        driver.get(url)
    except WebDriverException:
        logger.error('Could not reach rendezvousonline ', exc_info=True)
        raise
    try:
        WebDriverWait(driver, 1).until(ec.presence_of_element_located((By.ID, "reasons-2")))
    except TimeoutException:
        #logger.error('Cannot find depot passeport dropdown', exc_info=True)
        return None

    reason2 = driver.find_element_by_id('reasons-2')
    reason2.click()
    reason2input = reason2.find_elements_by_xpath(".//input")[0]
    reason2input.send_keys(f"{nb_persons}")
    reason2input.send_keys(Keys.RETURN);

    continuer = driver.find_element(By.TAG_NAME, 'form').find_elements_by_xpath('./div/span/button')[0]
    continuer.click()

    ## DISPONIBILITES ##
    try:
        WebDriverWait(driver, 1).until(ec.presence_of_element_located((By.CLASS_NAME, "card-body")))
    except TimeoutException:
        #logger.error('Cannot find card-body', exc_info=True)
        return None
    card_body = driver.find_element(By.CLASS_NAME, "card-body")
    time.sleep(1)
    card_text = card_body.text
    return card_text


def get_mairies(position: dict, distance: int):
    place = position['place_name']
    longitude = position['center'][0]
    latitude = position['center'][1]
    url = f"https://pro.rendezvousonline.fr/api-web/search-structures/Carte%20Nationale%20d'Identit%C3%A9%20(CNI)%20et%20Passeport/{place}/{latitude}/{longitude}?reasons_number=%7B%7D&sort=asap&radius={distance}&page=1&per_page=10"
    req = requests.get(url)
    req.raise_for_status()
    mairies = req.json()
    return mairies.get('results')


def get_postal_code_info(postal_code: str):
    access_token = "pk.eyJ1IjoidGxtY29tIiwiYSI6ImNrY293cjYweDAwcWQzMG1ncjRhY2VocHoifQ.laGtBR5tv_CZnw4tIHnY7w"
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{postal_code}.json?autocomplete=true&country=fr,gp,mq,gf,re,pm,yt,nc,pf,mf,tf&types=country,region,postcode,district,place,locality,neighborhood,address&access_token={access_token}"
    req = requests.get(url)
    req.raise_for_status()
    positions = req.json()
    if positions.get('features'):
        return positions.get('features')[0]
    return None

