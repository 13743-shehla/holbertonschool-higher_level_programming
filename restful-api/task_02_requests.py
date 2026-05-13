import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code
    and titles of all posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()
        # Iterate through the parsed JSON data and print titles
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches posts and saves specific fields (id, title, body)
    into a CSV file called posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Structure the data into a list of dictionaries with specific keys
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        # Write data into a CSV file called posts.csv
        keys = ['id', 'title', 'body']
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(structured_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
