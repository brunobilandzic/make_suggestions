class Item:
    def __init__(self, name, category, price, tag, _table_tag, _price_type_short, _price_type):
        self.name = name
        self.category = category
        self.price = price
        self.tag = tag
        self.assigned = False
        self.table_tag = _table_tag
        self.price_type_short = _price_type_short
        self.price_type = _price_type
        
        
    def __repr__(self):
        return f"\tName: {self.name}\n\tTag: {self.tag}\n\tCategory: {self.category}\n\tPrice: {self.price}\n\tPrice type:{self.price_type}\n\tTable tag: {self.table_tag}\n\tDeviation: {self.deviation}\n\tShare in category: {self.category_price}\n"


    deviation = 0.0
    category_price = 0.0

class Category:
    def __init__(self, category, count, sum):
        self.category = category
        self.count = count
        self.sum = sum
    def __repr__(self):
        return f"{self.category} has {self.count} items, it's sum is {self.sum}"

    sum = 0.0


class Person:
    def __init__(self, name, _short_name):
        self.name = name
        self.items = []
        self.mandate_items = []
        self.short_name = _short_name
    def __repr__(self):
        return f"\nPerson: {self.name}\nHas {len(self.items)} items worth {sum([item.price for item in self.items])}\nItems: {(self.items)}\nMandate: {self.mandate_items}"


class Parameters():
    def __init__(self, _number_of_combinations) -> None:
        self.number_of_combinations = _number_of_combinations

    def __repr__(self) -> str:
        return f"{self.number_of_combinations}"


class Person_Mandates():
    def __init__(self, _name, _mandate_tags) -> None:
        self.name = _name
        self.mandate_tags = _mandate_tags


class Combination():
    def __init__(self, _persons, _combinations_name, _tag, _persons_mandate_tags) -> None:
        self.persons = _persons
        self.tag = _tag
        self.combinations_name = _combinations_name
        self.persons_mandate_tags = _persons_mandate_tags

    def __repr__(self) -> str:
        testarray = []
        for person in self.persons:
            testarray.append(f"{person.name} got {len(person.items)} worth {sum([item.price for item in person.items])}\n")
        str = f"Combination {self.tag} in {self.combinations_name}\n"
        for item in testarray:
            str += item
        return str


class Combinations():
    def __init__(self, _name, _count) -> None:
        self.name = _name
        self.count = _count
        
               
    combinations = []
    used_items = []


def item_price(item):
    return item.price