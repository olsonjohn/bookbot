
# creating a function to count the number of each character and return that in a dictionary
def count_char(text):
    results = []
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for key,value in char_count.items():
        if key.isalpha():
            results.append({'char': key, 'count': value})
    return results


def count_words(text):
    words = text.split()
    return len(words)

def create_report(text):
    print("--- Begin text analysis ---")
    print(f"Number of words: {count_words(text)}")
    chars = count_char(text.lower())
    chars.sort(key=lambda x: x['count'], reverse=True)
    for char in chars:
        print(f"Char: {char['char']} Count: {char['count']}")
    print("--- End text analysis ---")
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        create_report(file_contents)

main()