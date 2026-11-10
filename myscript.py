def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    print(f"Word count: {word_count}")
    print(f"Character count: {char_count}")
    return word_count, char_count

if __name__ == "__main__":
    sample = "Hello, this is my active portfolio project for software engineering."
    analyze_text(sample)
