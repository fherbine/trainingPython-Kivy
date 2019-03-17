import pickle
from donnees import *
from random import Random

def pendu():
    player, player_score, scores = ask_player_name()
    secret_word = Random().choice(WORDS_LIST).upper()
    player_word = '*' * len(secret_word)
    max_try = MAX_TRY

    while max_try:
        player_word, max_try = check_input_letter(
            secret_word,
            player_word,
            max_try,
        )
        if player_word == secret_word:
            break

    final_score = get_final_score(player_score, max_try)
    write_score(player, final_score, scores)

def get_final_score(score, max_try):
    final_score = score + max_try
    print('You ended with the folowing score: {game_score}'.format(
        game_score=max_try,
    ))
    print('You have now {final_score} points.'.format(final_score=final_score))
    return final_score

def check_input_letter(secret_word, player_word, max_try):
    new_word = ''
    print('Here\'s the current discovered word: {word}'.format(
        word=player_word,
    ))
    letter = str(input('Type a letter: ')).upper()

    if letter in secret_word:
        print(
            'Well played the letter \'{letter}\' is in secret word !'.format(
                letter=letter,
            )
        )


    else:
        print('The letter {letter} isn\'t in secret word'.format(letter=letter))
        max_try -= 1

    for idx, ltr in enumerate(secret_word):
        if ltr == letter:
            new_word += ltr
            continue
        new_word += player_word[idx]

    return new_word, max_try

def ask_player_name():
    print('== Welcome on the pendu\'s game ==')
    player = str(input('What\'s your name ? '))
    player_score, scores = load_score(player)
    print('Mmmh.. Ok {player}, here\'s your current score: {score}'.format(
        player=player,
        score=player_score,
    ))
    return player, player_score, scores

def load_score(player):
    scores = {}
    with open('scores', 'ab+') as score_file:
        pass
    with open('scores', 'rb') as score_file:
        score_unpickler = pickle.Unpickler(score_file)
        try:
            scores = score_unpickler.load()
        except EOFError:
            pass

    return scores.get(player.upper(), 0), scores


def write_score(player, player_score, scores):
    if player.upper() in scores:
        scores[player.upper()] += player_score
    else:
        scores[player.upper()] = player_score

    with open('scores', 'wb+') as score_file:
        score_pickler = pickle.Pickler(score_file)
        scores = score_pickler.dump(scores)
