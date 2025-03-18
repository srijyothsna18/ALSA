import re
import pytest
from Core.common import run_command

"""This test case is to verify volume increase/decrease is perfectly set  using amixer utility"""

def get_current_volume():
    result = run_command("amixer get Master")
    match = re.search(r"Mono: Playback (\d+) \[([0-9]+)%\]", result.stdout)
    if match:
        return int(match.group(2))
    else:
        print("❌ Could not extract current volume.")
        return None


def change_volume(amount, increase=True):
    current_volume = get_current_volume()
    if current_volume is None:
        pytest.fail("❌ Failed to get current volume")

    operation = "+" if increase else "-"
    result = run_command(f"amixer sset Master {amount}%{operation}")
    action = "increased" if increase else "decreased"
    print(f"\n🔊 Master volume {action} by {amount}%")
    print(result)

    new_volume = get_current_volume()
    if new_volume is None:
        pytest.fail("❌ Failed to verify the new volume.")


    if increase:
        expected_volume = current_volume + amount + 1
    else:
        expected_volume = current_volume - amount - 1

    assert new_volume == pytest.approx(expected_volume, abs=1), f"❌ Volume mismatch! Expected {expected_volume}%, but got {new_volume}%."
    print(f"✔️ Volume successfully {action} to {new_volume}%")


def test_increase_volume():
    change_volume(20, increase=True)

def test_decrease_volume():
    change_volume(10, increase=False)
