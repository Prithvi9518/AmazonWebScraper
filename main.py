from amazon_search.amazon_search import AmazonSearch
from amazon_search.filter_menu import FilterMenu


def get_search_item_from_user():
    return input("Enter the item you want to search: ")


def show_available_filters():
    print("If you'd like, there are some filters available to narrow down your search. Press:")
    print("0- No filters")
    print("1- Filter by customer ratings")


def get_desired_filter():
    show_available_filters()
    return int(input("Enter your choice: "))


search_item = get_search_item_from_user()

filter_menu = FilterMenu()

filter_menu.choose_filters()
desired_filters = filter_menu.filters

with AmazonSearch(teardown=False) as bot:

    bot.open_amazon()
    bot.accept_cookies()
    bot.search_item(search_item)
    bot.apply_filter(desired_filters)



