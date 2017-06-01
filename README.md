# Naver Text To Speech Service at python 2.X

You can get the mp3 file and sound of text(Korean) as a result by giving some text as input.

## Dependency
```
$ pip2 install pygame
```

## Running a demo
``` python
import tts

text_to_speech = tts.tts()
your_text = u"내일의 최고 기온은 28.00 도, 최저 지온은 18.00 도 이며, 구름이 많은 날씨가 예상됩니다."
print(text_to_speech.get_speech_file_path(your_text))
```
