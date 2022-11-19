import pytest
from io import StringIO
from blank_space_game import open_csv, get_number_of_rounds, get_number_of_players, get_player_names


def test_open_csv():
    assert open_csv("test.csv") == [["test_item."], ["another_test_item."]]


def test_no_csv_to_open():
    with pytest.raises(FileNotFoundError):
        open_csv("fake_file.csv")


def test_get_number_of_rounds(monkeypatch):
    number_input = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert get_number_of_rounds() == 1
    number_input = StringIO('20\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert get_number_of_rounds() == 20


# need another function to test valueerror exception for number of rounds ... or break oup into two functions ???

def test_get_number_of_players(monkeypatch):
    number_input = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert get_number_of_players() == 3
    number_input = StringIO('20\n')
    monkeypatch.setattr('sys.stdin', number_input)
    assert get_number_of_players() == 20


# need another function to test valueerror exception for number of players ... or break oup into two functions ???

