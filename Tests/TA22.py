from Core.common import run_command

"""This test case is to verify that alsa utils is installed"""

def test_aplay_version():
    result = run_command("aplay --version")
    print(result.stdout)
    if result.returncode == 0:
        print("ALSA installed sucessfully")
    else:
        print("No alsa utils")

