from Core.common import run_command


"""This test case is to verify that aplay list the available playback devices properly"""


def get_sound_cards():
    result = run_command('aplay -l')
    cards = [line for line in result.stdout.split('\n') if "card" in line]
    return result.returncode, cards


def test_sound_card_recog():
    returncode, cards = get_sound_cards()

    for card in cards:
        print("\n", card, "\n")

    assert returncode == 0, "No sound cards present"
