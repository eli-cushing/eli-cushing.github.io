#Ordinal function adapted from https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers (Answer by Winston Ewert (https://codereview.stackexchange.com/users/1659/winston-ewert) and provided under CC BY-SA 4.0 (https://stackoverflow.com/legal/terms-of-service/public#licensing) license terms (https://creativecommons.org/licenses/by-sa/4.0)
SUFFIX_DICT = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal_suffix(i):
    if len(str(i)) >= 2:
        i = int(str(i)[-2:])
    if 10 < i < 14:
        suffix = 'th'
    else:
        suffix = SUFFIX_DICT.get(i % 10, 'th')
    return suffix
def main():
    user_name = 'World'
    print("Hello " + user_name + "! What's your name?")
    user_name = input('>')
    for counter in range(1,3+1,1):
        print("Hello " + user_name + "! Nice to meet you. You seem to be the " + str(counter) + ordinal_suffix(counter) + " person I've met so far. Is anyone else there?")
        user_name = input('>')
    print("Hello " + user_name + "! Well, it's nice to have met you all but I'm going to rest now. Goodbye.")
if __name__ == '__main__':
    main()
