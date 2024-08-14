from read import read_data
from category_operations import get_category_items
from metadata_model import item_price

import os
from dotenv import load_dotenv


load_dotenv()


def make_random_choices(_persons, _choose_by_ctagory):
    items = read_data(os.environ["filename"], True)
    for item in items:
        item.assigned = False
    assing_mandate_items(_persons)
    for person in _persons:
        for mandate_item in person.mandate_items:
            item_found = [item for item in items if item.tag == mandate_item.tag][0]
            item_found.assigned = True
    for item in items:
        while not item.assigned:
            person = None
            if(_choose_by_ctagory):
                person = person_with_min_category_items_price_sum(items, _persons, item.category)
            else:
                person = person_with_min_items_price_sum(items, _persons)
            
            if(not person):
                print("No person found")
                return
            person.items.append(item)
            item.assigned = True


def assing_mandate_items(_persons):
    for person in _persons:
        for mandate_item in person.mandate_items:
            person.items.append(mandate_item)


def person_with_min_category_items_price_sum(_items, _persons, _category_tag):
    person_to_return = None
    category_items = get_category_items(_items, _category_tag)
    min_item_price = sum(list(map(item_price, category_items)))
    for person in _persons:
        person_sum = sum(item.price for item in get_category_items(person.items, _category_tag))
        if person_sum < min_item_price:
            min_item_price = person_sum
            person_to_return = person
    return person_to_return


def person_with_min_items_price_sum(_items, _persons):
    person_to_return = None
    min_item_price = sum(list(map(item_price, _items)))
    for person in _persons:
        person_sum = sum(item.price for item in person.items)
        if person_sum < min_item_price:
            min_item_price = person_sum
            person_to_return = person
    return person_to_return