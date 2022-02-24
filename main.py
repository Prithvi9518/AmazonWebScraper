from amazon_search.amazon_search import AmazonSearch

search_item = input("Enter the item you want to search: ")

with AmazonSearch(teardown=False) as bot:

    bot.open_amazon()
    bot.accept_cookies()
    bot.search_item(search_item)

