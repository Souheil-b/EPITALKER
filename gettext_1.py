# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def speaktext(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def detect_word(text):
    myword = ["gpa", "module", "plannig", "agenda", "credits", "modules"]
    for word in text.split():
        if word in myword:
            print(word)
            return word
    print("word not found")


# Loop infinitely for user to
# speak


def get_audio():
    while 1:

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                print("Dites quelque chose")
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2, language="fr-FR")
                MyText = MyText.lower()

                print("Vous avez dit: ", MyText)
                speaktext(MyText)
                detect_word(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")


get_audio()
