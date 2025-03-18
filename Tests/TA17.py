import pytest
from Core.common import run_command
from Core.common import Inputs

"""This test case is to verify that alsa rejects invalid ALSA device and checks for an error."""


@pytest.mark.xfail(reason="ALSA is expected to fail when using an invalid device.")
def test_invalid_alsa_device():

    invalid_device = "hw:99,0"
    audio_file = Inputs.AUDIO_FILE

    print(f"Attempting to play {audio_file} using invalid device {invalid_device}...\n")

    process = run_command(f"aplay -D {invalid_device} {audio_file}")

    print("=== ALSA Output ===")
    print(process.stderr)

    # Expected failure: ALSA should report an "audio open error"
    if "audio open error" in process.stderr.lower():
        pytest.xfail("⚠️ Expected failure: ALSA cannot open an invalid device.")

    assert False, "\n❌ Test failed unexpectedly: ALSA did not report an error for an invalid device"
