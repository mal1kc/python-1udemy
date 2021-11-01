import json
import scrapy


class bookSpider(scrapy.Spider):
    name = "book_spider"
    pageCount = int()
    jsonouts = list()
    after_data = dict()
    # def start_requests(self):
    #
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse),
    with open(r"books.json", "r", encoding="utf-8") as f:
        try:
            before_data = json.load(f)
        except:
            before_data = {}

    file = open("books.json", "w", encoding="utf-8")

    print(before_data.keys())
    try:
        for key in before_data.keys():
            after_data[key] = before_data[key]
    except:
        after_data = {}

    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/category&filter_category_all=true&path=1&page=1"
    ]

    def parse(self, response):
        page = int(response.url[-1])
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author a span::text").extract()
        book_publishers = response.css("div.publisher a span::text").extract()
        i = 0
        temp_list = list()
        while i < len(book_names):
            temp_list.append({
                "name": book_names[i],
                "author": book_authors[i],
                "publisher": book_publishers[i],
            })
            i += 1

        if temp_list is not None:
            self.after_data[f"page_{page}"] = dict()
            itemnumber = 0
            for item in temp_list:
                self.after_data[f"page_{page}"][str(itemnumber)] = item
                itemnumber += 1
        # * next page
        next_url = response.css(
            "html body.tr div.content-bg div.container_12 div#content.grid_9 div.box.no-padding div.pagination div.links a.next::attr(href)").extract_first()
        self.pageCount += 1
        if next_url is not None and self.pageCount != 5:
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.jsonouts = list()
            self.jsonouts.append(json.dumps(self.after_data, indent=4))
            for d in self.jsonouts:
                self.file.write(d)
            self.file.close()
