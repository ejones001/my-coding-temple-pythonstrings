def create_summary(review):
    max_length = 30
    if len(review) <= max_length:
        return review
    else:
        summary = review[:max_length]
        # Check if the last character is part of a word
        if summary[-1] != ' ':
            # Find the last space within the summary
            last_space_index = summary.rfind(' ')
            if last_space_index != -1:
                summary = summary[:last_space_index]
        return summary + "..."

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

summaries = [create_summary(review) for review in reviews]

for i, summary in enumerate(summaries, 1):
    print(f"Review {i} Summary: {summary}")
