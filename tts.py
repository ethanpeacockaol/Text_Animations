from gtts import gTTS

text_to_speak = "all hail paegan"
language = 'en'  # 'en' for English, 'es' for Spanish, 'fr' for French, etc.

tts = gTTS(text=text_to_speak, lang=language, slow=False) # slow=False makes the speech faster

file_name = "/data/data/com.termux/files/home/0/0/Music/output42.mp3"
tts.save(file_name)
