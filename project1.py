import json

def read_movies():
   with open("movies.json") as f:
    data= json.load(f)
   for movie in data["movies"]:
      print(movie)
read_movies()

def read_halls():
        with open("halls.json", "r") as y:
            data = json.load(y)
            for hall in data:
                print(hall)

read_halls()
def search_movie():
    print("choose search method:")
    print("1.  title")
    print("2.  genre")
    print("3.  rating")

    choice=input("enter your choice (1/2/3): ")
    with open("movies.json", "r") as f:
        data = json.load(f)
        movies = data["movies"]

    matching = []

    if choice == "1":
        keyword = input("enter the movie title or part of it: ").lower()
        for movie in movies:
            if keyword in movie["title"].lower():
                matching.append(movie)

    elif choice == "2":
        genre = input(" Enter the movie genre: ").lower()
        for movie in movies:
            if genre in movie["genre"].lower():
                matching.append(movie)

    elif choice == "3":
        try:
            rating = float(input(" enter the minimum rating: "))
            for movie in movies:
                if movie["rating"] >= rating:
                    matching.append(movie)
        except ValueError:
            print("rating must be a number")
            return None
    else:
        print("invalid choice")
        return None
    if matching:
        print("matching movies:")
        i = 1
        for movie in matching:
            print(f"{i}. {movie['title']} | genre: {movie['genre']} | duration: {movie['duration']} mins | rating: {movie['rating']}")
            i += 1

search_movie()




def add_movie():
    with open("movies.json", "r", ) as file:
        data = json.load(file)

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

    data["movies"].append(new_movie)

    with open("movies.json", "w") as file:
        json.dump(data, file, indent=2)

    print(f"Movie '{title}' added successfully!")

add_movie()
print('you have added the new movie successfully!:')








