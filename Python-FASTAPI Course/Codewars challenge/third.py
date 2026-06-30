inventory = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 300
}

{'laptop': 1080.0, 'mouse': 25, 'keyboard': 80, 'monitor': 270.0}

def apply_discount(items: dict) -> dict:
    return {
        product: price * 0.9 if price > 100 else price
        for product, price in items.items()
    }
