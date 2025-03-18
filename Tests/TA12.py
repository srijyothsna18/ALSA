import subprocess
from Core.common import run_command


"""This test case is to verify that there are no errors related to alsa in the system logs"""

def test_check_alsa_system_logs():
    command = ["dmesg"]
    result = run_command(command)

    # ALSA-related keywords
    alsa_keywords = ["alsa", "snd_", "hda_intel", "hda_codec", "pcm", "ac97"]
    error_keywords = ["error", "failed", "not found", "unable to", "no such device"]

    alsa_logs = [line for line in result.stdout.split("\n") if any(alsa in line.lower() for alsa in alsa_keywords)]
    alsa_errors = [line for line in alsa_logs if any(err in line.lower() for err in error_keywords)]

    if alsa_errors:
        print("❌ ALSA-related errors found in system logs:")
        for error in alsa_errors:
            print(f"   - {error}")
    else:
        print("\n✅ No ALSA-related errors found in system logs.")

