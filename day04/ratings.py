# -*- encoding: utf-8 -*-
# 
# looping through dictionaries
# 
# activity 001 of day04
# ----------------------------

# ask ratings for a list of programming languages  and calculate the average rating score

# tuple of bands, we do not change this
languages = ("Java", "C++", "Python", "JavaScript", "PHP", "Assembly language", "Swift", "Ruby", "Visual Basic"
        )

langRatings = {}
numOfLang = len(languages)
counter = 1

for lang in languages:
    s = "(" + str(counter) + "/" + str(numOfLang) + ")"
    print(s + "Rate " + lang + ". (1-9)") 
    rating = input(":")
    # add rating and language to dictionary
    langRatings.update({lang: int(rating)})
    counter = counter + 1

totalRatings = 0
numRatings = 0 

print("\nYour Ratings:")
for lang, rating in langRatings.items():
    print(lang + ": " + str(rating))
    totalRatings = totalRatings + rating
    numRatings = numRatings + 1

avarage = totalRatings / numRatings

print("\nYour avarage rating is a: " + str(avarage))

    
