import random
subjects = ["Fahad Musrtafa" ,
            "Ali Khan" ,
            "John Doe" ,
            "Jane Smith" ,
            "Elon Musk" ,
            "Bill Gates"]
actions = ["buys" ,
           "sells" ,
           "donates" ,
           "steals" ,
           "launches" ,
           "destroys"]
places_or_things = ["a new startup" ,
                    "a spaceship" ,
                    "a charity" ,
                    "a secret project" ,
                    "a luxury car" ,
                    "a controversial invention"]  
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f" BREAKING NEWS:{subject} {action} {place_or_thing}!"
    print("\n" + headline)
    
    user_input = input("\nDo you want to generate another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
    
print("\nThank you for using the Fake News Headline Generator, Have a great day!")