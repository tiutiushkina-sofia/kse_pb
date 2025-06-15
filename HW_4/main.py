import random

def calculate_status(guess_word, correct_word, correct_length):
    statuses=[]
    index = 0
    while index < correct_length:
        character = guess_word[index]
        if character == correct_word[index]:
            statuses.append('correct')
        elif character in correct_word:
            statuses.append('present')
        else:
            statuses.append('absent')
        index += 1
    return statuses

def build_display(guess_word, correct_word, correct_length):
    statuses = calculate_status(guess_word, correct_word, correct_length)
    display = []
    index = 0
    while index < correct_length:
        character = guess_word[index]
        status = statuses[index]
        if status == 'correct':
            display.append("["+character.upper()+"]")
        elif status == 'present':
            display.append("("+character+")")
        else:
            display.append(" "+character+" ")
        index+=1
    return display


def input_word(tries_more, correct_length):
    guess_word = input("Attempt "+str(7 - tries_more)+"/6 – Enter guess: ").lower()
    if not guess_word.isalpha():
        print("Please, enter only letters")
        return False
    if len(guess_word) != correct_length:
        print("Wrong length. Expected", correct_length)
        return False
    return guess_word

def on_win():
    print("You win!!!")

def on_lose(correct_word):
    print("You lose! The word was:", correct_word)

def start_of_game(correct_length, tries): 
    print("Welcome to Wordle!")
    print("Guess the",correct_length,"-letter word. You have", tries, "tries.")

def display(display_info):
        print("Result: ", ' '.join(display_info))

def generate_word(word_list):
    secret_word = random.choice(word_list)
    return secret_word

def game(tries, word_list):
    correct_word = generate_word(word_list)
    correct_length = len(correct_word)
    start_of_game(correct_length, tries)
    while tries != 0:
        guess_word = input_word(tries, correct_length)
        if guess_word==False:
            continue
        if guess_word==correct_word:
            on_win()
            break
        display_info = build_display(guess_word, correct_word, correct_length)
        display(display_info)
        tries = tries - 1
    else:
        on_lose(correct_word)

def main():
    max_tries = 6
    possible_secret_words = ['apple', 'bread','candy', 'dream','eagle','flame','grape','house','input','joker']
    while True:
        game(max_tries, possible_secret_words)
        more_games = input("Do you want to play more games(\"Yes\" for yes, anything else for no)")
        if more_games != "Yes":
            break
main()

#у цьому коді переробила структуру використовуючи функції замість суцільного полотна коду. 
#функції відповідають за окремі найменші підзадачі.
#виклик функій одна в одній допоміг зробити код знічно більш читабельним
#з загального - змінила рандомний вибір слова, додала перевірку на введення лише літер, додала головний цикл гри що дозволяє грати багато раундів.
#також прибрала жахливий неймінг та повторювані частини