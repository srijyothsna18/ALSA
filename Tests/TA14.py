import subprocess
import time
import pytest
from Core.common import Inputs
from Core.common import run_command

"""This test case is to verify that aplay supports only wav files and uncompressed like mp3 files are not directly supported by aplay."""

def alsa_unsupported_format(audio_file, expected_to_fail=True):

    print(f"\nAttempting to play {audio_file} using aplay...\n")
    process = run_command(f"aplay -d {Inputs.PLAY_DURATION} {audio_file}")

    print("=== ALSA Output ===")
    print("STDOUT:", process.stdout.strip())
    print("STDERR:", process.stderr.strip())

    # Case 1: ALSA tries to play raw data instead of rejecting (wrong behavior)
    if "Playing raw data" in process.stderr:
        print("\n❌ ALSA misinterpreted the file as raw PCM. MP3 is NOT supported by aplay!")
        assert not expected_to_fail, "ALSA incorrectly handled an unsupported format (raw data misinterpretation)"

    # Case 2: Proper rejection
    elif "audio open error" in process.stderr or "Invalid" in process.stderr:
        print("\n✅ ALSA correctly rejected the unsupported format!")
        assert expected_to_fail, "ALSA correctly rejected the unsupported format!"

    # Case 3: Expected successful playback
    elif "Playing WAVE" in process.stderr:
        print("\n✅ ALSA successfully played the WAV file!")
        assert not expected_to_fail, "ALSA should have played this format successfully"

    # Case 4: No output (unexpected behavior)
    elif process.stdout.strip() == "" and process.stderr.strip() == "":
        print("\n⚠️ Unknown behavior: No output captured. Try running manually.")
        assert False, "No output captured, unknown ALSA behavior"

    # Case 5: Any other unexpected output
    else:
        print("\n⚠️ Unexpected output. Review manually.")
        assert False, f"Unexpected ALSA behavior: {process.stderr.strip()}"


@pytest.mark.xfail(reason="MP3 is not supported by ALSA aplay")
def test_alsa_mp3():
    alsa_unsupported_format(Inputs.MP3_FILE, expected_to_fail=True)  # Should fail, as MP3 is unsupported
    time.sleep(5)

def test_alsa_wav():
    alsa_unsupported_format(Inputs.WAV_FILE, expected_to_fail=False)  # Should succeed, as WAV is supported
    time.sleep(5)
