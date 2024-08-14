# House-Price-Scraper
This project is a web scraper built using Scrapy to extract property data from Rightmove's house prices pages for the Southwark area. The spider crawls through the first 40 pages of the listings and saves the data to a CSV file.

## Features

- Extracts property information such as address, type, transaction history, and location.
- Automatically paginates through up to 40 pages.
- Outputs data to a CSV file/ JSON file


## Requirements

- Python 3.7+
- Scrapy

## Configuration

Before running the spider, you may need to update the following values in the `housespider.py` file to match your target website or requirements:

- **`name`**: The name of the spider. Update this to a unique name for your spider if needed.

    ```python
    name = "houseSpider"
    ```

- **`allowed_domains`**: List of allowed domains to ensure the spider does not crawl unwanted sites. Update this to include the domain of the website you're targeting.

    ```python
    allowed_domains = []
    ```

- **`start_urls`**: List of starting URLs where the spider will begin crawling. Update this to the URL(s) of the pages you want to scrape.

    ```python
    start_urls = []
    ```

These values are located in the `housespider.py` file in the root of the repository. Make sure to modify these settings according to your specific scraping needs.

## Usage

1. **Run the spider:**

    ```bash
    scrapy crawl houseSpider -o output.csv
    ```

    This command will start the spider and save the scraped data into `output.csv`.

2. **Customize the output format:**

    You can change the output format by replacing `output.csv` with a different file extension, such as `.json` or `.xml`. For example, to output as JSON:

    ```bash
    scrapy crawl houseSpider -o output.json
    ```

## Files

- `housespider.py`: The main spider file that contains the logic for scraping the data. Remember to update the configuration values as described above.
- `output.csv`: The default output file that contains the scraped data.


