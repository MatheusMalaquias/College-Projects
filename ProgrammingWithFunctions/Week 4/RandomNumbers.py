import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    print(f'Numbers: {numbers_list}')

    append_random_numbers(numbers_list)
    print(f'Numbers: {numbers_list}')

    append_random_numbers(numbers_list, 3)
    print(f'Numbers: {numbers_list}')

    words = []

    append_random_words(words, 6)
    print(f'words: {words}')


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity=1):
    candidates = ['arm', 'car', 'cloud', 'head', 'heal', 'hydrogen', 'jog', 'join', 'laugh', 'love', 'sleep', 'smile', 'speak', 'sunshine', 'toothbrush', 'tree', 'truth', 'walk', 'water']

    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)

if __name__ == "__main__":
    main()