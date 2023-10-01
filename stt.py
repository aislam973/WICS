from gtts import gTTS

# Define the language for speech synthesis (in this case, English)
language = "en"

# The text you want to convert to speech
text = "Hello Women in Computer Science club members. Hopefully this works!"

# Create a 'gTTS' object by specifying the text, language, and other options
# 'slow' is set to False, which means the speech will not be artificially slowed down
# 'tld' (Top-Level Domain) is set to "com.au," which may affect the accent/pronunciation
speech = gTTS(text=text, lang=language, slow=False, tld="com.au")

# Save the generated speech as an MP3 file with the name 'textTospeech.mp3'
speech.save("textTospeech.mp3")

