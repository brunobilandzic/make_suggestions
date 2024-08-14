from constants import categories
from helper_parser import parse_regular_input
from metadata_model import Category


def get_category_items(_items, category_tag):
    def is_in_category(_item):
        return _item.category == category_tag
    in_category = list(filter(is_in_category, _items))
    return in_category


def get_category_count(_items, category_tag):
    return len(get_category_items(_items, category_tag))


def create_category_array(_items):
    categories_array = []
    for category in categories:
        category_item = Category(categories[category],
                                 get_category_count(_items, categories[category]),
                                 sum_category_price(_items, categories[category]))
        categories_array.append(category_item)
    return categories_array


def sum_category_price(_items, category_tag):
    category_price = 0
    category_items = get_category_items(_items, category_tag)
    for _item in category_items:
        category_price += _item.price
    return category_price


def items_category_percentage(_items):
    for category in categories:
        category_items = get_category_items(_items, categories[category])
        category_price = sum_category_price(_items, categories[category])
        for _item in category_items:
            if(category_price == 0):
                _item.category_price = 0
                continue
            _item.category_price = (_item.price / category_price) * 100


def get_assing_by_category(callback):
    will = parse_regular_input("\nAssing by category price sum or wholte price sum? Type (Y) or (y) to assign by sum of category prices, type any other button to assign it based on all item values: ", callback)
    assing_by_category = False
    if will == "Y" or will == "y":
        assing_by_category = True
    return assing_by_category