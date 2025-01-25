user_name = 'World'
print("Hello " + user_name + "! What's your name?")
user_name = input('>')
for counter in range(1,3 + 1, 1):
    print("Hello " + user_name + "! Nice to meet you. You seem to be the " + str(counter) + " person I've met so far. Is anyone else there?")
    user_name = input('>')
print("Hello " + user_name + "! Well, it's nice to have met you all but I'm going to rest now. Goodbye.")
