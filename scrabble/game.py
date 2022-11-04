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
    
    def verify(word:str):
        word = word.lower()
        for v_word in valid_words:
            if word == v_word:
                return True 
        
    def points(word: str):
        total = 0
        for letter in word:
            # print(f'{letter} = {Tile.points(letter)}')
            total += Tile.points(letter)
            
        return total
              
class Bag:
    
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
    
    def give_tiles():
        pass
    
class Player:
    def longest_word():
        pass

    def best_word():
        pass

    def best_triple_word():
        pass

def get_dictionary():
    path = '/Users/elizabeth/Documents/Projects/SigmaLabs/technical-tests/scrabble/dictionary.txt'
    dictionary = []
    with open(path) as file:
        dict_str = file.read()
        dictionary = dict_str.splitlines()
        # print(dictionary)
    
    return dictionary
        
def user_input():
    pass

def main():
#region tests
    # print(Tile.points('b'))
    # print(Word.verify('bob'))
    print(Word.points('bob'))
#endregion
    pass

if __name__ == '__main__':
    valid_words = get_dictionary()
    main()