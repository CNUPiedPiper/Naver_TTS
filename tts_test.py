# -*- coding: utf-8 -*-
import tts

text_to_speech = tts.tts()

your_text = u"오늘 날씨는 맑을것으로 예상 됩니다."
print(text_to_speech.get_speech_file_path(your_text))
