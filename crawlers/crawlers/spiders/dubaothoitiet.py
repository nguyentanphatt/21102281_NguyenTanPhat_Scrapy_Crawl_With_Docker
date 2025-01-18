import scrapy
from database.csv_handler import CSVHandler
from database.txt_handler import TXTHandler
from database.sql_handler import SQLHandler
class DubaothoitietSpider(scrapy.Spider):
    name = "dubaothoitiet"
    allowed_domains = ["thoitiet.vn"]
    start_urls = ["https://thoitiet.vn"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_handler = CSVHandler(file_name='dubaothoitiet_data.csv')  
        self.txt_handler = TXTHandler(file_name='dubaothoitiet_data.txt')
        self.sql_handler = SQLHandler(
            host='host.docker.internal',
            user='root',
            password='sapassword',
            database='scrapy_data'
        )
    def parse(self, response):
        
        cities = response.css('div.col-md-3')

        for city in cities:
            data = self.extract_item_data(city)
            if data:
                print(data)
                self.csv_handler.save_data(data)
                self.txt_handler.save_data(data)
                self.sql_handler.save_data("dubaothoitiet",data)


    def extract_item_data(self, city):
        
        # Tên thành phố
        city_name = city.css('h3.card-city-title::text').get()
        if not city_name:
            return None
        
        # Mật độ
        precipitation_div = city.css('div.precipitation')
        rainfall = precipitation_div.xpath('./i/following-sibling::text()').get(default='').strip()
        
        # Dự báo thời tiết 
        sky_description = city.css('p.mb-0::text').get(default='').strip()
        
        # Nhiệt độ
        current_temp = city.css('div.card-city-footer p[title="Hiện tại"]::text').get(default='').strip()
        
        # Cảm giác như
        feels_like_temp = city.css('div.card-city-footer p[title="Cảm giác như"]::text').get(default='').strip()

        return {
            'city_name': city_name.strip(),
            'rainfall': rainfall,
            'sky_description': sky_description,
            'current_temp': current_temp,
            'feels_like_temp': feels_like_temp
        }