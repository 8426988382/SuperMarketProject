from utils.offer import Offer
from utils.inventory import Inventory
from typing import List

'''
TODO: 
1. regex validation
2. add offer for the products that does not exists 

'''

MENU_PROMPT = """
Press 
1 => Add To Inventory
2 => Sale
3 => Stock Check
4 => Add New Offer
5 => Quit
for proceeding: 
"""

INVENTORY_TEMPLATE = '''ProductId|ProductName|Quantity|Price-Per-Quantity'''
STOCK_TEMPLATE = '''Product ID'''
SALES_TEMPLATE = '''ProductId|Quantity;ProductId|Quantity'''
OFFER_TEMPLATE = '''BuyXMore|OFFER-ID|Product-ID|Minimum-Quantity|Discount-Percentage'''

inventory: List[Inventory] = []


def add_inventory() -> None:
    print("Please provide details as follows. ")
    invents = input(f'INVENTORY=>{INVENTORY_TEMPLATE}: ').split('|')

    try:
        product_id = int(invents[0])
        product_name = invents[1]
        product_quantity = int(invents[2])
        product_price = int(invents[3])
        new_inventory = Inventory(
            product_id=product_id,
            product_name=product_name,
            product_quantity=product_quantity,
            price_per_quantity=product_price,
            offers=Offer(product_id)
        )

        for invent in inventory:
            if product_id == invent.product_id:
                inventory.remove(invent)
                break
        inventory.append(new_inventory)

    except (ValueError, TypeError, IndexError):
        print("Bad Input")

    else:
        print('Inventory Updated.')


def sale() -> None:
    print("Please provide details as follows. ")
    sales = input(f'SALE=>{SALES_TEMPLATE}: ').split(';')
    sales_product = []
    stock_out = False
    for product in sales:
        product_id, product_quantity = product.split('|')

        for invent in inventory:
            if str(invent.product_id) == product_id:
                if int(product_quantity) <= invent.product_quantity:
                    print("yes product is available")
                    offer_id = None
                    discount_percentage = None

                    if len(invent.offer.offers) != 0:
                        print("there are some offers")
                        print(invent.offer.offers)

                    net = invent.price_per_quantity * int(product_quantity)

                    sales_product.append(
                        {
                            "product_id": invent.product_id,
                            "product_name": invent.product_name,
                            "quantity_purchased": product_quantity,
                            "product_price": invent.price_per_quantity,
                            "offer_id": offer_id,
                            "net": net
                        }
                    )
                    invent.product_quantity = invent.product_quantity - int(product_quantity)
                else:
                    print(f'Product with product id {product_id} is not in stock')
                    stock_out = True
                    break
        if stock_out:
            break
    else:
        print("order successful")
        print('== Bill ==')
        for product in sales:
            print(product)


def stock_check() -> None:
    print('Please provide details as follows: ')
    user_input = int(input(f'STOCK=> {STOCK_TEMPLATE}: '))

    for invent in inventory:
        if user_input == invent.product_id:
            print(f'{invent.product_name} - {invent.product_quantity}')
            break
    else:
        print(f'No such product with {user_input} id')


def add_new_offer() -> None:
    print("Please provide details as follows. ")
    offer_details = input(f'NEW-OFFER=>{OFFER_TEMPLATE}: ').split('|')
    '''BuyXMore | OFFER - ID | Product - ID | Minimum - Quantity | Discount - Percentage'''
    offer_name = offer_details[0]
    offer_id = offer_details[1]
    product_id = offer_details[2]
    minimum_quantity = offer_details[3]
    discount_percent = offer_details[4]

    new_offer = {
        "product_id": product_id,
        "offer_id": offer_id,
        "offer_name": offer_name,
        "minimum_quantity": minimum_quantity,
        "discount_percent": discount_percent
    }

    for invent in inventory:
        if str(invent.product_id) == product_id:
            invent.offer.add_offer(new_offer)
            break
    else:
        print(f'No Product with {product_id} id is present')


selected_choice = {
    "1": add_inventory,
    "2": sale,
    "3": stock_check,
    "4": add_new_offer
}


def menu() -> None:
    selection = input(MENU_PROMPT)

    while selection != '5':
        print("Current Items Details in Inventory:")
        for invent in inventory:
            print(invent)
        if selection in selected_choice:
            selected_function = selected_choice[selection]
            selected_function()
        else:
            print("Unknown Input, Please select a valid option")

        selection = input(MENU_PROMPT)


menu()
