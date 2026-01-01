# Seif
import json
def book_snacks():
    items = [
        ("Popcorn Small", 80),
        ("Popcorn Large", 110),
        ("Nachos", 95),
        ("Fries", 50),
        ("Hot Dog", 85),
        ("Burger", 120),
        ("Pizza Slice", 90),
        ("Pepsi", 40),
        ("Red bull", 90),
        ("Water", 25),
        ("Chocolate", 35),
        ("Ice Cream", 45)
    ]
    print("_snacks list_")
    for i in range(len(items)):
        name, price = items[i]
        print(f"{i+1}_{name}_{price} LE")
    print("0_finish and print receipt")
    cart={}
    while True:
        pick_item=int(input('enter item num:__(0 to finish)'))
        if pick_item == 0:
            break
        elif pick_item >= 1 and pick_item <= len(items):
            index = pick_item - 1
            item_name, item_price = items[index]
            quantity_text = int(input(f"Enter quantity for {item_name}: "))
            if quantity_text > 0:
                # to add items on cart
                cart[item_name] = cart.get(item_name, 0) + quantity_text
                print(f"Added {quantity_text} x {item_name}.")
            else:
                print("Quantity must be greater than 0")
        else:
            print("sorry, out of the range")
    print("\n_Receipt_")
    if len(cart) == 0:
        print("No items selected.")
        print("Total: 0 LE")
        return 0
    total = 0
    for i in range(len(items)):
        name, price = items[i]
        if name in cart:
            quantity_text = cart[name]
            line_total = price * quantity_text
            total += line_total
            print(f"- {name}: {quantity_text} x {price} = {line_total} LE")
    print(f"\nTotal: {total} LE")
    return total

def book_combos():
    combos = [
        ("Pepsi + Fries", 60, 90),        # بدل 90 _ 60
        ("2x Popcorn", 170, 200),         # بدل 200 _ 170
        ("Burger + Pepsi", 140, 160),     # بدل 160 _ 140
        ("Pizza Slice + Pepsi", 120, 130),# بدل 130 _ 120
        ("Hot Dog + Fries", 120, 135)     # بدل 135 _ 120
    ]
    print("_Cinema Combos Menu_")
    for i in range(len(combos)):
        name, discount_price, normal_price = combos[i]
        print(f"{i+1}_ {name} _ {discount_price} LE (instead of {normal_price} LE)")
    print("0_Finish and print receipt")
    cart = {}
    while True:
        combo_item=int(input('enter combo num:__(0 to finish)'))
        if combo_item == 0:
            break
        elif combo_item >= 1 and combo_item <= len(combos):
            index = combo_item - 1
            combo_name, discount_price, normal_price = combos[index]
            quantity_text = int(input(f"Enter quantity for {combo_name}: "))
            if quantity_text > 0:
                # to add combo on cart
                cart[combo_name] = cart.get(combo_name, 0) + quantity_text
                print(f"Added {quantity_text} x {combo_name}.")
            else:
                print("Quantity must be greater than 0")
        else:
            print("sorry, out of the range")

    print("\n_Receipt_")
    if len(cart) == 0:
        print("No items selected.")
        print("Total: 0 LE")
        return 0
    total = 0
    for i in range(len(combos)):
        name, discount_price, normal_price = combos[i]
        if name in cart:
            quantity_text = cart[name]
            line_total = discount_price * quantity_text
            total += line_total
            print(f"- {name}: {quantity_text} x {discount_price} = {line_total} LE")
    print(f"\nTotal: {total} LE")
    return total

def sales_report():
    print("\n Ticket Summary:\n")
    with open('movies.json', 'r', encoding='utf-8') as file:
        movies = json.load(file)
    for movie in movies["movies"]:
        print(movie["title"])
        print("s-tickets:", movie["s-tickets"])
        print("revenue =", movie["s-tickets"]*200)
        print("f-tickets:", movie["f-tickets"])
        print("revenue =", movie["f-tickets"]*160)
        print("_")

def swap():
    with open("movies.json", "r", encoding="utf-8") as file:
        movies = json.load(file)["movies"]
    #     Lower revenues from the 3 big halls
    first_three = movies[:3]
    min_first = min(first_three, key=lambda m: m["s-tickets"] + m["f-tickets"])
    min_first_total = min_first["s-tickets"] + min_first["f-tickets"]
    #   Highest revenues from the 2 small halls
    next_two = movies[3:5]
    max_next = max(next_two, key=lambda m: m["s-tickets"] + m["f-tickets"])
    max_next_total = max_next["s-tickets"] + max_next["f-tickets"]
    # Print values of 2 chooosen halls
    print(min_first["title"])
    print("s-tickets:", min_first["s-tickets"])
    print("f-tickets:", min_first["f-tickets"])
    print("total:", min_first_total)
    print("___")
    print(max_next["title"])
    print("s-tickets:", max_next["s-tickets"])
    print("f-tickets:", max_next["f-tickets"])
    print("total:", max_next_total)
    print("___")
    if min_first_total < max_next_total:
        print("We will exchange films.")
    else:
        print("No exchange.")

def assign_halls():
    with open("movies.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    #     Replacing film
    index = int(input("Enter movie number to replace (1 to 5): ")) - 1
    # Get inputs from admin
    print(" Enter new movie details:")
    title = input("Title: ")
    genre = input("Genre: ")
    duration = int(input("Duration (minutes): "))
    rating = float(input("Rating: "))
    price = int(input("Price: "))
    s_tickets = int(input("Single Tickets: "))
    f_tickets = int(input("Family Tickets: "))
    hall_id = int(input("Hall ID: "))
    hall_name = input("Hall Name: ")
    seats = int(input("Seats: "))
    # Import or save this data
    new_movie = {
        "title": title,
        "genre": genre,
        "duration": duration,
        "rating": rating,
        "price": price,
        "s-tickets": s_tickets,
        "f-tickets": f_tickets,
        "id": hall_id,
        "name": hall_name,
        "seats": seats
    }
    # Replacing in right place
    data["movies"][index] = new_movie
    # Save changes in json file
    with open("movies.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("\n Movie replaced successfully")
