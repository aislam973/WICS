import random
import time
import csv
import speech_recognition as sr

# This function records audio from a microphone, attempts to recognize speech in the recording,
# and returns the recognized transcription or any errors.
def recognize_speech_from_mic(recognizer, microphone):
    # Check that the recognizer and microphone arguments are of the appropriate type.
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be a `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be a `Microphone` instance")

    # Adjust the recognizer's sensitivity to ambient noise and record audio from the microphone.
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Set up the response object to store the results of speech recognition.
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Try recognizing the speech in the recording.
    # If a RequestError or UnknownValueError exception is caught, update the response object accordingly.
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    # Read words from a CSV file
    with open('valid_solutions.csv', 'r') as file:
        reader = csv.reader(file)
        words = [row[0] for row in reader]

    # Select 5 random words from the list
    NUM_WORDS_TO_PICK = 10
    selected_words = random.sample(words, NUM_WORDS_TO_PICK)
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # Create recognizer and microphone instances from the SpeechRecognition library.
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Get a random word from the list of words.
    word = random.choice(selected_words)

    # Format the instructions string to provide the user with information about the game.
    instructions = (
        "Welcome to the Word Guessing Game!\n"
        "I've picked a five letter word, and you have {n} tries to guess it.\n"
        "Here are some words you can guess:\n"
        "{words}\n"
    ).format(words=', '.join(selected_words), n=NUM_GUESSES)

    # Display instructions to the user and wait for 3 seconds before starting the game.
    print(instructions)
    time.sleep(3)

    # Loop for the maximum number of guesses.
    for i in range(NUM_GUESSES):
        # Get the user's guess through speech input.
        # If a transcription is returned, break out of the loop and continue.
        # If no transcription is returned and the API request failed, break the loop and continue.
        # If the API request succeeded but no transcription was returned, re-prompt the user to say their guess again,
        # and do this up to the PROMPT_LIMIT times.
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i + 1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        # If there was an error, stop the game and display the error message.
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))

        # Display what the user said.
        print("You said: {}".format(guess["transcription"]))

        # Determine if the user's guess is correct and if any attempts remain.
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # Determine if the user has won the game.
        # If not, repeat the loop if the user has more attempts.
        # If there are no attempts left, the user loses the game.
        if guess_is_correct:
            print("Correct! You win! The word was '{}'.".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose! The word was '{}'.".format(word))
            break
