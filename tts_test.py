# -*- coding: utf-8 -*-
import tts

text_to_speech = tts.tts()

your_text = u"hoo.. 내일의 최고 기온은 28.00 도, 최저 지온은 18.00 도 이며, 구름이 많은 날씨가 예상됩니다."
print(text_to_speech.get_speech_file_path(your_text))
