import mysql.connector

class SQLHandler:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        self.cursor = self.connection.cursor()

    def ensure_table(self, table_name):
        """
        Ensure that the required table exists. Creates the table if it does not exist.
        
        Args:
            table_name (str): The name of the table to check/create.
        """
        if table_name == "batdongsan":
            query = """
            CREATE TABLE IF NOT EXISTS batdongsan (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                price VARCHAR(50),
                address VARCHAR(255),
                area VARCHAR(50)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
            """
        elif table_name == "dubaothoitiet":
            query = """
            CREATE TABLE IF NOT EXISTS dubaothoitiet (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city_name VARCHAR(255),
                rainfall VARCHAR(50),
                sky_description VARCHAR(255),
                current_temp VARCHAR(50),
                feels_like_temp VARCHAR(50)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
            """
        else:
            raise ValueError(f"Unknown table name: {table_name}")

        self.cursor.execute(query)

    def save_data(self, table_name, data):
        """
        Save data into the specified table. Ensures the table exists before insertion.
        
        Args:
            table_name (str): The name of the table to insert data into.
            data (dict): A dictionary where keys are column names and values are the data to be inserted.
        """
        if not data:
            raise ValueError("Data dictionary cannot be empty")

        self.ensure_table(table_name)  # Ensure the table exists before inserting data

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(data.values())

        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.cursor.close()
        self.connection.close()
