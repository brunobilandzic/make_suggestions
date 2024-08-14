from metadata_model import Person
from metadata_map import *

categories = {
    "prostor": "PROSTOR",
    "vikendica": "VIKENDICA",
    "ostalo_tag": "OSTALO",
    "stan": "STAN",
}


translate_price_type = {
    "po najamnini": "naj",
    "?vrsta": "cvrsta",
    "?vrsta vremenski korigirana": "cvk",
    "realna": "realna",
    "fiktivna +": "+",
    "fiktivna -": "-",
    "labava procjena": "procjena",
}


def make_persons():
    persons = []
    for name in [["Vicko", "V"], ["Damir", "D"], ["Jana", "J"]]:
        persons.append(Person(name[0], name[1]))
    return list(persons)


def calculate_exclude():
    return list(ostalo_exclude) + list(stanovi_exclude)  + list(prostori_exclude) + list(vikendice_exclude) + list(default_exclude)

