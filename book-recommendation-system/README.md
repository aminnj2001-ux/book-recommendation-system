# Book Recommendation System

## Project Overview
The goal of this project is to develop a simple intelligent agent that recommends books to users based on book features and user preferences. The initial version uses content-based filtering: it compares a user's preferred genres and optional keywords with each book's metadata and ranks books by a relevance score.

This is a baseline implementation for the first project milestone. It uses a small sample catalog and can later be extended with real ratings, user-item interactions, collaborative filtering, and a larger dataset.

## Problem Definition
Given a user's preferred genres and optional keywords, the system should return a ranked list of books that are likely to match the user's interests.

**Input:** preferred genres and optional keywords.  
**Output:** a ranked list of recommended books with titles, authors, genres, and relevance scores.  
**Goal:** provide relevant, diverse, and useful recommendations while avoiding books the user has already read (when that information is available).

## PEAS Description

| Component | Description for the Book Recommendation System |
|---|---|
| **Performance Measure** | Precision@K / Recall@K when ground-truth user ratings are available; otherwise, user satisfaction, relevance of the top-K results, catalog coverage, and response time. |
| **Environment** | The user, book catalog, book metadata (title, author, genres, description), and optionally user ratings, reading history, and feedback. |
| **Actuators** | Display ranked recommendations, show book details, filter or sort results, and request feedback such as like/dislike. |
| **Sensors** | User-entered genre preferences and keywords; book metadata; optionally ratings, clicks, reading history, and explicit feedback. |

## Environment Properties

| Property | Classification | Explanation |
|---|---|---|
| Observability | Partially observable | The system does not initially know all of a user's interests, reading history, or reasons for liking a book. |
| Agents | Single-agent (for the baseline) | The recommender makes ranking decisions; the user interacts with the system but is not modeled as a competing agent. |
| Determinism | Stochastic / uncertain | A recommendation does not guarantee that the user will like or read the book. |
| Episodic vs. Sequential | Sequential | Recommendations and user feedback can influence later recommendations. |
| Static vs. Dynamic | Dynamic | The catalog, user preferences, and reading history may change over time. |
| Discrete vs. Continuous | Mostly discrete | Books, genres, and user actions are discrete; relevance scores are numerical and continuous-valued. |

## Evaluation Criteria
For a labeled dataset containing relevant books or user ratings, evaluate the recommender using **Precision@K** and **Recall@K**. Precision@K measures the fraction of the top-K recommendations that are relevant, while Recall@K measures the fraction of all relevant books that appear in the top-K list.

For the initial sample-catalog version, also check:
- Whether recommendations match the selected genres and keywords.
- Whether the system returns up to K unique books.
- Whether already-read books can be excluded.
- Runtime for producing recommendations.

## Baseline Algorithm
1. Normalize the user's genre preferences and keywords.
2. Compare them with each book's genres, title, author, and description.
3. Calculate a simple relevance score using genre matches and keyword matches.
4. Exclude books in the user's read list.
5. Sort by score and return the top-K books.

## How to Run
Requires Python 3.10 or later. NumPy and Matplotlib are used for environment checks in `check_env.ipynb`; the baseline recommender itself uses only the Python standard library.

```bash
python main.py
```

To check the development environment, open `check_env.ipynb` in Jupyter Notebook or VS Code and run all cells.

Install notebook dependencies with:

```bash
pip install -r requirements.txt
```

## Project Limitations
- The sample catalog is small and illustrative, not suitable for real-world performance claims.
- The baseline does not learn from other users and is not collaborative filtering.
- Recommendations depend on the quality and completeness of book metadata.
- No empirical Precision@K or Recall@K can be reported until a labeled dataset or user feedback is available.

## Next Steps
- Replace the sample catalog with a public book dataset.
- Collect user ratings or implicit feedback.
- Add automated tests and calculate Precision@K / Recall@K.
- Compare content-based filtering with collaborative filtering.
