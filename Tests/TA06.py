import pytest
from Core.common import run_command

"""This test case verifies that the speakers are working by generating a 440 Hz sine wave test tone"""

def test_speaker_output():
    print("\n🔊 Running speaker-test to verify speaker functionality...")

    command = ["speaker-test -c 2 -t sine f 440 -l 1"]

    process = run_command(command)  # Using your function

    print("STDOUT:\n", process.stdout)
    print("STDERR:\n", process.stderr)

    assert process.returncode == 0, f"❌ speaker-test failed: {process.stderr}"
    assert "error" not in process.stderr.lower(), f"❌ Audio error: {process.stderr}"

    print("\n✅ Speaker test passed: 440 Hz sine wave played successfully!")
