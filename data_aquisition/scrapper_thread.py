from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import RLock

def try_find_out_of_index(driver : webdriver.Firefox, rlock_printer : RLock) -> bool:
    """_summary_

    Args:
        driver (webdriver.Firefox): _description_
        rlock_printer (RLock): _description_

    Returns:
        bool: _description_

    Description:
        Try to see if the driver is in an immoweb search page by using the deplacement button of the search pages.
        If it does not found a button, return true.
        Else return False
    """
    try:
        if len(driver.find_elements(By.CLASS_NAME, "pagination__item")) == 0:
            return True
        else:
            return False
    except:
        with rlock_printer:
            print("ERROR : Unable to check the page !")
        return False

def change_page(driver : webdriver.Firefox, page : int, province : str, rlock_printer : RLock) -> bool:
    """_summary_

    Args:
        driver (webdriver.Firefox): _description_
        page (int): _description_
        province (str): _description_
        rlock_printer (RLock): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
        
    Description:
        Change the page of the driver to go to a immoweb search page.
        If the new page is not a immoweb search page, raise an error and return False.
        else, return True after the change
    """
    try:
        driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/for-sale/{province}/province?countries=BE&page={page}&orderBy=relevance")
        #Test if the page the driver is currently in is a immoweb search page. Raise a exception when out of the search pages
        if try_find_out_of_index(driver, rlock_printer):
            raise Exception(f"Last page attain : {province} !")
    except Exception as e:
        with rlock_printer:
            print(e)
        return False
    return True
    
def try_cookie(driver : webdriver.Firefox):
    """_summary_
    Args:
        driver (webdriver.Firefox): _description_
        
    Description:
        Search on the page if there is a coockie by using the Xpath of the button to remove it.
    """
    try:
        coockie_button = driver.find_element(By.XPATH, '//*[@id="uc-btn-accept-banner"]')
        coockie_button.click()
    except:
        pass
    
def get_property_urls(driver : webdriver.Firefox, urls : list):
    """_summary_
    Args:
        driver (webdriver.Firefox): _description_
        urls (list): _description_
        
    Description:
        Get all the urls of the properties on the search page of immoweb by using their href.
        Add the urls to the urls list if they are not already in.
    """
    articles_found = driver.find_elements(By.CLASS_NAME, "card__title-link")
    for article in articles_found:
        url = article.get_attribute("href")
        if url not in urls:
            urls.append(url)
            
def print_urls(urls : list, lock : RLock):
    """_summary_

    Args:
        urls (list): _description_
        lock (RLock): _description_
        
    Description :
        Check if the url is in the file link.csv and add it to it if it's not.
    """
    found = False
    with lock:
        with open('.\links.csv', 'r') as file:
            lines = file.readlines()
        with open('.\links.csv', 'a') as file:
            for url in urls:
                if url not in lines:
                    file.write(url + "\n")

def link_scrapper(province : str, rlock_csv : RLock, rlock_printer : RLock, excutable_path):
    """_summary_
    Args:
        province (str): _description_
        rlock_csv (RLock): _description_
        rlock_printer (RLock): _description_
        
    Description :
        This function is to be called by the Thread to get the Urls of Immoweb properties.
        It loop trought the buy_types and used the belgium provinces name to move trought the url bar.
    """
    continue_loop : bool = True
    page = 1
    urls = []

    #Create a new driver for each buy_type to prevent memory overload
    driver = webdriver.Firefox(executable_path=excutable_path)
    driver.implicitly_wait(0.5)
    while continue_loop:
        #change the page, if you're not in a search result page of immoweb, return false and get out of the loop
        continue_loop = change_page(driver, page, province, rlock_printer)
        if continue_loop:
            #Test if there is a cookie request on the page. If there is a cookies request, click on it to remove it
            try_cookie(driver)
            #Get all the urls in the research page and append them to the urls list
            get_property_urls(driver, urls)
            with rlock_printer:
                print(f"link scrapper {province} : page {page}")
            page += 1
    driver.close()
    print_urls(urls, rlock_csv)
    with rlock_printer:
        print(f"{province} has printed on the csv file !")