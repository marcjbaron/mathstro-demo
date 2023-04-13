name = input("What is your name?")
quest = input("What is your quest?")
airspeed = input("What is the air-speed velocity of an unladen swallow?")


if ("african" in airspeed.lower()) & ("european" in airspeed.lower()): 
    print("I...don't know. \n*I have been thrown off the bridge*")
else:
    print("*You have been thrown off the bridge*")