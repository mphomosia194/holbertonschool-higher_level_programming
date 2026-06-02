#!/usr/bin/python3
"""Fetch and process data from JSONPlaceholder."""

import csv
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status code and titles."""
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save selected data to posts.csv."""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(data)
