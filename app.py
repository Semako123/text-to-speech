from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

HUGGING_FACE_KEY = os.getenv("HUGGING_FACE_KEY")
story_text = ""

with open('story.txt') as story:
    story_text = story.read()

print(story_text)

def load_audio(texts):
    pass