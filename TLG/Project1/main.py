#!/usr/bin/env python3
#Project 1 Using if-else statements

#Declare variables
answer = ""
name = input("Please enter your name!")
movie = input("Please enter the name of the movie you want to watch!")
rating = float(input(f"Hey {name} what is the rating of {movie}?"))

#if the user inputs the rating greater than 10
if rating > 10 :
    print(f"Hey {name}, IMDB rates the movies on the scale of 1 to 10. That is not a valid rating.")

#if the user inputs the rating greater than 7
elif rating > 7:
    print(f"Hey {name}, it seems like a good movie. Do you want to watch {movie}?")

#while loop for the users input from the answer yes or no?
    while True:
        answer = input("Type Y for Yes and N for No")

#if the user answers yes
        if (answer == "y"):
            print("Awesome, I will make popcorn and the drinks ready")
            break

# if the user answers no
        elif (answer == "n"):
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


