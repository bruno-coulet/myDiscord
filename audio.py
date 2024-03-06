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
    print(f"Recording for {duration}s")
    new_record = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
    sd.wait()
    return new_record


def play(records, samplerate=44100):
    """
    Plays recording
    :param records:
    :param samplerate:
    :return: None
    """
    sd.play(records, samplerate=samplerate)
    sd.wait()


if __name__ == "__main__":
    recording = record(10)

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording.wav", 44100, recording)
