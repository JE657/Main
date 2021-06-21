"""
PROGRAM AUTHOR: Jordan Evan
FIND THIS SCRIPT @ MY REPOSITORY: HTTPS://GITHUB.COM/OMNIJK

PROGRAM DESCRIPTION:
                    PYTHON WEB SCRAPER for www.mybenta.com
                    Return an .xlsl worksheet containing Pricing Details and Contact Information
                    for listings on different pages of MyBenta, which is an alternate form
                    of craigslist/ebay centered around the Philippines (according to the site).
                    
                    Currently Returns (In Order): 
                    Listing Name    
                    Listing Description 
                    Listing Price       [Price of Listing]
                    Listing Images      [Thumbnail Image placed first in column]
                    Contact Name        [Username of Listing Author]
                    Contact Number      [Cell of Listing Author]
                    
                    
                    NOTE:   Category-specific search only supports the "Buy & Sell" section of MyBenta 
                            as I do not have the time nor will to enter specific IDs for the other 
                            100+ sections of this website, however, searching individual pages by ID 
                            and/or a range-based ID search is still supported.
                    
"""

import requests  # requests module for grabbing an HTML page from an http response
from bs4 import (
    BeautifulSoup,
)  # BeautifulSoup module for parsing and extracting data from the HTML
import time  # Python Time module for time.sleep() function to slow down HTTP requests between webpages
import pandas as pd  # Pandas Data Analysis module converting python objects into file formats, such as excel worksheets
import sys  # Python sys module to terminate program after execution


class Scraper:
    """
    Scraper [summary]
    
    Class to encapsulate all web scraping functionality specifically for MyBenta.com
    
    """

    def __init__(self):
        """
        __init__ [summary]
        
        Initialize all required information for single or multi-page scraping 
        
        Variables: 
            base_url:   (str): contains the base url for which all scraping will take place from 
                        as the layout of all category-based pages goes as follows:
                        
                        https://mybenta.com/ + search?cat= + page_id 
                        
                        where '?cat=' in the url takes a 3 digit number corresponding to a catgetory on the site
                        
            page_ids:   (Dictionary (str): Dictionary (str:int)): contains a pre-made dictionary where the key 
                        represents the main category of the listings and the value contains
                        another dictionary which corresponds to {sub_category (str): page_id (int)}
                        where the the page_id is a 3-digit integer appended to the url to load a certain page
                        
                        
        Returns:
            None
        
        """
        self.base_url = "https://www.mybenta.com/search?cat="
        self.page_ids = {
            "Animals": {
                "All Animals": "303",
                "Birds": "322",
                "Cats": 323,
                "Dogs": 324,
                "Exotic": 325,
                "Fish & Reptiles": 326,
                "Insects": 595,
                "Livestock": 327,
                "Other Pets": 328,
                "Pet Accessories": 321,
            }
        }

    def scrape_page(self, _page_id, _keyword):

        # If by some chance _page_id, an undefined value for _page_id is passed.
        if not _page_id:
            _page_id = 303

        print("attempting to scrape page id {}".format(_page_id))
        page_number = 1

        try:
            response = requests.get(
                self.base_url + str(_page_id) + "&page=" + str(page_number)
            )
            soup = BeautifulSoup(response.content, "html.parser")

            # page_category = soup.select('span[id="filterCat"] > b').text

            if not soup.body:
                print("Id of {} invalid, skipping page".format(_id))
            else:
                titles = soup.select("h1.searchtitle > strong")
                descs = soup.select(
                    'p[class="adDescription uk-text-break uk-link-muted well"]'
                )
                sellers = soup.select(
                    'span[class="adSeller uk-text-small uk-text-nowrap uk-link-muted"] > b'
                )

                prices = soup.select('span[class="searchprice"]')

                for title, desc, price, sell in zip(titles, descs, prices, sellers):
                    if not sell.text in contact["Contact_Name"]:
                        res = requests.get("https://www.mybenta.com/" + sell.text)
                        soup = BeautifulSoup(res.content, "html.parser")

                        ob = soup.select_one('i[class="uk-icon-location-arrow"]')

                        for i in range(10):
                            ob = ob.previous_sibling
                    else:
                        print("Name {} already in contact information")

                    t = soup.select("h1.searchtitle")[0:3]
                    title_urls = []
                    for _t in t:
                        title_urls.append(_t.parent["href"])
                        print(_t.parent["href"])

                    n_res = requests.get(
                        complete_url
                        + "/classified/812505/residential-condo-apartment-for-rent"
                    )
                    print(n_res.status_code)
                    n_soup = BeautifulSoup(n_res.content, "html.parser")

                    images = []
                    images.append(
                        complete_url + n_soup.select_one('img[id="adImage"]')["src"]
                    )

                    im = n_soup.select("img")
                    for _im in im:
                        if _im["src"][0:4] == "/img":
                            images.append(complete_url + _im["src"])

                    contact["Listing"].append(title.text)
                    contact["Description"].append(desc.text)
                    contact["Price"].append(price.text)
                    contact["Images"].append(images)
                    contact["Contact_Name"].append(sell.text)
                    contact["Contact_Number"].append(ob.text)

                    time.sleep(3)

                if not soup.select_one('i[class="uk-icon uk-icon-angle-double-right"]'):
                    return
                else:
                    print(
                        soup.select_one(
                            'i[class="uk-icon uk-icon-angle-double-right"]'
                        ).parent["href"]
                    )
                    page_no += 1

                # time.sleep(3)

                df = pd.DataFrame(data=contact)
                # df.to_csv('{}_page{}_listings.csv'.format(_id, page_no), index=False, header=1)
                print("Saved {}_bentalistings.xlsx".format(_id))
                df.to_excel("{}_bentalistings.xlsx".format(_id))

                sys.exit(1)
        except:
            print(
                "An Error Occured with Scraping the Page {} at {}\n{}".format(
                    page_number, _page_id, complete_url
                )
            )

    def multi_scrape(self, a):
        return None

    def select_page(self, _page_id):
        return self.base_url + _page_id


complete_url = ""

for _id in self.page_ids:
    _id = 313

    contact = {
        "Listing": [],
        "Description": [],
        "Price": [],
        "Images": [],
        "Contact_Name": [],
        "Contact_Number": [],
    }

