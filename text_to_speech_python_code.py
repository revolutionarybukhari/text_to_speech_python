//@Syed Husnain Haider Bukhari
from gtts import gTTS

text = "Hello, this is a test of the text-to-speech conversion using Python."

# Create a gTTS instance
tts = gTTS(text, lang='en', tld='co.in')
tts.speed = 2.0
tts.save("hello.mp3")
