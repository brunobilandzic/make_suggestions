def iterator_length(iterator):
    return iterator.stop - iterator.start


def calculate_length(include, exclude):
    return iterator_length(include) - iterator_length(exclude)


def print_iterator(iterator):
    for item in iterator:
        print(item)


def flatten_array(array_to_flatten):
    flattened_array = []
    for item in array_to_flatten:
        for sub_item in item:
            flattened_array.append(sub_item)
    return flattened_array


def skip_rows(reader, count):
    for i in range(count):
        next(reader)
        
def print_items(items):
    print("Here are the items.")
    print_iterator(items)


def make_csv_from_used_items(used_items):
    items_csv_array = [f"{item.name} {item.tag} {item.table_tag} {item.price} {item.price_type}" for item in used_items]
    return items_csv_array      