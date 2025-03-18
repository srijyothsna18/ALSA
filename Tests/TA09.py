import os
from Core.common import run_command
from Core.common import Inputs

"""This test case is to verify audio recording using arecord is successfull"""

def audio_recording(duration):
    OUTPUT_FILE = "/home/vlab/ALSA/Outputs/test_recording.wav"
    print("\n🎙️ Recording audio...")
    process = run_command(f"arecord -d {duration} -f cd -t wav { OUTPUT_FILE}")


    assert process.returncode == 0, f"❌ arecord failed: {process.stderr}"
    assert os.path.exists(OUTPUT_FILE), f"❌ Audio file was not created at {OUTPUT_FILE}."
    assert os.path.getsize(OUTPUT_FILE) > 0, "❌ The recorded audio file is empty."

    print("\n🔊 Playing recorded audio...")
    run_command("aplay test_recording.wav")

    print("\n✅ Audio recording test completed.")


def test_audio_recording():
    audio_recording(Inputs.PLAY_DURATION)
