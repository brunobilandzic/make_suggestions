import os


def delete_all_temp_files():
    filenames = os.listdir("files/temp")
    for filename in filenames:
        if filename == "dont_delete.txt":
            continue
        os.remove("files/temp/" + filename)