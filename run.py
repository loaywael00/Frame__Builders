from HallManagementloay import *
from MovieManagementahmed import *
from Ticketingseif import *
user_name = input("Please enter your name")

check = True
while not admin_choise.isdigit():
    admin_choise = int(input("Are you admin or user(1/2)"))
    if admin_choise == 1:
        pass
    elif  admin_choise == 2:
        while not admin_choise.isdigit():
            user_chiose = int(input("Do you want family or single ticket(1/2)"))
            if user_chiose == 1:
                f_chosen_movie,ticket_num = book_single_ticket()
            elif user_chiose == 2:
                kid_num , kids = book_family_ticket()
            else:
                print("wrong input please choose (1/2)")
            combo = input("Do you want combo?(y/n)").lower()
            while combo !="y" or combo != "n":
                combo = input("please choose (y/n)").lower()
            if combo == "y":
                combo_total = book_combos()
            snacks = input("Do you want snacks?(y/n)").lower()
            while snacks !="y" or snacks != "n":
                combo = input("please choose (y/n)").lower()
            if combo == "y":
                snacks_total = book_snacks()

    else:
        print("wrong input please choose (1/2)")
