import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(data.resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            # Print current resource values
            print(f"Bread: {data.resources['bread']} slice(s)")
            print(f"Ham: {data.resources['ham']} slice(s)")
            print(f"Cheese: {data.resources['cheese']} ounce(s)")
        elif choice in data.recipes:
            sandwich = data.recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich['ingredients']):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(choice, sandwich['ingredients'])
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()