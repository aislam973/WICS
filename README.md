# WICS
This the the demo from the Intro to AI/ML workshop. 

# For the stt.py:
API used: Google Translate’s Text-to-Speech API: https://gtts.readthedocs.io/en/latest/index.html
To get started, you need to install gTTS:
pip install gTTS 

# For game.py:
Library used: https://pypi.org/project/SpeechRecognition/
To get started, you need to install pyaudio and SpeechRecognition: 
pip install SpeechRecognition
pip install pyaudio

I initially drew inspiration from the Real Python article titled "Python Speech Recognition" (https://realpython.com/python-speech-recognition/) and used the code provided as a starting point. This article gives a concise introduction to how speech recognition software works, outlines APIs and libraries available for implementing speech recognition in Python, and also provides a detailed breakdown of the code/ game logic.

To put my own twist on provided code, I used a dataset from Kaggle that contains solutions for 5-letter words in the game Wordle. This dataset made it possible for me to pick words for the game without having to hardcode a set of words into the program.

# Here are some other great resources to learn more about speech to text/ text to speech programs within python.
https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
https://thepythoncode.com/article/convert-text-to-speech-in-python
