import pyttsx3  ## text to speach library
import webbrowser

def voiceMessage():
    ttsEngine = pyttsx3.init()

    volume = ttsEngine.getProperty('volume')
    print("starting volume", volume)
    ttsEngine.setProperty('volume', 0.5)  # volume level  between 0 and 1

    voices = ttsEngine.getProperty('voices')  # getting details of current voice
    print(voices)
    ttsEngine.setProperty('voice', voices[0].id)

    ttsEngine.say("I will speak this text")
    ttsEngine.runAndWait()


def startUp():
    print("starting")
    pyttsx3.speak(" Powered on")
    webbrowser.open("www.google.com")
    runLoop()


def getQuery():
    query = "a" # this will be the voice command
    return query


def runLoop():
    while True:
        query = getQuery().lower()


if __name__ == '__main__':
    startUp()

