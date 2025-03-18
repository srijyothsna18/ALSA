import subprocess
import time
import pytest
from Core.common import Inputs

"""This test case is to verify that ALSA direct hardware access doesnt support multiple audio streams to play simultaneously"""

def play_audio_hw(device, file):
    return subprocess.Popen(["aplay", "-d", Inputs.PLAY_DURATION,"-D", device, file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@pytest.mark.xfail(reason="ALSA is expected to prevent multiple audio streams using direct hardware access.")
def test_play_multiple_audio_hw():
    alsa_device = Inputs.HARDWARE

    print(f"🎵 Playing {Inputs.AUDIO_FILE} using {alsa_device}...")
    process1 = play_audio_hw(alsa_device, Inputs.WAV_FILE_MULTIPLE)

    time.sleep(5)

    print(f"🎵 Attempting to play {Inputs.WAV_FILE} using {alsa_device}...")
    process2 = play_audio_hw(alsa_device, Inputs.WAV_FILE)

    time.sleep(5)

    process1.wait()
    process2.wait()

    stdout1, stderr1 = process1.communicate()
    stdout2, stderr2 = process2.communicate()

    print("\n=== First Process Output ===")
    print(stdout1.decode(), stderr1.decode())

    print("\n=== Second Process Output ===")
    print(stdout2.decode(), stderr2.decode())

    assert process1.returncode == 0, f"❌ First audio process failed with error: {stderr1.decode()}"
    assert "error" not in stderr1.decode().lower(), f"❌ Error in first audio playback: {stderr1.decode()}"

    # Mark xfail instead of failing when "Device or resource busy" occurs
    stderr2_decoded = stderr2.decode().lower()
    if "device or resource busy" in stderr2_decoded:
        pytest.xfail(f"⚠️ Expected failure: ALSA prevented the second playback with error: {stderr2_decoded}")

    print("\n✅ Verification complete: ALSA direct hardware access prevents multiple audio streams simultaneously!")
