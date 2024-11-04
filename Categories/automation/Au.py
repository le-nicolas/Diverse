from gtts import gTTS
import os

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    os.system(f"mpg321 {output_file}")

text = "Hello, this is an automated voice message."
audio_file = 'output.mp3'
text_to_speech(text, audio_file)
