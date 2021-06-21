# this is a short and simple word guessing game i made for a friend/
# if you are using this just change the secret_word and the clues so if fits for your needs
secret_word = "crime design"
guess = ""
hint = 0
hint_limit = 4
you_win =False
guess_count = 0
guess_limit = 4
you_lose = False
while guess != secret_word and not(you_lose) and not(you_win):
    if guess_count < guess_limit and hint < hint_limit:
        guess = input("enter your guess: ")
        if guess == secret_word:
            you_win= True
            if you_win == True:
                print("You Win!!!")
        else:
            guess_count += 1
            hint += 1
        if hint == 1 and not(you_lose) and not(you_win):
            print("heres a clue: it was a great idea")
        elif hint == 2 and not(you_lose) and not(you_win):
            print("heres a clue: it will be a real thing")
        elif hint == 3 and not(you_lose) and not(you_win):
            print("last clue: Alex hates it")
    else:
        you_lose = True
        print("You Failed!")



