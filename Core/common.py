import subprocess


def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    return process

class Inputs:
    AUDIO_FILE = "/home/vlab/ALSA/Inputs/sample.wav"         #44.1khz sampling rate
    WAV_FILE = "/home/vlab/ALSA/Inputs/thandel.wav"          #wav audio file
    MP3_FILE="/home/vlab/ALSA/Inputs/thandel.mp3"            #mp3 audio file
    AUDIO_FILE_96fs ="/home/vlab/ALSA/Inputs/output.wav"     #96khz sampling rate
    WAV_FILE_MULTIPLE = "/home/vlab/ALSA/Inputs/hileso.wav"  #44.1khz sampling rate
    AUDIO_FILE_MONO = "/home/vlab/ALSA/Inputs/thandel-mono.wav" #mono channel(1)
    HARDWARE = "hw:0,0"
    plugins = "plug"
    PLAY_DURATION = 10