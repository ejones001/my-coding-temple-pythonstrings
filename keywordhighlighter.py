def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    for review in reviews:
        highlighted_review = review
        for keyword in keywords:
            highlighted_review = highlighted_review.replace(keyword, keyword.upper())
        print(highlighted_review)

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

highlight_keywords(reviews)
