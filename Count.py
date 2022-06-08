# This code adds the total of prices in the Receipt subdirectory
# Each file name in the Receipt subdirectory that ends with .jpg or .png is added to a list
# The substring of the file name is converted to an integer and totaled
# File names are Formatted as: store-price-date.jpg, store-price-date.jpeg, or store-price-date.png

from turtle import st
import os
import regex


class Store:
    def __init__(self, name):
        self.name = name
        self.total_spent = 0.0
        self.count = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def header():
    # Print the header
    print(f"\t{bcolors.HEADER}Reciepts Calculator")
    print("\t  by: Geoffery10")
    print(f"\t==================\n{bcolors.OKCYAN}")

def main():
    filenames = []
    price_total = 0.0
    stores = []
    stores_obj = []
    count = 0
    delimiter = " - "

    header()

    for filename in os.listdir('Receipt'):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            filenames.append(filename)
            count += 1
    print('Total number of files:', count)
    if count == 0:
        print(f'{bcolors.WARNING}No receipts found in the Receipt directory{bcolors.ENDC}')
        return

    # Add every store
    for filename in filenames:
        if filename.split(delimiter)[0] not in stores:
            store_name = filename.split(delimiter)[0]
            print(f'{store_name} added to list')
            stores.append(store_name)

    for store in stores:
        stores_obj.append(Store(store))

    # Add the prices and total
    for filename in filenames:
        # delimiter is delimiter
        price_total += float(filename.split(delimiter)[1])
        for store in stores_obj:
            if store.name == filename.split(delimiter)[0]:
                store.total_spent += float(filename.split(delimiter)[1])
                store.count += 1
    
    # Print out the total per store
    print(f'\n\t{bcolors.OKGREEN}Total per store:{bcolors.OKBLUE}')
    for store in stores_obj:
        print(
            f"- {store.name} [{store.count}]: {bcolors.OKCYAN}${store.total_spent}{bcolors.OKBLUE}")
    # Print out the total
    print(f'\n\t{bcolors.OKGREEN}Total: {bcolors.OKCYAN}${price_total}')



if __name__ == "__main__":
    main()
