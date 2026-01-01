from functions import *
user_name = input("Please enter your name")

check = True
while not admin_choise.isdigit():
    admin_choise = int(input("Are you admin or user(1/2)"))

    if admin_choise == 1:
        admin=int(input("data_report(1):read_halls(2):add_movie(3):Movie_xchange(4):swap_halls(5):"))
        if admin==1:

        elif admin==2:
            print("read halls")
        elif admin==3:
            print("add movie")
        elif admin==4:

    elif  admin_choise == 2:
        user=int(input("search_movies(1):schedule_show(2):book_single(3):book_family(4):calculate_price(5):book_snacks(6):book_combo(7):cancel_ticket(8)"))
        if user==1:
            print("search movies")
        elif user==2:
            print("schedule show")
        elif user==3:

