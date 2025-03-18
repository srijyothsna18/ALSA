import subprocess
import time
from Core.common import Inputs

"""This test case is to verify that ALSA's plugin dmix allows multiple audio streams to play simultaneously"""

def play_audio_dmix(file):
    return subprocess.Popen(["aplay", "-D", "plug:dmix", "-d", str(Inputs.PLAY_DURATION), file],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_play_multiple_audio_streams():
    print(f"Playing {Inputs.WAV_FILE_MULTIPLE} using dmix...")
    process1 = play_audio_dmix(Inputs.WAV_FILE_MULTIPLE)

    time.sleep(1)  # Give the first audio stream a little head start

    print(f"Playing {Inputs.WAV_FILE} using dmix...")
    process2 = play_audio_dmix(Inputs.WAV_FILE)

    # Wait for both processes to complete
    stdout1, stderr1 = process1.communicate()
    stdout2, stderr2 = process2.communicate()

    print("\n=== First Process Output ===")
    print(stdout1.decode(), stderr1.decode())

    print("\n=== Second Process Output ===")
    print(stdout2.decode(), stderr2.decode())

    # Check if both processes ran successfully
    assert process1.returncode == 0, f"❌ First audio process failed with error: {stderr1.decode()}"
    assert process2.returncode == 0, f"❌ Second audio process failed with error: {stderr2.decode()}"

    # Ensure no errors occurred during playback
    assert "error" not in stderr1.decode().lower(), f"❌ Error in first audio playback: {stderr1.decode()}"
    assert "error" not in stderr2.decode().lower(), f"❌ Error in second audio playback: {stderr2.decode()}"

    print("\n✅ Verification complete: ALSA dmix allows multiple audio streams simultaneously!")
