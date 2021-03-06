from amazon_search.amazon_search import AmazonSearch
from amazon_search.filter_menu import FilterMenu


def get_search_item_from_user():
    return input("Enter the item you want to search: ")


search_item = get_search_item_from_user()

filter_menu = FilterMenu()

filter_menu.choose_filters()
desired_filters = filter_menu.filters

try:
    with AmazonSearch(teardown=False) as bot:

        bot.open_amazon()
        bot.accept_cookies()
        bot.search_item(search_item)
        bot.apply_filter(desired_filters)
        bot.get_results()
except Exception as e:
    raise




