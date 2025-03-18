import pytest
from Core.common import Inputs
from Core.common import run_command

"""This test case attempts to play an audio file directly through ALSA hw:0,0 using hardware supported and unsupported sample rates"""


def play_audio_hw(audio_file, expected_warning=False):
    print(f"\n🎵 Attempting to play {audio_file} using direct ALSA (hw:0,0)...\n")

    process = run_command(f"aplay -D {Inputs.HARDWARE} {audio_file}")

    print("=== ALSA Output ===")
    print("STDOUT:", process.stdout.strip())
    print("STDERR:", process.stderr.strip())

    stderr_lower = process.stderr.lower()

    if "warning" in stderr_lower or "suggest using plug" in stderr_lower:
        print("✅ ALSA produced a warning and suggested using plug!")
        if expected_warning:
            pytest.xfail("⚠️ Expected failure: ALSA does not support this sample rate directly.")
        else:
            assert False, "Unexpected warning when playing supported audio"
    elif "audio open error" in stderr_lower or "invalid" in stderr_lower:
        print("❌ ALSA failed to open the device!")
        assert False, "ALSA failed to open the device (hw:0,0)"
    else:
        print("✅ No warning detected. The hardware supports this sample rate.\n")
        assert not expected_warning, "Expected a warning but didn't receive one"

def test_audio_supported():
    """Test with an audio file that has a supported sample rate"""
    play_audio_hw(Inputs.AUDIO_FILE, expected_warning=False)

@pytest.mark.xfail(reason="ALSA is expected to warn for unsupported sample rates.")
def test_audio_unsupported():
    """Test with an audio file that has an unsupported sample rate"""
    play_audio_hw(Inputs.AUDIO_FILE_96fs, expected_warning=True)
