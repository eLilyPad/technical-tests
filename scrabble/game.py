
from rich.prompt import Prompt
from itertools import permutations
import random


class Tile:
    _points_charts = {
        1: ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H','V','W','Y'],
        5: ['K'],
        8: ['J','X'],
        10: ['Q','Z'],
    }
    
    def points(letter: str):
        for score, letters in Tile._points_charts.items():
            lower = list(map(lambda l: l.lower(), letters))
            if letter in lower:
                return score 
            
        return 0 #TODO: Invalid Letter

class Word:
    
    def verify(word: str):
        word = word.lower()
        for v_word in valid_words:
            if word == v_word:
                return True 
        
    def points(word: str):
        total = 0
        word = word.lower()
        for letter in word:
            total += Tile.points(letter)
            
        return total
              
class Bag:
    """the chance for a letter to be generated given as a percentage"""
    _distribution = {
        27: ['E'],
        20: ['A','I'],
        18: ['O'],
        13: ['N','R','T'],
        9: ['L','S','U','D'],
        7: ['G'],
        4: ['B','C','M','P','F','H','V','W','Y'],
        2: ['K','J','X','Q','Z'],
    }
    
    def give_tiles(amount = 7):
        tiles = []
        for i in range(amount):
            tiles.append(Bag._get_tile())
            
        return tiles
        
    def _get_tile():
        chance = list(Bag._distribution.keys())
        all_letters = list(Bag._distribution.values())
        letters = random.choices(all_letters, chance, k=1) [0]
        
        ## not needed
        if len(letters) == 1:
            return letters[0]
        else:
        ##
            return random.choice(letters)
        # for chance, letters in Bag._distribution.items():
    
class Player:
    def longest_word(letters: list):
        for i in range(len(letters),0, -1):
            print ("Checking against words of length %d" % i)
            pool = permutations(letters, i) 
            for comb in pool:
                word = ''.join(comb)
                if Word.verify(word):
                    return word
                
        return ''

    def best_word(letters: list):
        best_score = 0
        for i in range(len(letters),0, -1):
            print ("Checking against words of length %d" % i)
            pool = permutations(letters, i) 
            for comb in pool:
                word = ''.join(comb)
                if Word.verify(word):
                    score = Word.points(word)
                    print (f'Valid: {word} score = {score}')
                    if score > best_score:
                        return word #TODO: not returning best score just first verified word
                
        return ''

    # def best_triple_word(letters: lists):
    #     best_score = 0
    #     for i in range(len(letters),0, -1):
    #         print ("Checking against words of length %d" % i)
    #         pool = permutations(letters, i) 
    #         for comb in pool:
    #             word = ''.join(comb)
    #             if Word.verify(word):
    #                 score = Word.points(word)
    #                 print (f'Valid: {word} score = {score}')
    #                 if score > best_score:
    #                     return word
                
    #     return ''

def get_dictionary():
    # TODO: change to relative path
    path = '/Users/elizabeth/Documents/Projects/SigmaLabs/technical-tests/scrabble/dictionary.txt'
    dictionary = []
    with open(path) as file:
        dict_str = file.read()
        dictionary = dict_str.splitlines()
        # print(dictionary)
    
    return dictionary
        
def user_input():
    input = Prompt.ask('Enter A word:')
    
    is_valid = Word.verify(input)
    while not is_valid:
        print('Invalid word')
        input = Prompt.ask('Enter A word:')
        is_valid = Word.verify(input)
        
    return input

def main():
#region tests
    # print(Tile.points('b'))
    # print(Word.verify('bob'))
    # print(Word.points('TEE'))
    # print(Bag.give_tiles(5))
    # print(Player.best_word(Bag.give_tiles(5)))
    available_tiles = Bag.give_tiles(7)
    print(available_tiles)
    word = user_input()
    print(f'You scored {Word.points(word)}')
    print(f'The best score was {Player.best_word(available_tiles)}')
#endregion
    pass

if __name__ == '__main__':
    valid_words = get_dictionary()
    main()
