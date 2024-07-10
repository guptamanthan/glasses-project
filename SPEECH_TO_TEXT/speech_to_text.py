import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2 , duration=1)

                audio2 = r.listen(source2)

                Mytext = r.recognize_google(audio2) # type: ignore

                return Mytext
            

        except sr.RequestError as e:
            print("could not request result , {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured") 


    return

def output_txt(text):
    f=open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close
    return

while(1):
    text = record_text()
    output_txt(text)

    print("wrote text")                 

