# Gürkan Bıyık 07.04.2024
# https://www.linkedin.com/in/grkanbyk/
# https://github.com/grknbyk

# petlebi_scrapy.py
import json
import scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess

class PetlebiSpider(scrapy.Spider):
    name = "petlebi"
    allowed_domains = ["petlebi.com"]    
    start_urls = [
        "https://www.petlebi.com/kopek-petshop-urunleri?page=1&op=json",  # 3568 products
        "https://www.petlebi.com/kedi-petshop-urunleri?page=1&op=json",  # 3115 products
        "https://www.petlebi.com/kus-petshop-urunleri?page=1&op=json",  # 282 products
        "https://www.petlebi.com/kemirgen-petshop-urunleri?page=1&op=json",  # 133 products
    ]

    def parse(self, response):
        json_data = json.loads(response.body)
        products = Selector(text=json_data["response"]).css("div.card-body.pb-0.pt-2.pl-3.pr-3")

        for product in products:
            item = {}

            product_data = json.loads(product.css("a::attr(data-gtm-product)").get())
            
            item["id"] = product_data["id"]
            item["name"] = product_data["name"]
            item["brand"] = product_data["brand"]
            item["price"] = float(product_data["price"])
            item["url"] = product.css("a::attr(href)").get()
            item["stock"] = product_data["dimension2"]
            item["category"] = product_data["category"]
            item["sku"] = ""  # couldn't find in the page

            yield response.follow(url=item["url"], callback=self.parse_product, meta={"item": item})


        next_url = json_data["next_data_url"] # next page data api url
        if next_url != "": # if there is a next page, continue to scrape
            yield response.follow(url=next_url, callback=self.parse)

    def parse_product(self, response):
        item = response.meta["item"]

        item["barcode"] = response.xpath('//div[@class="row mb-2"][div[@class="col-2 pd-d-t" and contains(text(), "BARKOD")]]/div[@class="col-10 pd-d-v"]/text()').get().strip()

        description = response.xpath('//span[@id="productDescription"]//text()').getall() 
        item["description"] = "".join(description).strip().replace('"',"'")

        item["images"] = [
            link.replace("//", "", 1) # remove double slashes '//' from the beginning of the link
            for link in response.css("a.thumb-link::attr(data-image)").extract()[:-2] # exclude 2 default img
        ]
                
        yield item
        


process = CrawlerProcess({
"DOWNLOAD_DELAY": 0,
"FEEDS": {"petlebi_products.json": {"format": "json", "encoding": "utf8", "overwrite": True}}
})

process.crawl(PetlebiSpider)
process.start()

print("Scraping is completed successfully.")