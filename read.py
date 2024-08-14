import csv
from random import shuffle
from helper_iterator import skip_rows, calculate_length
from metadata_model import Item
from helper_parser import excel_float_to_float
from constants import categories, translate_price_type
from metadata_map import *
from category_operations import items_category_percentage
from math_operations import put_deviation


def test_excel(line):
    print("in test excel ", line[53])


def make_items(file, do_shuffle):
    items = []
    prostori_items = read_prostori(file, do_shuffle)
    items.extend(prostori_items)
    stanovi_items = read_stanovi(file, do_shuffle)
    items.extend(stanovi_items)
    vikendice_items = read_vikendice(file, do_shuffle)
    items.extend(vikendice_items)
    ostalo_items = read_ostalo(file, do_shuffle)
    items.extend(ostalo_items)
    put_deviation(items)
    items_category_percentage(items)
    return items


def read_prostori(file, do_shuffle):
    file.seek(0)
    reader = csv.reader(file)
    skip_rows(reader, prostori.start - 1)
    i = 0
    items = []
    for line in reader:
        rownumber = int(line[rownumber_column  - 1])
        if rownumber in stanovi_exclude:
            continue
        item = Item(line[0], categories["prostor"], excel_float_to_float(line[price_column]), rownumber, line[table_tag_column], translate_price_type[line[price_type_column]], line[price_type_column])
        items.append(item)
        i += 1
        if i >= calculate_length(prostori, prostori_exclude):
            break

    if do_shuffle:
        shuffle(items)

    return items


def read_vikendice(file, do_shuffle):
    file.seek(0)
    reader = csv.reader(file)
    skip_rows(reader, vikendice.start - 1)
    i = 0
    items = []
    for line in reader:
        rownumber = int(line[rownumber_column  - 1])
        if rownumber in stanovi_exclude:
            continue
        item = Item(line[0], categories["vikendica"], excel_float_to_float(line[price_column]), rownumber, line[table_tag_column], translate_price_type[line[price_type_column]], line[price_type_column])
        items.append(item)
        i += 1
        if i >= calculate_length(vikendice, vikendice_exclude):
            break
    if do_shuffle:
        shuffle(items)

    return items


def read_stanovi(file, do_shuffle):
    file.seek(0)
    reader = csv.reader(file)
    skip_rows(reader, stanovi.start - 1)
    i = 0
    items = []
    for line in reader:
        rownumber = int(line[rownumber_column  - 1])
        if rownumber in stanovi_exclude:
            continue
        item = Item(line[0], categories["stan"], excel_float_to_float(line[price_column]), rownumber, line[table_tag_column],translate_price_type[line[price_type_column]], line[price_type_column])
        items.append(item)
        i += 1
        if i >= calculate_length(stanovi, stanovi_exclude):
            break
    if do_shuffle:
        shuffle(items)

    return items


def read_ostalo(file, do_shuffle):
    file.seek(0)
    reader = csv.reader(file)
    skip_rows(reader, ostalo.start - 1)
    i = 0
    items = []
    for line in reader:
        rownumber = int(line[rownumber_column  - 1])
        if rownumber in ostalo_exclude:
            continue
        item = Item(line[0], categories["ostalo_tag"], excel_float_to_float(line[price_column]), rownumber, line[table_tag_column], translate_price_type[line[price_type_column]], line[price_type_column])
        items.append(item)
        i += 1
        if i >= calculate_length(ostalo, ostalo_exclude):
            break
    if do_shuffle:
        shuffle(items)

    return items


def read_data(filename, do_shuffle):
    with open(filename, "r") as f:
        return make_items(f, do_shuffle)