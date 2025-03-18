import os
import pytest
from Core.common import run_command

"""This test case is to verify alsa configuration files are present ot it is using default settings"""

def test_check_alsa_config():
    #Check if ALSA configuration files exist and validate ALSA settings

    config_files = ["/etc/asound.conf", os.path.expanduser("~/.asoundrc")]
    missing_files = []

    for file in config_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"⚠️ Missing ALSA config files: {', '.join(missing_files)}")
    else:
        print("✅ ALSA configuration files exist.")

    result = run_command("aplay -L")

    if "default" not in result.stdout:
        pytest.fail("❌ ALSA default PCM device is not set. Check configuration!")

    print("✅ ALSA configuration files and settings are correct.")
