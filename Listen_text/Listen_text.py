import speech_recognition as sr




class lisien_text:
    def __init__(self,rout):
        r = sr.Recognizer()
        AUDIO_FILE = rout  
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  
        try:
            text = r.recognize_google(audio)
            print("Transcription: " + text)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")