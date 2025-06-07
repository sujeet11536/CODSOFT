# Recommendation System

A simple recommendation system that suggests items to users based on their preferences. This project demonstrates basic recommendation techniques such as collaborative filtering to recommend movies, books, or products.

## Features

- User-based collaborative filtering
- Suggests items based on similar users' preferences
- Easy to extend for content-based filtering or hybrid methods

## Dataset

This project uses user-item rating data (e.g., MovieLens dataset). Place your data file as `data/ratings.csv` with the following columns:

- `userId` — unique user identifier
- `movieId` — unique item identifier (e.g., movie)
- `rating` — user rating for the item

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/recommendation-system.git
   cd recommendation-system
