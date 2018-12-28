## Pole courses scraper
Scrapes all available coursers with title, start and end date
## Supported websites
1. Pole People: [http://www.polepeople.co.uk/](http://www.polepeople.co.uk/)

## Dev Setup
1. get `pipenv`
```
pip3 install pipenv
```
2. Clone the repo
3. Install deps: `cd polescraper && pipenv install`
4. Run the scraper:
```
scrapy crawl polepeople
```
