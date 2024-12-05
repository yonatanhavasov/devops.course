from flask import Flask, render_template
import os
import mysql.connector
import random

app = Flask(__name__)

# Database connection details
db_config = {
    'host': 'db',  # Name of the MySQL service in docker-compose.yaml
    'user': 'gif_user',
    'password': 'gif_password',
    'database': 'gif_db'
}

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

@app.route("/")
def index():
    image_urls = get_image_urls()

    # Check if there are image URLs in the database
    if image_urls:
        url = random.choice(image_urls)
        return render_template("index.html", url=url)
    else:
        return "No images found in the database."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
