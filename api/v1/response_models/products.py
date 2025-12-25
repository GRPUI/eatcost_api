from typing import List, Dict, Any

import msgspec


class ProductItem(msgspec.Struct, omit_defaults=True):
    id: int
    name: str
    slug: str
    permalink: str
    date_created: str
    date_modified: str
    type: str
    status: str
    price: float
    regular_price: float
    sale_price: float
    stock_status: str
    categories: List[Dict[str, Any]]
    images: List[str]

class CategoryProducts(msgspec.Struct, omit_defaults=True):
    category_name: str
    items: List[ProductItem]
