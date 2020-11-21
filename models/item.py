import uuid
from abc import ABC
from dataclasses import dataclass, field
import requests
import re
from typing import Dict
from bs4 import BeautifulSoup
from models.model import Model


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    price: float = field(default=None)

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find(self.tag_name, self.query)
        string_price = elements.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d\d)")  # (\d,?\d\d\d\.\d\d)
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        return self.price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "price":self.price,
            "query": self.query
        }
