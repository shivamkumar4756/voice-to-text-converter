import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust ambient noise
        audio = recognizer.listen(source, timeout=5)  # Listen audio input within a 5-second timeout

    text = recognizer.recognize_google(audio)

    print("You said: " + text)

except sr.WaitTimeoutError:
    print("No speech detected. Please try again.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
