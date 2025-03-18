import subprocess
import time
from Core.common import run_command
from Core.common import Inputs

""" this test case is to verify the plug plugin functionality when more than hardware supported sample rate is being played """


def get_hw_params():
    #Read the current hardware playback parameters
    result = run_command("cat /proc/asound/card0/pcm0p/sub0/hw_params")
    return result.stdout


def play_audio(device, file_path):
    #Plays an audio file and reads hardware parameters during playback
    print(f"\nPlaying on device: {device}...")
    process = subprocess.Popen(f"aplay -D {device} {file_path}", shell=True, text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    time.sleep(1)

    # Get hardware parameters during playback
    hw_params = get_hw_params()
    process.wait()

    stdout, stderr = process.communicate()
    print("Playback complete...\n")
    print("STDOUT:", stdout)
    print("STDERR:", stderr)

    return hw_params


def test_plugin_functionality():
    #Playing audio on hardware hw:0,0
    hw_params_hw = play_audio(Inputs.HARDWARE, Inputs.AUDIO_FILE_96fs)

    #Playing audio on hardware hw:0,0 using plug plugin
    hw_params_plughw = play_audio("plughw:0,0", Inputs.AUDIO_FILE_96fs)

    #Check sample rate change
    if "96000" in hw_params_hw and "96000" in hw_params_plughw:
        print("\n✅ plughw preserved the sample rate at 96 kHz.")
        assert True
    elif "48000" in hw_params_plughw:
        print("\nplughw resampled the file to 48 kHz.")
        assert True
    else:
        print("\nUnexpected behavior. Check manually.")
        assert False
