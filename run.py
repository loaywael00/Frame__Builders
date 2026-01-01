from functions import *
user_name = input("Please enter your name")

check = True
while not admin_choise.isdigit():
    admin_choise = int(input("Are you admin or user(1/2)"))

    if admin_choise == 1:
        admin=int(input("data_report(1):read_halls(2):add_movie(3):Movie_xchange(4):swap_halls(5):"))
        if admin==1:
            sales_report()
        elif admin==2:
            print("read halls")
        elif admin==3:
            print("add movie")
        elif admin==4:
            xchange()
        elif admin==5:
            swap()

    elif  admin_choise == 2:
        user=int(input("search_movies(1):schedule_show(2):book_single(3):book_family(4):calculate_price(5):book_snacks(6):book_combo(7):cancel_ticket(8)"))
        if user==1:
            print("search movies")
        elif user==2:
            print("schedule show")
        elif user==3:
            f_chosen_movie,ticket_num = book_single_ticket()
        elif user==4:
            kid_num , kids = book_family_ticket()
        elif user==5:
            Calculate_Price()
        elif user==6:
            book_snacks()
        elif user==7:
            book_combos()
        elif user==8:
            print("cancle ticket")


            cancel_tickets()
            

