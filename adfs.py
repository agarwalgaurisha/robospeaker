import pyttsx3
if __name__ == '__main__':


    engine = pyttsx3.init()

    while True:
        speak = input("Enter the text to speak : ")

        if speak != 'q':
            engine.say(speak)  # Making the pyttsx3 speak the text entered by the user
            engine.runAndWait()

        else:
            engine.say("thank you for using Robo Speaker ")
            engine.runAndWait()
            break
