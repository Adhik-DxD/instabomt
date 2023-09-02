import feedparser
import urllib.request
from instabot import Bot
import os
import re

def download_and_post_to_instagram(entry, bot):
    try:
        url = entry.media_content[0]['url']
        img_data = urllib.request.urlopen(url).read()
        caption = entry.title + '\n' + clean_html_tags(entry.description) + '\n\n' + tags
        bot.upload_photo(photo=img_data, caption=caption)
        print("Posted to Instagram successfully.")
    except Exception as e:
        print(f"Error posting to Instagram: {e}")

def clean_html_tags(text):
    # Implement your HTML tag cleaning logic here
    pass

if __name__ == "__main__":
    NewsFeed = feedparser.parse("https://www.sportsmole.co.uk/football/barcelona.xml")
    bot = Bot()

    # Retrieve Instagram credentials from environment variables
    username = os.environ.get("INSTAGRAM_USERNAME")
    password = os.environ.get("INSTAGRAM_PASSWORD")

    try:
        bot.login(username=username, password=password)
        print("Logged in to Instagram successfully.")
    except Exception as e:
        print(f"Error logging into Instagram: {e}")
        exit()

    tags = 'tags\n\n#barca #a #barcelona #messi ...'  # Add your tags here

    print('Number of RSS posts:', len(NewsFeed.entries))

    latest_entry_id = None

    for entry in NewsFeed.entries:
        try:
            entry_id = entry.get('id')
            if entry_id != latest_entry_id:
                print("New feed item found:")
                print(clean_html_tags(entry.description))
                download_and_post_to_instagram(entry, bot)
                latest_entry_id = entry_id
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Script execution completed.")
