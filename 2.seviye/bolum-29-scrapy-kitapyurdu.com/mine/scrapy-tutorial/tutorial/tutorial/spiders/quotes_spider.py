import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count = 1
    start_urls = [
                'http://quotes.toscrape.com/page/1/']
    
    def parse(self,response):
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            page_number = response.url[-3]     
            yield{
                "quote_page/count":{str(page_number),str(self.quote_count)},
                "title":title,
                "author":author,
                "tags":tags,
            }
            self.quote_count += 1
        self.quote_count = 1
        next_url = response.css("li.next a::attr(href)").extract_first()
        if next_url is not None:
            next_url = "http://quotes.toscrape.com"+next_url
            yield scrapy.Request(url=next_url,callback=self.parse)
            
        
    
    
        
    # def start_requests(self):
    #     
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')
    