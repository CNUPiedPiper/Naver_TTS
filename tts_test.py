# -*- coding: utf-8 -*-
import tts

text_to_speech = tts.tts()
print(text_to_speech.get_speech_file_path(u"오늘은 비가 올 것으로 예상 됩니다."))
