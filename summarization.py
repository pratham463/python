from colorama import Fore, Style, init
import string
init(autoreset=True)
STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "on", "for", "with",
    "that", "this", "it", "as", "are", "was", "were", "be", "by",
    "an", "or", "from", "at", "which", "but", "has", "have", "had"
}
def summarize_text(text, sentence_limit):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    word_freq = {}
    for sentence in sentences:
        words=sentences.lower().split
        for word in words:
            word = word.strip(string.punctuation)
            if word and word not in STOPWORDS:
                word_freq[word] = word_freq.get(word, 0) + 1
    sentence_scores = {}

    for sentence in sentences:
        score = 0
        words = sentence.lower().split()
        for word in words:
            word = word.strip(string.punctuation)
            score += word_freq.get(word, 0)
        sentence_scores[sentence] = score

    ranked_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )
    summary = ranked_sentences[:sentence_limit]

    return ". ".join(summary) + "."

if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "👋 Hi! Welcome to Text Summarizer")

    text = input(Fore.CYAN + "\nEnter text to summarize:\n").strip()

    if not text:
        print(Fore.RED + "❌ No text provided.")
    exit()

print(Fore.YELLOW + "\nChoose summary type:")
print("1. Short Summary")
print("2. Detailed Summary")
choice = input("Enter 1 or 2: ").strip()

if choice == "2":
    sentences = 5
    print(Fore.BLUE + "Generating detailed summary...\n")
else:
    sentences = 3
    print(Fore.BLUE + "Generating short summary...\n")

summary = summarize_text(text, sentences)
print(Fore.GREEN + Style.BRIGHT + "✅ SUMMARY:\n")
print(summary)