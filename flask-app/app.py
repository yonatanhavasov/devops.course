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

# Function to get image URLs from the database
def get_image_urls():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT url FROM images')
        image_urls = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return image_urls
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

# Function to get and increment the visitor count in the database
def get_and_increment_visitor_count():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create the table if it does not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS visitor_count (
                          id INT PRIMARY KEY AUTO_INCREMENT,
                          count INT NOT NULL DEFAULT 0
                        )''')
        
        # Insert initial value if the table is empty
        cursor.execute('SELECT count FROM visitor_count LIMIT 1')
        row = cursor.fetchone()
        
        if row is None:
            cursor.execute('INSERT INTO visitor_count (count) VALUES (1)')
            visitor_count = 1
        else:
            visitor_count = row[0] + 1
            cursor.execute('UPDATE visitor_count SET count = %s', (visitor_count,))
        
        conn.commit()
        cursor.close()
        conn.close()
        return visitor_count
    except Exception as e:
        print(f"Error updating visitor count: {e}")
        return None

@app.route("/")
def index():
    image_urls = get_image_urls()
    visitor_count = get_and_increment_visitor_count()
    
    if image_urls:
        url = random.choice(image_urls)
        return render_template("index.html", url=url, visitor_count=visitor_count)
    else:
        return "No images found in the database."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
