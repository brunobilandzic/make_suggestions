from read import read_data
from helper_iterator import print_items
from house_keeping import delete_all_temp_files
from dotenv import load_dotenv
import os
from mandate_tags_operations import save_mandates
from combinations_operations import make_new_combinations_of_combinations


load_dotenv()
items = read_data(os.environ["filename"], False)


def print_menu():
    delete_all_temp_files()
    print("------------------------------------------"*3)
    print("Menu")
    choice = None
    while 1:
        print("Enter 1 to make combinations")
        print("Enter 2 to print all items")
        print("Enter 3 to make new mandates")
        print("Enter 0 to exit\n")
        choice = int(input("\n\n"))
        match choice:
            case 1:
                make_new_combinations_of_combinations(callback(choice))
            case 2:
                print_items(items)
            case 3:
                save_mandates(callback(choice))
            case 0:
                delete_all_temp_files()
                exit()
    delete_all_temp_files()


def callback(choice):
    choice = None
    return print_menu
    

if __name__ == "__main__":
   print_menu()
