import pytest
import re
from Core.common import run_command

"""This test case is to verify changes made to master volume percentage reflects correctly using amixer properly"""

def set_volume(percentage):
    #Set the Master volume to a specified percentage
    result = run_command("amixer get Master")

    match = re.search(r"Mono: Playback (\d+) \[([0-9]+)%\]", result.stdout)
    if match:
        current_volume = int(match.group(2))
        print(f"Current volume is {current_volume}%")
    else:
        print("❌ Could not extract current volume.")
        return None

    if 0 <= percentage <= 100:
        result = run_command(f"amixer set Master {percentage}%")
        print(f"===🔊 Master volume set to {percentage}% ===\n", result)

        result = run_command("amixer get Master")
        match = re.search(r"Mono: Playback (\d+) \[([0-9]+)%\]", result.stdout)
        if match:
            new_volume = int(match.group(2))
            return new_volume
        else:
            print("❌ Could not verify volume.")
            return None
    else:
        print("❌ Invalid volume percentage! Enter a value between 0 and 100.")
        return None


def test_set_volume():
    percentage = 10
    new_volume = set_volume(percentage)
    assert new_volume == percentage, f"❌ Volume mismatch! Expected {percentage}%, but got {new_volume}%."
    print(f"✔️ Volume successfully set to {new_volume}%")

