from playsound import playsound
from elevenlabs.client import ElevenLabs

api_key = "4f730ae5c21b5260aab82cbb50794ba6"

client = ElevenLabs(api_key=api_key)

text = "A laptop computer or notebook computer, also known as a laptop or notebook, is a small, portable personal computer (PC). Laptops typically have a clamshell form factor with a flat panel screen (usually 11–17 in or 280–430 mm in diagonal size) on the inside of the upper lid and an alphanumeric keyboard and pointing device (such as a trackpad and/or trackpoint) on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are often marketed as laptops or as having a laptop mode7.Most of the computer's internal hardware is fitted inside the lower lid enclosure under the keyboard, although many laptops have a built-in webcam at the top of the screen and some modern ones even feature a touch-screen display. In most cases, unlike tablet computers which run on mobile operating systems, laptops tend to run on desktop operating systems, which were originally developed for desktop computers."
voice = "woman"
model = "eleven_multilingual_v2"

audio = client.generate(text=text, voice=voice, model=model)

with open("welcome.mp3", "wb") as file:
    for chunk in audio:
        file.write(chunk)  

playsound("welcome.mp3")
