def count_vowels(word):
    """Counts the occurrences of each vowel in a given word.

    Args:
        word: The word to analyze.

    Returns:
        A dictionary containing the vowel counts.
    """

    vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in word:
        if char in vowel_counts:
            vowel_counts[char] += 1

    return vowel_counts

def main():
    name = input("Hello! What's your name? ").capitalize()
    print(f"Hi {name}! This is a vowel detector program.\n"
          f"Type in a word or a phrase and let's check how many vowels it has!\n")

    while True:
        word = input("Enter a word: ")

        vowel_counts = count_vowels(word)

        print(f"There are {sum(vowel_counts.values())} vowels in '{word}'.")

        for vowel, count in vowel_counts.items():
            if count > 0:
                print(f"'{vowel}' is present {count} times in your word.")

        again = input("\nDo you want to enter another word? (y/n) ").lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
