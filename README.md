# Naver Text To Speech Service at python 2.X

You can get the mp3 file path(unique) as a result by giving some text as input.

``` python
import tts

text_to_speech = tts.tts()
print(text_to_speech.get_speech_file_path("안녕하세요"))
```
