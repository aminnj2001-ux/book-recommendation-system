"""
A simple content-based book recommender.
This is a baseline demonstration using a small illustrative catalog.
"""

BOOKS = [
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "genres": ["fantasy", "adventure"],
        "description": "A hobbit joins a quest involving a dragon and a lost treasure."
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genres": ["classic", "romance"],
        "description": "A novel about relationships, first impressions, and social expectations."
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genres": ["science fiction", "adventure"],
        "description": "Political conflict and survival on a desert planet."
    },
    {
        "title": "The Martian",
        "author": "Andy Weir",
        "genres": ["science fiction", "adventure"],
        "description": "An astronaut uses science and engineering to survive on Mars."
    },
    {
        "title": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genres": ["mystery", "crime"],
        "description": "A detective investigates a murder aboard a train."
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genres": ["self-help", "personal development"],
        "description": "Practical strategies for building habits and improving routines."
    },
    {
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "genres": ["history", "nonfiction"],
        "description": "A broad overview of human history and the development of societies."
    },
    {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupery",
        "genres": ["classic", "philosophy"],
        "description": "A poetic story about friendship, meaning, and seeing beyond appearances."
    },
]


def recommend_books(preferred_genres, keywords=None, read_books=None, top_k=5):
    """Return books ranked by a simple content-match score."""
    preferred_genres = {g.strip().lower() for g in (preferred_genres or []) if g.strip()}
    keywords = {word.strip().lower() for word in (keywords or []) if word.strip()}
    read_books = {title.strip().lower() for title in (read_books or []) if title.strip()}

    if top_k <= 0:
        return []

    ranked = []
    for book in BOOKS:
        if book["title"].lower() in read_books:
            continue

        book_genres = {genre.lower() for genre in book["genres"]}
        searchable_text = " ".join(
            [book["title"], book["author"], book["description"], *book["genres"]]
        ).lower()

        genre_score = sum(1 for genre in preferred_genres if genre in book_genres)
        keyword_score = sum(1 for keyword in keywords if keyword in searchable_text)
        score = (2 * genre_score) + keyword_score

        if score > 0:
            ranked.append((score, book))

    ranked.sort(key=lambda item: (-item[0], item[1]["title"].lower()))
    return [
        {**book, "score": score}
        for score, book in ranked[:top_k]
    ]


def main():
    print("=== Book Recommendation System ===")
    genres_input = input("Preferred genres (comma-separated, e.g. fantasy, adventure): ")
    keywords_input = input("Optional keywords (comma-separated, e.g. dragon, science): ")
    read_input = input("Books already read (comma-separated; optional): ")

    results = recommend_books(
        preferred_genres=genres_input.split(","),
        keywords=keywords_input.split(","),
        read_books=read_input.split(","),
        top_k=5,
    )

    if not results:
        print("\nNo matches found. Try different genres or keywords.")
        return

    print("\nRecommended books:")
    for index, book in enumerate(results, start=1):
        print(f"{index}. {book['title']} — {book['author']}")
        print(f"   Genres: {', '.join(book['genres'])} | Score: {book['score']}")
        print(f"   {book['description']}")


if __name__ == "__main__":
    main()
