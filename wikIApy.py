import pyttsx3 as ptt
import speech_recognition as sr
import wikipediaapi as wk
# import pywhatkit as wt


def parler(command):
    engine = ptt.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voice",voice[0].id)
    engine.say(command)
    engine.runAndWait()

def ecouter():
    liscener = sr.Recognizer()
    try:
        with sr.Microphone() as source :
            print("parlez maintenant ...")
            voix = liscener.listen(source)
            command = liscener.recognize_google(voix ,language="fr-FR")      
            return command

    except :
        pass




def lancerass() :
    import datetime
    x = datetime.datetime.now()
    command = ecouter()
    # if 'date' in command :
    #     jour = x.strftime("%A")
    #     mois = x.strftime("%B")
    #     annee =x.strftime("%Y")
    #     date = jour + mois + annee
    #     parler(date)
    
    #wt.playonyt(command)

    if 'bonjour' in command :
        parler("bonjour ça va et toi ?")
    
    if 'blague' in command:
        b ="""Pourquoi les cahiers de mathématiques sont-ils tristes ?
Réponse : Parce qu'ils ont trop de problèmes."""
        parler(b)

 
    wiki_wiki = wk.Wikipedia('fr')
    page_py = wiki_wiki.page(command)
    if page_py.exists():
        parler(page_py.summary)
        print(page_py.summary)
        
       
       



        

   




lancerass()