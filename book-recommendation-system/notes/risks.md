# Risks and Limitations

## 1. Cold-start problem
**Risk:** A new user may not have any ratings or reading history, so the system has limited evidence about their interests. A new book with incomplete metadata may also be difficult to recommend.

**Mitigation:** Ask the user to select a few genres or favorite books, and make sure each catalog entry has basic metadata.

## 2. Limited or inaccurate book metadata
**Risk:** Incorrect genres, short descriptions, or missing authors can lead to irrelevant recommendations.

**Mitigation:** Validate the dataset, standardize genre labels, and periodically review missing or inconsistent fields.

## 3. Popularity and diversity bias
**Risk:** A recommender may repeatedly suggest similar books and fail to expose users to less familiar genres or authors.

**Mitigation:** Add a diversity rule, such as limiting repeated authors or including a small number of recommendations from secondary preferred genres.

## 4. Evaluation data is unavailable
**Risk:** Without verified relevance labels, user ratings, or feedback, Precision@K and Recall@K cannot be measured reliably.

**Mitigation:** Use a public dataset with ratings or collect explicit user feedback; report baseline results only when supported by data.

## 5. Privacy concerns
**Risk:** Reading history and ratings may reveal personal interests.

**Mitigation:** Collect only necessary data, explain how it is used, and avoid storing personal identifiers in the prototype.

## 6. Small sample catalog
**Risk:** The included catalog is only a demonstration. Results may not generalize to a larger and more diverse collection.

**Mitigation:** Replace the sample data with a documented public dataset before making performance claims.
