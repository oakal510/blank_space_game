import sys
import csv
import random


# This is a fun social game where a group of 3 or more friends suggest a word to complete a sentence with a blank space and
# then the friends vote on their favorite suggested word or phrase.


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f'{self.name}'

    def filler(self, filling):
        self.filling = filling

    def score_increment(self, n):
        self.score = self.score + n


def main():
    try:
        sentences = open_csv("assets/sentences.csv")
    except FileNotFoundError:
        sys.exit("This game cannot be loaded at this time.")

    number_of_rounds, game_players = initialize_game()

    for round in range(number_of_rounds):
        sentences = play_round(sentences)
        round_blank_space_filling(game_players)
        for player in game_players:
            print(f"Player {player} filled in with {player.filling}.")
        round_winner = score_round(game_players)
        if round < number_of_rounds:
            for player in game_players:
                print(f'After this round, Player {player.name} has a score of {player.score}.')
        # TODO: upddate to make this the final score
        else:
            for player in game_players:
                print(f'The final score for {player.name} is {player.score}.')

    # print(*game_players, sep="\n")


def open_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_contents.append(row)
        return csv_contents


def initialize_game():
    rounds_of_play = get_number_of_rounds()
    game_players = create_players(get_player_names(get_number_of_players()))
    return (rounds_of_play, game_players)


def get_number_of_rounds():
    while True:
        try:
            no_of_rounds = int(input("How many rounds do you want to play? "))
            if not 0 < no_of_rounds < 21:
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a valid number of rounds between 1 and 20.")
    return no_of_rounds


def get_number_of_players():
    while True:
        try:
            no_of_players = int(input("How many players are playing? "))
            if not 2 < no_of_players < 21:
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a valid number of players between 3 and 20.")
    return no_of_players


def get_player_names(number_of_players):
    names = []
    for _ in range(number_of_players):
        names.append(input("What is the player's name? ").title())
    return names


def create_players(player_names):
    all_players = []
    for player in player_names:
        player = Player(player)
        all_players.append(player)
    return all_players


def play_round(sentences):
    round_sentence = random.choice(sentences)
    print(*round_sentence)
    sentences.remove(round_sentence)
    return sentences


def round_blank_space_filling(players):
    for player in players:
        player.filler(input(f"What word or phrase did {player.name} choose to fill the blank space? "))
    return


def score_round(players):

    voted_player = {}
    for player in players:
        vote = input(f"Which player does {player.name} vote for this round? ").title()
        if any(player.name == vote for player in players):
            if vote in voted_player:
                voted_player[vote] += 1
            else:
                voted_player[vote] = 1

    top_score = max(voted_player.values())

    scoring_players = [player for player,score in voted_player.items() if score == top_score]

    if len(scoring_players) == 1:
        for player in players:
            if player.name in scoring_players:
                player.score_increment(2)
    else:
        for player in players:
            if player.name in scoring_players:
                player.score_increment(1)

if __name__ == "__main__":
    main()