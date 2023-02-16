import logging
import re
from functools import lru_cache
from typing import Any, Optional, Union
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from httpx import AsyncClient

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@lru_cache
def is_valid_logo(logo_url: str) -> bool:
    try:
        response = requests.head(logo_url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def extract_base_url(url: str) -> str:
    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc
    return base_url


def extract_logo(url: str, soup: BeautifulSoup) -> Optional[str]:
    logos = soup.find_all("img", {"class": re.compile(r".*logo.*")})
    logo_url = None
    if logos:
        for logo in logos:
            logo_url = logo.get("src")
            if not logo_url.startswith("http"):
                if logo_url.startswith("/"):
                    logo_url = f"{extract_base_url(url)}{logo_url}"
                else:
                    logo_url = f"{extract_base_url(url)}/{logo_url}"
            if is_valid_logo(logo_url):
                break
    else:
        logger.info("website's logo not found")
    return logo_url


def extract_phones(soup: BeautifulSoup) -> list[str]:
    regex = r"(\+?\d[\d\s-]+\d|\(?\d+\)?[\d\s-]+\d+|\d{4}[\s-]?\d{4})"
    phones = []
    for tag in soup.find_all("a", href=re.compile(r"tel:")):
        match = re.search(regex, tag.get("href"))
        if match:
            phones.append(match.group())
    return phones


async def make_request_async(
    client: AsyncClient, url: str
) -> Optional[Union[dict[str, Any], str]]:
    try:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            logo_url = extract_logo(url, soup)
            phones = extract_phones(soup)
            return {"logo": logo_url, "website": url, "phones": phones}
        else:
            logger.error(f"URL: {url} status code = {response.status_code}")
            return "DeadPage"
    except Exception as exc:
        logger.exception(exc)
        return None
