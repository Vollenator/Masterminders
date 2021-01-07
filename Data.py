
class MastermindData:

    def __init__(self):
        self.buffer = 'buffer'

    def check(self, code, guess):
        for i in range(4):
            if code[i] == guess[i]:
                guess[i] = 'check'

            if guess[i] == code[0] or guess[i] == code[1] or guess[i] == code[2] or guess[i] == code[3]:
                guess[i] = 'half'

            if guess[i] != 'check' and guess[i] != 'half':
                guess[i] = 'wrong'
        return guess

