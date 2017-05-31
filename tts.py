# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import datetime
from urllib2 import urlopen, Request
from urlparse import urlparse
from pygame import mixer, time
from pydub import AudioSegment

class tts:
    def __init__(self):
        self.client_id = "YOUR_CLIENT_ID"
        self.client_secret = "YOUR_CLIENT_SECRET"

    def play_sound(self, file_path):
        mixer.init(frequency=16000, buffer=24000)
        mixer.music.load(file_path)
        mixer.music.play(loops=1)
        while mixer.music.get_busy():
            time.Clock().tick(100)

    def get_speech_file_path(self, input_text):
        data = "speaker=mijin&speed=0&text=" + unicode(input_text);

        q = Request("https://openapi.naver.com/v1/voice/tts.bin")
        q.add_header("X-Naver-Client-Id", self.client_id)
        q.add_header("X-Naver-Client-Secret", self.client_secret)

        response = urllib2.urlopen(q, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode == 200):
            print("Saved TTS to MP3")
            response_body = response.read()
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y%m%d_%H:%M:%S')
            filename = str(nowDatetime) + '.mp3'
            
            with open(filename, 'wb') as f:
                f.write(response_body)

            song = AudioSegment.from_mp3(filename)
            second_of_silence = AudioSegment.silent(duration=1000)
            newsong = second_of_silence + song + second_of_silence
            newsong.export(filename, format="mp3")

            self.play_sound(filename)
            return filename
            
        else:
            print("Error Code:" + rescode)

