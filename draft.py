items = {

    "Perfect Grade": {
        'GUNDAM RAISER': 315.0,
        'Gundam SEED Astray': 320.0,
        'Wing Gundam': 350.0,
        'Freedom Gundam': 410.0
    },

    "Real Grade": {
        'RG GoldyMarg': 52.0,
        'RG Gao Gai Gar': 78.0,
        'God Gundam': 58.0,
        'Wing Gundam': 38.0
    },

    "Master Grade": {
        'Eclipse Gundam': 195.0,
        'Full Saber': 72.0,
        'Unicorn Gundam': 64.0,
        'Gundam Dynames': 56.0
    },

    "Mecha Girl": {
        'Messiah Ranka Lee': 95.0,
        'Ganesa': 20.0,
        'Arcanadea Lumitea': 75.0,
        'Tsubasa Kazanari': 90.0
    },

    "Motorized": {
        'Little Ryan': 30.0,
        'Elephant Racer': 17.0,
        'Zoids Stylaser': 148.0,
        'Cannon Bull': 35.0
    }

}

shopping_cart = []

discount_options = {
    '0': 0,
    '1': 0.05,
    '2': 0.1,
    '3': 0.15
}


def main_menu():
    print('\n--- Anime Toy Ordering System ---')
    print('1. View All Items')
    print('2. View Toy Categories')
    print('3. View Shopping Cart')
    print('4. Search For Items')
    print('5. Check Out')


def cat_menu():
    print('\nToy Categories: ')
    for i, cat in enumerate(items):
        print(f'{i + 1}. {cat}')


def it_menu(cat_choice):
    if 1 <= cat_choice <= 5:
        cat = list(items.keys())[cat_choice - 1]
        print(f'\nCategory: {cat}')
        print('\nItems:')
        item = items[cat]
        for i, (item, price) in enumerate(item.items()):
            print(f'{i + 1}. {item}: ${price}')
    else:
        print('\nInvalid Category number. Please try again')


def add_to_cart(cat_choice, it_choice, quant):
    for i, item in enumerate(items):
        if i == cat_choice - 1:
            for j, sub_item in enumerate(items[item]):
                if j == it_choice - 1:
                    shopping_cart.append({
                        'cat': item,
                        'item': sub_item,
                        'cost': items[item][sub_item],
                        'quant': quant
                    })
            break


def show_all_items():
    print('\nAll Items and Prices:')
    for category, items_dict in items.items():
        print(f'\nCategory: {category}')
        for item_name, item_price in items_dict.items():
            print(f'{item_name}: ${item_price}')


def cart_disp():
    print('\nShopping Cart: ')
    if shopping_cart:
        for i, item in enumerate(shopping_cart, start=1):
            print(f'{i}. {item["item"]}: ${item["cost"]} x {item["quant"]}')
            print(f'Sub Total: ${item["cost"] * item["quant"]}')
        r_choice = int(input('\nEnter Item number you want to perform an action to (0 to quit): '))
        if 1 <= r_choice <= len(shopping_cart):
            action_choice = input(f'\nWhat action would you like to perform on "{shopping_cart[r_choice - 1]["item"]}"?'
                                  f'\n1. Change quantity\n'
                                  f'2. Remove from cart\n'
                                  f'\nEnter option: ')
            if action_choice == '1':
                new_quantity = int(input(f'\nEnter new quantity for {shopping_cart[r_choice - 1]["item"]}: '))
                if new_quantity > 0:
                    shopping_cart[r_choice - 1]['quant'] = new_quantity
                    print(f'\nQuantity updated for {shopping_cart[r_choice - 1]["item"]}.')
                else:
                    print('Invalid quantity. Quantity must be greater than 0.')
            elif action_choice == '2':
                item = shopping_cart.pop(r_choice - 1)
                print(f'\n{item["item"]} has been removed from the cart.')
            else:
                print('\nInvalid input. Please try again.')
        elif r_choice == 0:
            return
        else:
            print('\nInvalid input. Please try again.')
            return
    else:
        print('Your cart is empty.')


def search_item():
    search_name = input('\nEnter the name of the item you want to search for: ')
    found_items = []

    for category, items_dict in items.items():
        for item_name, item_price in items_dict.items():
            if search_name.lower() in item_name.lower():
                found_items.append((category, item_name, item_price))
    if found_items:
        print('\nFound items:')
        for i, (category, item_name, item_price) in enumerate(found_items, start=1):
            print(f'{i}. {item_name} ({category}): ${item_price}')
        choice = int(input('\nEnter Item number to add to cart (0 to cancel): '))
        if 1 <= choice <= len(found_items):
            category, item_name, item_price = found_items[choice - 1]
            quantity_ = int(input(f'Enter quantity of {item_name} to add to your cart: '))
            category_items = items[category]
            if item_name in category_items:
                add_to_cart(category_items, item_name, quantity_)
                print(f'{item_name} added to cart.')
            else:
                print('Item not found in category.')
        elif choice == 0:
            return
        else:
            print('Invalid input. Please try again.')
    else:
        print('No items matching the search term were found.')


def checkout():
    print('\nCheckout:')
    print('0. Non-Member')
    print('1. Bronze Member')
    print('2. Silver Member')
    print('3. Gold Member')

    while True:
        discount_choice = input('\nEnter member option: ')
        if discount_choice in discount_options:
            discount_percentage = discount_options[discount_choice]
            break
        else:
            print('\nInvalid discount option. Please try again.')

    total_price = 0.0
    for item in shopping_cart:
        subtotal = item['cost'] * item['quant']
        total_price += subtotal

    discount_amount = total_price * discount_percentage
    gst_amount = total_price * 0.08
    payable_amount = total_price - discount_amount + gst_amount

    print('\nBill Statement:')
    for item in shopping_cart:
        subtotal = item['cost'] * item['quant']
        print(f'{item["item"]}: {item["quant"]} x ${item["cost"]:.2f} = ${subtotal:.2f}')
    print(f'Total price before discount: ${total_price:.2f}')
    print(f'Discount: ${discount_amount:.2f}')
    print(f'GST: ${gst_amount:.2f}')
    print(f'Final payable amount: ${payable_amount:.2f}')

    shopping_cart.clear()


category_choice = 0

while True:
    main_menu()
    option = input('\nEnter option: ')
    if option == '1':
        show_all_items()
    elif option == '2':
        cat_menu()
        while True:
            try:
                category_choice = int(input('\nEnter Category to view items: '))
                if 1 <= category_choice <= len(items):
                    it_menu(category_choice)
                    break
                else:
                    print('\nInvalid Category number. Please try again.')
                    continue
            except ValueError:
                print('\nInvalid input. Please enter a number.')
                continue
        try:
            item_choice = int(input('\nEnter Item number to add to cart: '))
            if 1 <= item_choice <= 4:
                quantity = int(input('\nEnter quantity of item(s): '))
                add_to_cart(category_choice, item_choice, quantity)
            else:
                print('\nInvalid input. Please try again.')
        except ValueError:
            print('\nInvalid input. Please enter a number.')
            continue
    elif option == '3':
        cart_disp()
        continue
    elif option == '4':
        search_item()
        continue
    elif option == '5':
        if shopping_cart:
            checkout()
            break
        else:
            print('\nYour shopping cart is empty. Please add items before checking out.')
    else:
        print('\nInvalid input. Please try again.')
