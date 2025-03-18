import pytest
from Core.common import run_command
from Core.common import Inputs

"""This test case is to verify that ALSA rejects mono playback on a stereo-only device"""


def mono_playback_on_stereo(device, file_name, duration=10):

    print(f"\n🎵 Testing playback of {file_name} on {device} for {duration} seconds...")
    result = run_command(f"aplay -D {device} -d {str(duration)} {file_name}")

    print("=== ALSA Output ===")
    print("STDOUT:", result.stdout.strip())
    print("STDERR:", result.stderr.strip())

    stderr_lower = result.stderr.lower()
    stdout_lower = result.stdout.lower()

    # Check if ALSA rejects mono playback
    if "channels count non available" in stderr_lower:
        pytest.xfail(f"⚠️ Expected failure: ALSA rejected mono playback on {device} for {file_name}.")

    print(f"✅ ALSA played audio for {duration} seconds on {device}.")

    # Ensure stereo playback confirmation
    if file_name == Inputs.WAV_FILE:
        assert "stereo" in stdout_lower or "stereo" in stderr_lower, \
            f"❌ Test failed: Expected 'stereo' in output for {file_name}, but found:\n{stdout_lower}\n{stderr_lower}"


@pytest.mark.xfail(reason="Mono playback is expected to fail on a stereo-only device.")
def test_mono():
    mono_playback_on_stereo(Inputs.HARDWARE, Inputs.AUDIO_FILE_MONO, Inputs.PLAY_DURATION)


def test_stereo():
    mono_playback_on_stereo(Inputs.HARDWARE, Inputs.WAV_FILE, Inputs.PLAY_DURATION)
