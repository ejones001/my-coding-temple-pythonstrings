def track_positive_negative_words(reviews, positive_words, negative_words):
    results = []
    for review in reviews:
        positive_count = 0
        negative_count = 0
        review_lower = review.lower()
        for word in positive_words:
            if word in review_lower:
                positive_count += 1
        for word in negative_words:
            if word in review_lower:
                negative_count += 1
        results.append((positive_count, negative_count))
    return results

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

results = track_positive_negative_words(reviews, positive_words, negative_words)
for i, (positive_count, negative_count) in enumerate(results, 1):
    print(f"Review {i}: Positive words: {positive_count}, Negative words: {negative_count}")
