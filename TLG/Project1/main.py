#!/usr/bin/env python3
#Project 1 Using if-else statements

#Declare variables
answer = ""
rating = 0.0

while True:
    name = input("Please enter your name!")
    #checking if name is empty
    if not name: 
        print("Name not valid. Please try again.")
    else:
        break

while True:
    movie = input("Please enter the name of the movie you want to watch!")
    #checking if movie is empty
    if not movie:
        print("Movie name not valid. Please try again.")
    else:
        break

while True:
    try: 
        rating = float(input(f"Hey {name} what is the rating of {movie}?"))
        if rating <= 10:
            break
        else:
            print(f"Hey {name}, IMDB rates the movies on the scale of 1 to 10. That is not a valid rating. Please try again!")
    except ValueError:
        print("Only numbers allowed for ratings. Please try again!")

#if the user inputs the rating greater than 7
if rating > 7:
    print(f"Hey {name}, it seems like a good movie. Do you want to watch {movie}?")

#while loop for the users input from the answer yes or no?
    while True:
        answer = input("Type Y for Yes and N for No")

#if the user answers yes
        if (answer.lower() == "y"):
            print("Awesome, I will make popcorn and the drinks ready")
            break
# if the user answers no
        elif (answer.lower() == "n"):
            print("OK! May be next time")
            break
#if the user answers anything other than yes or no
        else:
            print("Please enter your answer again.")

# if the user inters the ratings greater than 5
elif rating > 5:
    print("The rating is pretty low. I dont think i want to watch this movie")

#if the user inters the rating below 5 
else:
    print(f"{name}, Seems like {movie} is trash.")