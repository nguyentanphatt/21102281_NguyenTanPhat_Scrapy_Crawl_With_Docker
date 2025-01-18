## How to use
The project has been set up to crawl data from two sites https://thoitiet.vn/ and https://homedy.com/du-an-can-ho

### Set up
Create a mysql with username: root, password: sapassword, database: scrapy_data
Data from https://thoitiet.vn/ will be inserted into a table named dubaothoitiet
Data from https://homedy.com/du-an-can-ho will be inserted into a table named batdongsan

### Start
docker-compose build
docker-compose up --build
