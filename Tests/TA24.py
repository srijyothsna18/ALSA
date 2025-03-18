import pytest
from Core.common import run_command
from Core.common import Inputs

"""This test case is to verify that recording with S24_LE format is expected to fail as hardware doesn't support it."""


@pytest.mark.xfail(reason="Hardware does not support S24_LE format")
def test_recording_s24_le():
    device = Inputs.HARDWARE
    filename = "test_hw.wav"
    duration = Inputs.PLAY_DURATION

    print(f"\n🎙️ Attempting to record with {device} using S24_LE format...")

    command = f"arecord -D {device} -d {duration} -f S24_LE -r 96000 -c 2 -t wav {filename}"
    result = run_command(command)

    print("=== ALSA Output ===")
    print("STDOUT:", result.stdout.strip())
    print("STDERR:", result.stderr.strip())

    # Fail the test explicitly if the error message is present
    if "Sample format non available" in result.stderr:
        pytest.fail("❌ Expected failure: Hardware does not support S24_LE format")
