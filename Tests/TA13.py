import subprocess
import pytest
from Core.common import run_command

"""This test case is to verify ALSA's behavior when attempting to play a non-existent file"""


@pytest.mark.xfail(reason="ALSA is expected to fail when attempting to play a non-existent file.")
def test_non_existent_file_should_fail():
    file_name = "does_not_exist.wav"
    print(f"\nAttempting to play {file_name} using aplay...\n")

    process = run_command("aplay", file_name)

    print("=== ALSA Output ===\n")
    print("STDOUT:", process.stdout.strip())
    print("STDERR:", process.stderr.strip())

    # Expecting an error because the file does not exist
    if "No such file or directory" in process.stderr:
        pytest.xfail("⚠️ Expected failure: File does not exist.")

    assert False, "\n❌ Test failed unexpectedly: ALSA did not report a missing file."

