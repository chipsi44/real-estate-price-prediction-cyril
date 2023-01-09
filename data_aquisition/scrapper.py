from scrapper_thread import link_scrapper
from threading import Thread
from threading import RLock
from webdriver_manager.firefox import GeckoDriverManager
    
def get_urls_from_scrapper():
    """_summary_
    
    Description:
        Function to be called to create a thread for each provinces of Belgium.
        Each thread will collect the urls of the search pages on immoweb by using the provinces filter.
        When the threads have finished collecting all the urls, they will write them in a links.csv file.
    """
    link_scrappers = list()
    rlock_csv = RLock()
    rlock_printer = RLock()
    provinces = ["antwerp",
                 "limburg",
                 "east-flanders",
                 "flemish-brabant",
                 "west-flanders",
                 "walloon-brabant",
                 "hainaut",
                 "liege",
                 "luxembourg",
                 "namur",
                 "brussels"]
    
    executable_path = GeckoDriverManager().install()
    create_empty_file = open(".\links.csv", "w")
    create_empty_file.close()
    
    for province in provinces:
        thread = Thread(target= link_scrapper, args=(province, rlock_csv, rlock_printer, executable_path,))
        link_scrappers.append(thread)
    for thread in link_scrappers:
        thread.start()
    for thread in link_scrappers:
        thread.join()