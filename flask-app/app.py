from flask import Flask, render_template
import os
import mysql.connector
import random

app = Flask(__name__)

# Database connection details using environment variables
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# Path to the file that will store the visitor count
visitor_count_file = "/app/data/visitor_count.txt"


# Function to get image URLs from the database
def get_image_urls():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to get all image URLs from the 'images' table
        cursor.execute('SELECT url FROM images')
        image_urls = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return image_urls
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Function to get and increment the visitor count
def get_and_increment_visitor_count():
    try:
        # Read the current count from the file or start from 0 if the file doesn't exist
        if os.path.exists(visitor_count_file):
            with open(visitor_count_file, 'r') as file:
                count = int(file.read().strip())
        else:
            count = 0

        # Increment the count
        count += 1

        # Save the updated count back to the file
        with open(visitor_count_file, 'w') as file:
            file.write(str(count))

        return count
    except Exception as e:
        print(f"Error updating visitor count: {e}")
        return None

@app.route("/")
def index():
    image_urls = get_image_urls()
    visitor_count = get_and_increment_visitor_count()

    # Check if there are image URLs in the database
    if image_urls:
        url = random.choice(image_urls)
        return render_template("index.html", url=url, visitor_count=visitor_count)
    else:
        return "No images found in the database."

if __name__ == "__main__":
    # Get the port from the environment variable, defaulting to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
