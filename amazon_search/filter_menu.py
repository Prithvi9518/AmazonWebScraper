class FilterMenu:
    def __init__(self):
        self.filters = []

    def show_available_filters(self):
        print("If you'd like, there are some filters available to narrow down your search. Press:")
        print("0- No filters")
        print("1- Filter by customer ratings")
        print("2- Show today's deals")
        print("3- Show all discounted products")
        print("4- Specify minimum and maximum price")

    def choose_filters(self):
        self.show_available_filters()
        filter_choice = int(input("Enter your choice: "))
        self.filters.append(filter_choice)
        self.add_filters(filter_choice)

    def add_filters(self, filter_choice):
        if filter_choice == 1:
            self.filter_by_customer_ratings()
        elif filter_choice == 2:
            print("Fetching today's deals...")
        elif filter_choice == 3:
            print("Fetching all discounted products...")
        elif filter_choice == 4:
            self.get_min_max_price()
        elif filter_choice == 0:
            print("No filters added.")

    def filter_by_customer_ratings(self):
        self.show_customer_rating_options()
        customer_rating = int(input("Enter your choice: "))
        self.filters.append(customer_rating)

    def show_customer_rating_options(self):
        print("Filter By Customer Rating:")
        print("Press: ")
        print("1- 1 Star and Above")
        print("2- 2 Stars and Above")
        print("3- 3 Stars and Above")
        print("4- 4 Stars and Above")

    def get_min_max_price(self):
        min_price = input("Please enter the minimum price"
                          " (Just press ENTER if no minimum price needs to be specified): ")
        max_price = input("Please enter the maximum price "
                          "(Just press ENTER if no maximum price needs to be specified): ")

        self.filters.append(min_price)
        self.filters.append(max_price)


