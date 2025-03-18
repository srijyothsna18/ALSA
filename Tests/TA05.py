import time
import pytest
from Core.common import run_command
from Core.common import Inputs

"""This test case is to verify that mute/unmute functionality of a master and headphone using amixer utility provided by alsa-utils"""

def mute_unmute(control, mute):
    status = "mute" if mute else "unmute"
    run_command(f"amixer set {control} {status}")
    print(f"{control} is now {'Muted' if mute else 'Unmuted'}")

@pytest.mark.parametrize("control", ["Master", "Headphone"])
def test_audio(control):
    print(f"\n===Testing {control} Mute/Unmute===")

    mute_unmute(control, True)
    print(f"Playing audio when {control} is muted")
    run_command(f"aplay {Inputs.AUDIO_FILE}")
    time.sleep(2)

    mute_unmute(control, False)
    print(f"Playing audio when {control} is unmuted")
    run_command(f"aplay {Inputs.AUDIO_FILE}")
    time.sleep(2)

    print(f"{control} Mute/Unmute Test Completed.\n")
