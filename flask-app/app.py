from flask impo!rt Flask, render_template
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
visitor_count_file = 'visitor_counter.txt'

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
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Ensure the table exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS visitor_counter (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          count INT NOT NULL DEFAULT 0
                        )''')
        
        # Retrieve the current visitor count
        cursor.execute('SELECT count FROM visitor_counter LIMIT 1')
        row = cursor.fetchone()
        
        if row is None:
            visitor_count = 1
            cursor.execute('INSERT INTO visitor_counter (count) VALUES (%s)', (visitor_count,))
        else:
            visitor_count = row[0] + 1
            cursor.execute('UPDATE visitor_counter SET count = %s', (visitor_count,))

        conn.commit()
        cursor.close()
        conn.close()
        return visitor_count
    except mysql.connector.Error as err:
        print(f"Error: {err}")
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
