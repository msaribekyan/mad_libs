### Mad Libs
### Story generator

import random

# Print possible stories
print("\n")
print("Mad Libs")
print("Story generator")

print("\n")
print("Story 1\n")
print("It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) ! ")

print("\n")
print("Story 2\n")
print("This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!")

print("\n")
print("Story 3\n")
print("Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!")
print("\n")

# Select story
while True:
    input_text = input("Select story [1,2,3 or 4 (random)]: ")
    if input_text in ["1","2","3","4"]:
        story = input_text
        break
    print("Invalid input, try again")

if story == "4":
    story = random.choice(["1", "2", "3"])

print("Selected story: ", story)

# Generate story
if story == "1":
    
    number = input("Input a number: ")
    time = input("Input a measure of time: ")
    transport = input("Input a mode of transportation: ")
    adjective = input("Input an adjective: ")
    adjective2 = input("Input an adjective: ")
    noun = input("Input a noun: ")
    color = input("Input a color: ")
    part = input("Input a part of body: ")
    verb = input("Input a verb: ")
    number2 = input("Input a number: ")
    noun2 = input("Input a noun: ")
    noun3 = input("Input a noun: ")
    part2 = input("Input a part of body: ")
    verb2 = input("Input a verb: ")
    noun4 = input("Input a noun: ")
    adjective3 = input("Input an adjective: ")
    silly = input("Input a silly word: ")
    noun5 = input("Input a noun: ")

    print("It was about " + number + " " + time + " ago when I arrived at the hospital in a " + transport + ". The hospital is a/an " + adjective + " place, there are a lot of " + adjective2 + " " + noun + " here. There are nurses here who have " + color + " " + part + ". If someone wants to come into my room I told them that they have to " + verb + " first. I’ve decorated my room with " + number2 + " " + noun2 + ". Today I talked to a doctor and they were wearing a ", noun3, " on their ", part2, ". I heard that all doctors " + verb2 + " " + noun4 + "  every day for breakfast. The most " + adjective3 + " thing about being in the hospital is the " + silly + " " + noun5 + "!")

elif story == "2":

    name = input("Input a person's name: ")
    noun = input("Input a noun: ")
    feeling = input("Input a feeling: ")
    verb = input("Input a verb: ")
    feeling2 = input("Input a feeling: ")
    animal = input("Input an animal: ")
    verb2 = input("Input a verb: ")
    color = input("Input a color: ")
    verbing = input("Input a verb (ending in ing): ")
    adverb = input("Input an adverb (ending in ly): ")
    number = input("Input a number: ")
    time = input("Input a measure of time: ")
    color2 = input("Input a color: ")
    animal2 = input("Input an animal: ")
    number2 = input("Input a number: ")
    silly = input("Input a silly word: ")
    noun2 = input("Input a noun: ")

    print("This weekend I am going camping with " + name + ". I packed my lantern, sleeping bag, and " + noun + ". I am so " + feeling + " to " + verb + " in a tent. I am " + feeling2 + " we might see a(n) " + animal + ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and " + verb2 + ". I have heard that the " + color + " lake is great for " + verbing + ". Then we will " + adverb + " hike through the forest for " + number + " " + time + ". If I see a " + color2 + " " + animal2 + " while hiking, I am going to bring it home as a pet! At night we will tell " + number2 + " " + silly + " stories and roast " + noun2 + " around the campfire!!")

elif story == "3":

    name = input("Input a person's name: ")
    adjective = input("Input an adjective: ")
    color = input("Input a color: ")
    animal = input("Input a animal: ")
    place = input("Input a place: ")
    adjective2 = input("Input an adjective: ")
    creature = input("Input a magical creature (plural): ")
    adjective3 = input("Input an adjective: ")
    creature2 = input("Input a magical creature (plural): ")
    room = input("Input a room in a house: ")
    noun = input("Input a noun: ")
    noun2 = input("Input a noun: ")
    noun3 = input("Input a noun (plural): ")
    adjective4 = input("Input an adjective: ")
    noun4 = input("Input a noun (plural): ")
    number = input("Input a number: ")
    time = input("Input a measure of time: ")
    verb = input("Input a verb (ending in ing): ")
    adjective5 = input("Input an adjective: ")
    noun5 = input("Input a noun: ")
    print("Dear " + name + ", I am writing to you from a " + adjective + " castle in an enchanted forest. I found myself here one day after going for a ride on a " + color + " " + animal + " in " + place + ". There are " + adjective2 + " " + creature + " and " + adjective3 + " " + creature2 + " here! In the " + room + " there is a pool full of " + noun + ". I fall asleep each night on a " + noun2 + " of " + noun3 + " and dream of " + adjective4 + " " + noun4 + ". It feels as though I have lived here for " + number + " " + time + ". I hope one day you can visit, although the only way to get here now is " + verb + " on a " + adjective5 + " " + noun5 + "!!")

else:

    print("Something went wrong, exiting.")



