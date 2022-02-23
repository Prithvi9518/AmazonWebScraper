from amazon_search.amazon_search import AmazonSearch

with AmazonSearch(teardown=False) as bot:
    bot.open_amazon()