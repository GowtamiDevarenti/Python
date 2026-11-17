import requests

from get_json import get_json

BASE_URL = "https://fakestoreapi.com"


# Exercise 1: Sort the products by price

def retrieve_products():
    products = get_json(f"{BASE_URL}/products")

    if products is not None:
        sorted_products = sorted(
            products, key=lambda product: product["price"]
        )

        for line_item, product in enumerate(sorted_products, 1):
            print(
                f'{line_item}. {product["title"]:<100} {product["price"]} kr'
            )

retrieve_products()
