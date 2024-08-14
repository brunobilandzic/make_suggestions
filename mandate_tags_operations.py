from helper_iterator import flatten_array
from helper_parser import parse_int_input
from helper_parser import parse_regular_input
from read import read_data
from metadata_model import Person_Mandates
from constants import make_persons, calculate_exclude
import os
import csv
from dotenv import load_dotenv

load_dotenv()
items = read_data(os.environ["filename"], False)

def make_unique_persons_mandate_tags(_perons_mandate_tags1, _persons_mandate_tags2):
    persons_mandate_tags = []
    for person_mandate_tags1 in _perons_mandate_tags1:
        existing_person_mandate_tags_array = [person_mandate_tags for person_mandate_tags in persons_mandate_tags if person_mandate_tags.name == person_mandate_tags1.name]
        existing_person_mandate_tags = None
        if(bool(existing_person_mandate_tags_array)):
            existing_person_mandate_tags = existing_person_mandate_tags_array[0]
        if existing_person_mandate_tags:
            existing_person_mandate_tags.mandate_tags += person_mandate_tags1.mandate_tags
        else:
            persons_mandate_tags.append(person_mandate_tags1)
    for person_mandate_tags2 in _persons_mandate_tags2:
        existing_person_mandate_tags_array = [person_mandate_tags for person_mandate_tags in persons_mandate_tags if person_mandate_tags.name == person_mandate_tags2.name]
        existing_person_mandate_tags = None
        if(bool(existing_person_mandate_tags_array)):
            existing_person_mandate_tags = existing_person_mandate_tags_array[0]
        if existing_person_mandate_tags:
            existing_person_mandate_tags.mandate_tags += person_mandate_tags2.mandate_tags
        else:
            persons_mandate_tags.append(person_mandate_tags2)
    return persons_mandate_tags


def load_mandate(callback, tag_range_min, tag_range_max, tag_range_exclude, entered_mandates, name, max_items_count):
    mandate_items_tags = []
    mandate_item_num = 1
    print(f"Enter Max {max_items_count} for {name} ")
    try:
        input_data = 1
        while (
            not input_data == 0 and
            not mandate_item_num > max_items_count
            ):
            input_data = parse_int_input(f"Enter mandate item no{mandate_item_num} from {tag_range_min} to {tag_range_max} for {name}, exclude {list(set(tag_range_exclude+ entered_mandates + mandate_items_tags))} if you want to quit, enter 0:", callback)
            if input_data == 0:
                break
            if(
                input_data in entered_mandates or
                input_data in mandate_items_tags
            ):
                print("Value is already assigned. Enter another")
                continue
            if(
                input_data < tag_range_min or
                input_data > tag_range_max or
                input_data in tag_range_exclude
            ):
                print("That tag number falls out of range. Plese enter another")
                continue
            mandate_item_num += 1
            mandate_items_tags.append(input_data)
    except ValueError:
        print("Enter valid number")


    print(f"You've entered {mandate_items_tags}")
    return mandate_items_tags


def calculate_max_mandate(_person, _persons):
    if len(_person.mandate_items) >= len(items):
         return 0
    return len(items) - sum([len(person.mandate_items) for person in _persons])


def get_mandate_tags(person):
    return [item.tag for item in person.mandate_items]


def make_iterable_from_person_mandate_tags(_person_mandate_tags):
    iterable = []
    iterable.append(_person_mandate_tags.name)
    for mandate_tag in _person_mandate_tags.mandate_tags:
        iterable.append(mandate_tag)
    return iterable


def enter_additional_mandates(_persons, _mandates_from_files, callback):
    mandates = flatten_array([person_mandates.mandate_tags for person_mandates in _mandates_from_files])
    persons_mandate_tags = []
    for person in _persons:
        person_mandate_tags = load_mandate(callback, min([item.tag for item in items]), max([item.tag for item in items]), calculate_exclude(), mandates, person.name, len(items) - len(mandates))
        mandates = mandates + person_mandate_tags
        persons_mandate_tags.append(Person_Mandates(person.name, person_mandate_tags))
    return persons_mandate_tags


def save_mandates(callback):
    _persons = make_persons()
    person_mandates_array = [] 
    mandates = []
    for person in _persons:
        person_mandate_tags = load_mandate(callback, min([item.tag for item in items]), max([item.tag for item in items]), calculate_exclude(), mandates, person.name, calculate_max_mandate(person, _persons))
        mandates = mandates + person_mandate_tags
        person_mandates_array.append(Person_Mandates(person.name, person_mandate_tags))
    filename = input("Enter filename (without .csv): ")
    filename_full = "files/mandates/" + filename + ".csv"
    if("/" in filename):
        os.makedirs(os.path.dirname(filename_full), exist_ok=True)
    with open(filename_full, "w", newline="") as f:
        writer = csv.writer(f)
        for person_mandates in person_mandates_array:
            writer.writerow(make_iterable_from_person_mandate_tags(person_mandates))


def make_mandate_tags_array(line):
    mandate_tags_array = []
    for i in range(1, len(line)):
        mandate_tags_array.append(int(line[i]))
    return mandate_tags_array


def read_mandates(mandate_tags_name):
    filename = "files/mandates/" + mandate_tags_name + ".csv"
    with open(filename, "r") as f:
        reader = csv.reader(f)
        persons_mandate_tags = []
        for line in reader:
            mandate_tags = make_mandate_tags_array(line)
            persons_mandate_tags.append(Person_Mandates(line[0], mandate_tags))
    return persons_mandate_tags 


def enter_mandates(_persons, _persons_mandates_array):
    for person_mandates in _persons_mandates_array:
        person = [person for person in _persons if person.name == person_mandates.name][0]
        person.mandate_items = [item for item in items if item.tag in person_mandates.mandate_tags]
        

def resolve_mandates(_persons, callback):
    mandates_read_from_file = []
    additional_mandates = []
    will = parse_regular_input("\nDo you wish to load default mandates from some file? (Y) or (y) for yes, any other letter for no: ", callback)
    if(will == "Y" or will == "y"):
        filename = parse_regular_input("\nEnter mandate filename (without .csv): ", callback)
        mandates_read_from_file = read_mandates(filename)
        will = parse_regular_input("\nDo you want to enter additional mandates? (Y) or (y) for yes, any other letter for no:  ", callback)
        if(will == "Y" or will == "y"):
            additional_mandates = enter_additional_mandates(_persons, mandates_read_from_file, callback)
    else:
        will = parse_regular_input("\nDo you wish to enter mandates? (Y) or (y) for yes, any other letter for no:  ", callback)
        if(will == "Y" or will == "y"):
            additional_mandates = enter_additional_mandates(_persons, mandates_read_from_file, callback) 
    return make_unique_persons_mandate_tags(mandates_read_from_file, additional_mandates)