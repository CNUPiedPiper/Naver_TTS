# Naver Text To Speech Service at python 2.X

You can get the mp3 file path(timestamp) and sound of text(Korean) as a result by giving some text as input.

``` python
import tts

text_to_speech = tts.tts()
your_text = u"오늘 날씨는 맑을것으로 예상 됩니다."
print(text_to_speech.get_speech_file_path(your_text))
```
