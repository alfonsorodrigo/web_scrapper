import argparse
import logging

logging.basicConfig(level=logging.INFO)

from settings import SITES


logger = logging.getLogger(__name__)


def _news_scraper(news_site):
    host = SITES[news_site]["url"]

    logging.info("Beginning scraper for {}".format(host))
    logging.info("Finding links in homepage...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_site_choices = list(SITES.keys())
    parser.add_argument(
        "news_site",
        help="The news site that you want to scrape",
        type=str,
        choices=news_site_choices,
    )

    args = parser.parse_args()
    _news_scraper(args.news_site)
