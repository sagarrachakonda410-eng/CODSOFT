movies = {
    "action": ["Avengers", "John Wick", "RRR"],
    "comedy": ["Jathi Ratnalu", "DJ Tillu", "F2"],
    "horror": ["The Conjuring", "Annabelle", "The Nun"],
    "romance": ["Hi Nanna", "Sita Ramam", "Geetha Govindam"]
}

print("=== Movie Recommendation System ===")
print("Available genres: action, comedy, horror, romance")

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Sorry! Genre not found.")