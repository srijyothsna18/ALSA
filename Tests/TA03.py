from Core.common import run_command
from Core.common import Inputs
import time

"""This test case is to verify that a sample audio file is played using ALSA successfully"""

def play_audio():
    result = run_command(f"aplay -d {Inputs.PLAY_DURATION} {Inputs.AUDIO_FILE}")
    time.sleep(5)
    return result


def test_audio():
    #Test if ALSA can play an audio file successfully
    result = play_audio()
    print("\nPlaying audio file...")
    assert result.returncode == 0, f"❌ Failed to play audio: {result.stderr}"
    print("✅ Audio played successfully.")


