#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
Sound recording demo using PyAudio.
This script was tested on Python 2.7 and Python 3.6 using PyAudio 0.2.11
Latest version can be found at https://github.com/dakside/pydemo

References:
    PyAudio Documentation:
        http://people.csail.mit.edu/hubert/pyaudio/#docs
    Python documentation:
        https://docs.python.org/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2018, Le Tuan Anh <tuananh.ke@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__author__ = "Le Tuan Anh <tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2018, pydemo"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

import pyaudio
import wave
import time
import struct


class AudioFacade:
    ''' Simple Audio Facade '''
    def __init__(self, threshold=200):
        self.__audio = pyaudio.PyAudio()
        self.__threshold = threshold

    def loudness(self, chunk):
        # signed shorts, 2 bytes each
        count = len(chunk) / 2
        numbers = struct.unpack("{}h".format(count), chunk)
        return sum(abs(n) for n in numbers) / count

    def record(self, filename, duration=3, format=pyaudio.paInt16, channels=1, rate=44100, chunk_size=2048, **kwargs):
        ''' Record sound and write to a WAVE file '''
        # input stream
        stream = self.__audio.open(input=True, format=format, channels=channels, rate=rate, frames_per_buffer=chunk_size, **kwargs)
        # output file
        outfile = wave.open(filename, 'wb')
        outfile.setnchannels(channels)
        outfile.setsampwidth(pyaudio.get_sample_size(format))
        outfile.setframerate(rate)

        # recording
        # round() return floats in python 2, int() is not needed for python 3
        chunk_count = int(round((duration * rate) / chunk_size))
        chunks = []
        activated = False
        start_time = time.time()
        response_time = -1
        for i in range(0, chunk_count):
            chunk = stream.read(chunk_size, exception_on_overflow=False)
            if not activated:
                loudness = self.loudness(chunk)
                print(loudness)
                activated = loudness > self.__threshold
                if activated:
                    response_time = time.time() - start_time
            chunks.append(chunk)
        outfile.writeframes(b''.join(chunks))

        # close file & audio streams
        outfile.close()
        stream.stop_stream()
        stream.close()
        return (activated, response_time)

    def play_wav(self, filename, chunk=1024, **kwargs):
        ''' Play back a WAVE file '''
        wf = wave.open(filename, 'rb')
        audio_format = self.__audio.get_format_from_width(wf.getsampwidth())
        stream = self.__audio.open(format=audio_format,
                                   channels=wf.getnchannels(),
                                   rate=wf.getframerate(),
                                   output=True, **kwargs)
        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
        # finished
        stream.stop_stream()
        stream.close()
        wf.close()

    def get_devices(self):
        ''' Get all available devices '''
        device_count = self.__audio.get_device_count()
        devices = []
        for i in range(device_count):
            device = self.__audio.get_device_info_by_index(i)
            devices.append(device)
        return devices

    # support python context manager (using `with')
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.__audio.terminate()


if __name__ == "__main__":
    with AudioFacade() as aufa:
        # list all device for user to select
        devices = aufa.get_devices()
        for idx, device in enumerate(devices):
            indevs = device['maxInputChannels']
            outdevs = device['maxOutputChannels']
            print("{}. {} - Inputs: {} | Outputs: {}".format(idx, device['name'], indevs, outdevs))
        choice = raw_input("Which device do you want to use (enter nothing to quit)? ")
        if choice:
            device_id = int(choice)
        else:
            print("Bye")
            exit()

        # recording
        files = []
        for i in range(1, 4):
            print("Get ready for file %s" % i)
            time.sleep(0.5)
            print("Start!")
            filename = 'test_audio_%d.wav' % i
            files.append(filename)
            activated, response_time = aufa.record(filename, duration=3, chunk_size=4096, input_device_index=device_id)
            print("Activated: {} | response_time: {}".format(activated, response_time))

        # play back
        for fn in files:
            print("Playing {}".format(fn))
            aufa.play_wav(fn)
    print("Done")
