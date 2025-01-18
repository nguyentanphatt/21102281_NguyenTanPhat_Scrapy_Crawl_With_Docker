import scrapy
import re
from database.csv_handler import CSVHandler
from database.txt_handler import TXTHandler
from database.sql_handler import SQLHandler
class BatdongsanSpider(scrapy.Spider):
    name = 'batdongsan'
    allowed_domains = ['homedy.com']
    start_urls = ['https://homedy.com/du-an-can-ho']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_handler = CSVHandler(file_name='batdongsan_data.csv')  
        self.txt_handler = TXTHandler(file_name='batdongsan_data.txt')
        self.sql_handler = SQLHandler(
            host='host.docker.internal',
            user='root',
            password='sapassword',
            database='scrapy_data'
        )

    def parse(self, response):
        for item in response.css('div.tab-content div.item'):
            data = self.extract_item_data(item)
            self.csv_handler.save_data(data) 
            self.txt_handler.save_data(data)
            self.sql_handler.save_data("batdongsan",data)
    def extract_item_data(self, item):
        item_data = {}

        # Tên 
        title_element = item.css('h2.name::text').get()
        item_data['title'] = (
            re.sub(r'\s+', ' ', title_element).strip() if title_element else 'N/A'
        )

        # Giá
        price_element = item.css('span.price::text').get()
        item_data['price'] = price_element if price_element else 'N/A'

        # Địa chỉ
        address_element = item.css('div.address::text').get()
        item_data['address'] = address_element.strip() if address_element else 'N/A'

        # Kích thước
        area_element = item.css('span.name-item::text').get()
        item_data['area'] = area_element.strip() if area_element else 'N/A'
        print(item_data)
        return item_data
