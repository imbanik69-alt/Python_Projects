import random

subjects = [
    "Sharuk Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "Prime Minister Modi Ji",
    "Godi Media",
    "Chaiwala from Delhi",
    "Auto Rickshaw Driver",
    "A Mumbai Cat",
    "Amit Shah"
]

actions = [
    "launches",
    "gareebi dekhi hain",
    "Cancels",
    "dances with",
    "eats and drinks",
    "declares war on",
    "orders",
    "celebrates",
    "say's kantap maribe in"
]

places = [
    "London mein",
    "Dharamshala",
    "Guwahati chall",
    "Chai ki dukaan",
    "Modi ka mandir"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS : {subject} {action} {place}"
    print("\n" + headline)

    userinput = input("\nDo you want another headline? (YES/NO) ").strip()

    if userinput.lower() == "no":
        break