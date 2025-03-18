import subprocess
from Core.common import run_command

"""This test case is to verify alsa modules(drivers) are installed in the system properly"""

def test_check_alsa_modules():
    modules = ["snd_hda_intel", "snd_pcm",]
    result = run_command("lsmod")

    for module in modules:
        if module in result.stdout:
            print(f"✅ Module {module} is loaded.")
        else:
            print(f"❌ Module {module} is NOT loaded!")


