#Defining the main calling function in order to start the script
def main():
    about_me = {
        "Student_Name": "Mridul Gogia",
        "Student_ID": 10273459,
        "pizza_toppings": ["Chicken", "onions", "Pepperoni"],
        "Movies": [
            {
                "Title": "Interstellar",
                "Genre": "SciFi"
            },
            {
                "Title": "Breaking Bad",
                "Genre": ["Drama", "Action"]
            }
        ]
    }
    return about_me

    
 # A calling function is being used here in order to 
def Calling(details, New_Movie, about_me):
    New_Movie = {"Title": "Ford Vs Ferrari", "Genre": ["Sports"]}
    about_me["Movies"].append(New_Movie)

# Used the printing information function to define details about the user.
def printing_information(details):
    name = details["Student_Name"]
    id = details["Student_ID"]
    print(f"My name is {name}. But You can surely call me Lord {name.rsplit(' ', 1)[0]}."
          f" My student ID is {id}")

# Added a new pizza topping in the data structure using the function
def added_new_pizza_topping(details, new_topping):
    details["pizza_toppings"].append(new_topping)
    for i, topping in enumerate(details["pizza_toppings"]):
        details["pizza_toppings"][i] = topping.lower()
    details["pizza_toppings"].sort()


#Defining a function for the comment, fav pizza topping using for loop statement.
def pizza_toppings(details):
    print("My favorite pizza toppings are:")
    for topping in details["pizza_toppings"]:
        print(f"- {topping}")
    print()


#Movie genres function has been created using the function in the data structure.
def movie_genres(details):
    print("My go-to movie genres are :", end="", )
    genres = []
    for movie in details["Movies"]:
        genres.extend(movie["Genre"])
    print(",".join( genres))
    print()

#Function has been added to the data structures to list the movie titles in a print statement.
def movie_titles(details):
    print("My favorite movie titles are:", end="")
    titles = [movie["Title"] for movie in details["Movies"]]
    print(", ".join(titles), end=".",)
    print()

details = main()
Calling(details, "Pepper", details)
printing_information(details)
added_new_pizza_topping(details, "Pizza seasoning")
pizza_toppings(details)
movie_genres(details)
movie_titles(details)