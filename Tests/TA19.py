from Core.common import Inputs
import subprocess
import time

"""This test case is to verify that PulseAudio allows multiple audio streams to play simultaneously"""

def play_audio_pulse(file):
    return subprocess.Popen(["aplay", "-D", "pulse", "-d", "5", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_play_multiple_audio_streams():

    print(f"Playing {Inputs.AUDIO_FILE} using PulseAudio...")
    process1 = play_audio_pulse(Inputs.AUDIO_FILE)


    print(f"Playing {Inputs.WAV_FILE} using PulseAudio...")
    process2 = play_audio_pulse(Inputs.WAV_FILE)


    process1.wait()
    process2.wait()

    stdout1, stderr1 = process1.communicate()
    stdout2, stderr2 = process2.communicate()

    print("\n=== First Process Output ===")
    print(stdout1.decode(), stderr1.decode())

    print("\n=== Second Process Output ===")
    print(stdout2.decode(), stderr2.decode())

    assert process1.returncode == 0, f"❌ First audio process failed with error: {stderr1.decode()}"
    assert process2.returncode == 0, f"❌ Second audio process failed with error: {stderr2.decode()}"

    assert "error" not in stderr1.decode().lower(), f"❌ Error in first audio playback: {stderr1.decode()}"
    assert "error" not in stderr2.decode().lower(), f"❌ Error in second audio playback: {stderr2.decode()}"
    time.sleep(5)
    print("\n✅ Verification complete: PulseAudio allows multiple audio streams simultaneously!")
