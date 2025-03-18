import os
from Core.common import run_command
from Core.common import Inputs
import pytest

"""This test case is to verify ALSA audio playback using a specific hardware device"""

def test_hw_audio_playback():

    device = Inputs.HARDWARE
    file = Inputs.AUDIO_FILE

    if not os.path.exists(file):
        pytest.fail(f"❌ Error: File '{file}' not found!")

    print(f"\n🎵 Attempting to play {file} using {device}...\n")
    process = run_command(f"aplay -D {device} {file}")

    print("=== ALSA Output ===\n")
    stdout_clean = process.stdout.strip()
    stderr_clean = process.stderr.strip()
    print(stdout_clean)
    print(stderr_clean)

    # Extract lowercase output for comparison
    stderr_lower = stderr_clean.lower()

    if "audio open error" in stderr_lower:
        pytest.fail("❌ ALSA failed to direct audio to the specified device!")
    elif "no such file or directory" in stderr_lower:
        pytest.fail("❌ Error: Audio file not found!")

    print("\n✅ ALSA successfully played the audio!")
