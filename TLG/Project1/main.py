#!/usr/bin/env python3
#Project 1 Using if-else statements
answer = ""
name = input("Please enter your name!")
movie = input("Please enter the name of the movie you want to watch!")
rating = float(input(f"Hey {name} what is the rating of {movie}?"))

if rating > 10 :
    print(f"Hey {name}, IMDB rates the movies on the scale of 1 to 10. That is not a valid rating.")

elif rating > 7:
    print(f"Hey {name}, it seems like a good movie. Do you want to watch {movie}?")

    while True:
        answer = input("Type Y for Yes and N for No")

        if (answer == "y"):
            print("Awesome, I will make popcorn and the drinks ready")
            break

        elif (answer == "n"):
            print("OK! May be next time")
            break

        else:
            print("Please enter your answer again.")

elif rating > 5:
    print("The rating is pretty low. I dont think i want to watch this movie")
    
else:
    print(f"{name}, Seems like {movie} is trash.")


