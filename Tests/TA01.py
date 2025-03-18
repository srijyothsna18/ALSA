from Core.common import run_command


"""This test case is to verify that ALSA and alsa-utils are installed properly in the system"""

def test_ALSA_Installation():
	result_library = run_command('dpkg -l | grep libasound')
	result_utilities = run_command('dpkg -l | grep alsa-utils')
	result = result_library.stdout + result_utilities.stdout 

	print("\nCommand Output:\n",result)
	assert "libasound" in result, "libasound is not installed on this system"
	assert " alsa-utils" in result, "alsa-utils is not installed on this system"
	print("ALSA is installed on this system")



