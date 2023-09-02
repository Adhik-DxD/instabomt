import feedparser
import urllib.request
import os
import re
import time
from instapy_cli import client

def download_and_post_to_instagram(entry, username, password):
    try:
        url = entry.media_content[0]['url']
        img_filename = "imgmain.jpg"
        urllib.request.urlretrieve(url, img_filename)
        with client(username, password) as api:
            api.upload(img_filename, caption=caption)
        print("Posted to Instagram successfully.")
        os.remove(img_filename)  # Remove the image file after posting
    except Exception as e:
        print(f"Error posting to Instagram: {e}")

def clean_html_tags(text):
    # Implement your HTML tag cleaning logic here
    pass

if __name__ == "__main__":
    NewsFeed = feedparser.parse("https://www.sportsmole.co.uk/football/barcelona.xml")

    # Set your Instagram credentials using environment variables
    username = os.environ.get("INSTAGRAM_USERNAME")
    password = os.environ.get("INSTAGRAM_PASSWORD")

    try:
        print("Logging in to Instagram...")
        # Modify the logic to loop through entries and call download_and_post_to_instagram
        for entry in reversed(NewsFeed.entries):
            try:
                entry_id = entry.get('id')
                if entry_id == latest_entry_id:
                    print("All new posts have been processed.")
                    break
                print("New feed item found:")
                print(clean_html_tags(entry.description))
                caption = entry.title + '\n' + clean_html_tags(entry.description) + '\n\n' + tags
                download_and_post_to_instagram(entry, username, password)
                latest_entry_id = entry_id
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Logged in to Instagram successfully.")
    except Exception as e:
        print(f"Error logging into Instagram: {e}")
        exit()

    tags = 'tags\n\n#barca #a #barcelona #messi ...'  # Add your tags here

    print('Number of RSS posts:', len(NewsFeed.entries))

    latest_entry_id = None

    while True:
        for entry in reversed(NewsFeed.entries):
            try:
                entry_id = entry.get('id')
                if entry_id == latest_entry_id:
                    print("All new posts have been processed.")
                    break
                print("New feed item found:")
                print(clean_html_tags(entry.description))
                caption = entry.title + '\n' + clean_html_tags(entry.description) + '\n\n' + tags
                download_and_post_to_instagram(entry, username, password)
                latest_entry_id = entry_id
            except Exception as e:
                print(f"An error occurred: {e}")

        print("Waiting for 10 minutes before checking for new posts...")
        time.sleep(600)  # Sleep for 10 minutes before checking again

    print("Script execution completed.")
    
