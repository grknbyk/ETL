# Petlebi Scraper
### Scraping Petlebi.com Products with Python
Those URLs are used because they leverage an API that enhances performance for requests and makes data selection easier:

- https://www.petlebi.com/kopek-petshop-urunleri?page=1&op=json
- https://www.petlebi.com/kedi-petshop-urunleri?page=1&op=json
- https://www.petlebi.com/kus-petshop-urunleri?page=1&op=json
- https://www.petlebi.com/kemirgen-petshop-urunleri?page=1&op=json

### Total Scraped Products
https://www.petlebi.com/kopek-petshop-urunleri &emsp;&emsp; 2858 products 
<br>https://www.petlebi.com/kedi-petshop-urunleri &emsp;&emsp;&nbsp;&nbsp;&nbsp; 2809 products
<br>https://www.petlebi.com/kus-petshop-urunleri &emsp;&emsp;&emsp;&nbsp;&nbsp; 254 products
<br>https://www.petlebi.com/kemirgen-petshop-urunleri &nbsp;&nbsp;&nbsp; 122 products   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-------------------------------------------  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; Total: &emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; 6043 products   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;  Scraped: &emsp;&emsp;&emsp;&emsp; 5758 products <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;------------------------------------------- <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;Time Elapsed:   17 minutes (07.07.2024)

## Files

- `petlebi_scrapy.py`: Scrapy spider to scrape product data.
- `petlebi_products.json`: JSON file with scraped product data.
- `import_products.py`: Script to import JSON data into MySQL database.
- `petlebi_create.sql`: SQL script to create the `petlebi` table.
- `petlebi_insert.sql`: SQL script to insert data into the `petlebi` table.

## Setup

### Prerequisites

- Python 3.x
- Scrapy
- MySQL

### Installation

1. Clone the repository.
2. Install the required Python packages:
```bash
pip install scrapy mysql-connector-python
```

## Usage

To execute the scripts, follow these steps:

1. **Scrape Data:**
   - Run `petlebi_scrapy.py` to scrape product data.
   - This script will generate a JSON file named `petlebi_products.json`.

2. **Load Data into MySQL:**
   - Run `import_products.py` to load the scraped data into a MySQL database.
   - Ensure you configure the database connection settings in the script before running it.
   - The script will:
     - Create a database named `petlebi` if it doesn't already exist.
     - Create a table named `petlebi` within the `petlebi` database.
     - Insert the data from `petlebi_products.json` into the `petlebi` table.


## License

This project is licensed under the MIT License.
