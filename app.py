from dotenv import load_dotenv, find_dotenv
import os, requests

load_dotenv(find_dotenv())

HUGGING_FACE_KEY = os.getenv("HUGGING_FACE_KEY")
story_text = ""

with open("story.txt") as story:
    story_text = story.read()


def load_audio(texts):
    API_URL = (
        "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    )
    headers = {"Authorization": "Bearer " + HUGGING_FACE_KEY}

    response = requests.post(API_URL, headers=headers, json={"inputs": texts})

    with open("audio.flac", "wb") as audio:
        audio.write(response.content)


load_audio(story_text)
