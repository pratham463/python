import pandas as pd, sys
from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)

try:
    df = pd.read_csv('imbd_top_1000.csv')
    df['combined'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
except FileNotFoundError:
    print(Fore.RED + "File not found")
    sys.exit()

# Extract unique genres
genres = sorted({g.strip() for x in df['Genre'].dropna() for g in x.split(',')})

def recommend(genre=None, mood=None, rating=0, top=5):
    data = df.copy()
    
    if genre:
        data = data[data['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        data = data[data['imdb_top_100.csv'] >= rating]
    
    recs = []
    for _, r in data.sample(frac=1).iterrows():
        polarity = TextBlob(r['Overview']).sentiment.polarity
        if not mood or TextBlob(mood).sentiment.polarity * polarity >= 0:
            recs.append((r['Series_Title'], round(polarity, 2)))
        if len(recs) >= top:
            break
    
    return recs or [("No match found", 0)]

print(Fore.BLUE + "🎬 AI Movie Recommender 🎬")
name = input(Fore.YELLOW + "Your name: ")

print(Fore.CYAN + f"Hello {name}! Here are some options:")
print(Fore.GREEN + f"Available genres: {', '.join(genres[:10])} ...")  # show first 10

genre = input(Fore.YELLOW + "Enter a genre you like (or leave blank): ")
mood = input(Fore.YELLOW + "Describe your mood (happy, sad, excited, etc.): ")
rating = input(Fore.YELLOW + "Minimum IMDb rating (or leave blank): ")

try:
    rating = float(rating) if rating else 0
except ValueError:
    rating = 0

recommendations = recommend(genre, mood, rating)

print(Fore.MAGENTA + "\nTop Recommendations:")
for title, sentiment in recommendations:
    print(Fore.WHITE + f"🎥 {title} (Sentiment: {sentiment})")