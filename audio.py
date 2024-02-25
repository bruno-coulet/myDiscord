#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON

@file: audio.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
import sounddevice as sd
from scipy.io.wavfile import write


def record(duration, samplerate=44100, channels=2):
    """
    Records audio
    :param duration: duration in seconds
    :param samplerate: frequency of recording
    :param channels: number of channels
    :return: numpy array with audio data
    """
    print("Recording for 10s")
    new_record = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
    sd.wait()
    return new_record

def play(recording, samplerate=44100):
    """
    Plays recording
    :param recording:
    :param samplerate:
    :return: None
    """
    sd.play(recording, samplerate=samplerate)
    sd.wait()


if __name__ == "__main__":
    recording = record(10)
    play(recording)
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", 44100, recording)

