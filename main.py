def show_movies(title, movie_list):
    print(f"\n{title}\n")

    for movie in movie_list:
        print("⭐", movie)

    print("\n❤️ Thank you for using Movie Recommendation System!")
    print("=" * 50)


print("=" * 50)
print("🎬 Welcome to Movie Recommendation System 🎬")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nWelcome, {name}! 👋")

print("\n========== Choose Movie Genre ==========")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Sci-Fi")
print("5. Romance")
print("6. Thriller")

choice = int(input("\nEnter your choice: "))

action_movies = [
    "John Wick",
    "Mad Max: Fury Road",
    "The Dark Knight",
    "Mission Impossible",
    "Avengers: Endgame"
]

comedy_movies = [
    "The Hangover",
    "Free Guy",
    "Central Intelligence",
    "Jumanji",
    "Rush Hour"
]

horror_movies = [
    "The Conjuring",
    "Annabelle",
    "Insidious",
    "IT",
    "The Nun"
]

scifi_movies = [
    "Interstellar",
    "Inception",
    "The Matrix",
    "Avatar",
    "Dune"
]

romance_movies = [
    "Titanic",
    "The Notebook",
    "La La Land",
    "Me Before You",
    "The Fault in Our Stars"
]

thriller_movies = [
    "Se7en",
    "Gone Girl",
    "Shutter Island",
    "Prisoners",
    "The Silence of the Lambs"
]

if choice == 1:
    show_movies("🔥 Recommended Action Movies", action_movies)

elif choice == 2:
    show_movies("😂 Recommended Comedy Movies", comedy_movies)

elif choice == 3:
    show_movies("👻 Recommended Horror Movies", horror_movies)

elif choice == 4:
    show_movies("🚀 Recommended Sci-Fi Movies", scifi_movies)

elif choice == 5:
    show_movies("❤️ Recommended Romance Movies", romance_movies)

elif choice == 6:
    show_movies("🔪 Recommended Thriller Movies", thriller_movies)

else:
    print("\n❌ Invalid Choice!")
    print("Please restart the program and choose a number between 1 and 6.")