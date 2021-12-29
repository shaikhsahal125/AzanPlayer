from gtts import gTTS

import os



def generateSpeech(text, language, file_name):
	speech = gTTS(text = text, lang = language, slow = False)

	speech.save(f"/home/pi/AzanPlayer/customTextSpeech/{file_name}")



englishMsg = "Please complete your previous prayer if you haven't. The next Azaan will be in fifteen minutes. Thank You!"
language = 'en'
file_name = 'engMsg.mp3'
generateSpeech(englishMsg, language, file_name)


hindiTxt = "انشا اللہ،  اگلی آذان پندرہ منٹ مے ہوگی"
language = 'ur'
file_name = 'urduTest.mp3'
generateSpeech(hindiTxt, language, file_name)


engFajrMsg = "Please complete your fajr Prayer before the sunrise. Thank You!"
language = 'en'
file_name = 'engFajrMsg.mp3'
generateSpeech(engFajrMsg, language, file_name)



urduFajrMsg = 'انشا اللہ ، طلوع آفتاب پندرہ منٹ مے ہوگا !'
language = 'ur'
file_name = 'urduFajrMsg.mp3'
generateSpeech(urduFajrMsg, language, file_name)
