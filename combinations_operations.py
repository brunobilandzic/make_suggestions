from helper_other import get_computer_name
from constants import make_persons
from choice import make_random_choices
from helper_iterator import  make_csv_from_used_items
from helper_parser import parse_regular_input, parse_int_input, float_to_string
from read import read_data
from mandate_tags_operations import enter_mandates, resolve_mandates
from category_operations import get_assing_by_category
from metadata_model import Combinations, Combination
from tabulate import tabulate
import csv
import os
from dotenv import load_dotenv

load_dotenv()
items = read_data(os.environ["filename"], False)


def make_combinations(callback, _combinations_of_combinations, _combination_index, _all_persons_mandate_tags, _assing_by_category):
    computer_combinations_of_combinations_name = get_computer_name(_combinations_of_combinations.name)
    combinations_array = []
    for i in range(int(input(f"\nHow many combinations for combination {_combination_index + 1} / {_combinations_of_combinations.count } in {_combinations_of_combinations.name }:  "))):   
        _persons = make_persons() 
        enter_mandates(_persons, _all_persons_mandate_tags)
        make_random_choices(_persons, _assing_by_category)
        combination = Combination(_persons, _combinations_of_combinations.name, i + 1, _all_persons_mandate_tags)        
        combinations_array.append(combination)
        _combinations_of_combinations.combinations.append(combination)
    print_and_save_combinations(_combination_index, computer_combinations_of_combinations_name, combinations_array, callback)
    
   
def print_and_save_combinations(combinations_of_combinations_index, computer_combinations_of_combinations_name, combinations, callback):
    items_length = len(items)
    will = parse_regular_input("\nDo you want to show prices and prices types in header? Type (y) or (Y) for yes, any other letter for no:  ", callback)
    show_prices = True if will == "Y" or will == "y" else False
    if show_prices:
        items_tags_array = [f"{item.table_tag}\n{float_to_string(item.price)}\n{item.price_type_short[:3]}" for item in items]
    else:
        items_tags_array = [f"{item.table_tag}" for item in items]
    header = ["CMB"] + items_tags_array
    
    combination_index = 1
    rows = []
    csv_rows = []
    for combination in combinations:
        row = [combination_index]
        csv_row = [combination_index]
        for  items_index in range(items_length):
            for  person in combination.persons:
                for  item in person.items:
                    if item.tag == items[items_index].tag:
                        row.append(person.short_name)
                        csv_row.append(person.short_name)
        rows.append(row)
        csv_rows.append(csv_row)
        combination_index += 1

    print(tabulate(rows, headers=header, tablefmt="rst"))   
    with open(f"files/csv_output/{computer_combinations_of_combinations_name}.csv", "a") as w:
           writer = csv.writer(w, delimiter=";")
           writer.writerow([combinations_of_combinations_index + 1])
           writer.writerows(csv_rows)
           
           
def make_new_combinations_of_combinations(callback):
    combinations_name = parse_regular_input("\nEnter desired name for combinations of combinations, not number:  ", callback)
    combinations_count = parse_int_input("\nEnter desired number of combinations of combinations: ", callback)
    combinations = Combinations(combinations_name, combinations_count)
    combinations.used_items = items
    with open(f"files/csv_output/{get_computer_name(combinations.name)}.csv", "w") as w:
        writer = csv.writer(w, delimiter=";")
        items_csv_array = make_csv_from_used_items(items)
        writer.writerow(items_csv_array)

    for combination_index in range(combinations.count):
        _persons = make_persons()
        print(f"\n\nCombinations {combination_index + 1}/{combinations.count} in {combinations.name}")
        all_persons_mandate_tags = resolve_mandates(_persons, callback)
        assing_by_category = get_assing_by_category(callback)
        make_combinations(callback, combinations, combination_index, all_persons_mandate_tags, assing_by_category, )