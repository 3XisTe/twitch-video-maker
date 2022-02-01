from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

requestedLinks = []
howMany = 1
period = '7d'

def setValues(amount, days):
    global howMany
    howMany = amount
    global period
    period = days

def enterWeb():
    driver = webdriver.Safari()
    link = 'https://www.twitch.tv/directory?sort=VIEWER_COUNT'
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-a-target="consent-banner-accept"]'))).click()
    searchCat(driver)

def searchCat(driver):
    peopleWatchTitles = []
    peopleWatchLinks = []
    global period

    for i in range(10):
        xpath = '//a[@data-a-target="card-' + str(i) + '"]'
        peopleWatchTitles.append(driver.find_element_by_xpath(xpath).text)
        peopleWatchLinks.append(driver.find_element_by_xpath(xpath).get_attribute("href"))

    lastXDays = period
    searchClips(driver, peopleWatchLinks, lastXDays)

def searchClips(driver, linkedSites, lastXDays):
    global howMany
    for i in range(len(linkedSites)):
        link = linkedSites[i] + '/clips?range=' + lastXDays
        driver.get(link)
        try:
            for j in range(howMany):
                xpath = '//*[@data-a-target="clips-card-' + str(j) + '"]'
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
                try:
                    flag = False
                    while(flag == False):
                        user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
                        title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text
                        videoLink = driver.find_element_by_tag_name('video').get_attribute('src')
                        if 'clips' in videoLink and len(user) > 0 and len(title) > 0:
                            flag = True
                        else:
                            user = ''
                            title = ''
                            videoLink = ''
                            flag = False
                    requestedLinks.append(user + "#|#" + title + "#|#" + driver.current_url + "#|#" + videoLink)
                except:
                    print("Something went wrong, try again or if you don't want to proceed with xx results type no")
                    if input() == 'no':
                        requestedLinks.clear()
                    driver.quit()
                    break
                driver.back()
        except:
            driver.quit()

    driver.quit()

def saveLinks(linkPath):
    f = open(linkPath + "/Links/requestedLinks.txt", "w")
    for i in range(len(requestedLinks)):
        f.write(requestedLinks[i] + '\n')
    f.close()