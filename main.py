import random


class RPS:
    options = ['rock', 'paper', 'scissors']
    won = lost = draw = 0

    def __init__(self):
        while self.play_game():
            random_choice = random.choice(self.options)

            answer = self.print_question()

            if self.validate_answer(answer):
                answer = int(answer)
                print(self.parse_answer(self.options[answer], random_choice))
            else:
                print('That option is not correct')

        self.output_result(self.won, self.lost, self.draw)

    def play_game(self):
        a = input('Do you want to play a RPS [y or n] > ').lower()

        if a == 'y':
            return True
        else:
            return False

    def print_question(self):
        for i in range(0, len(self.options)):
            print("Choose {0} for {1}".format(i, self.options[i]))
        print('> ', end=' ')

        ans = input()
        return ans

    def validate_answer(self, ans):
        if int(ans) in range(0, len(self.options)):
            return True
        return False

    def parse_answer(self, option, rand_choice):
        self.print_choice(option, rand_choice)

        if option == rand_choice:
            self.draw += 1
            return 'Golly its a tie, you cant defeat each other\n'
        else:
            return self.can_defeat(option, rand_choice)

    def can_defeat(self, answer, rand):
        defeat = {
            'rock': ['scissors', 'crush'],
            'paper': ['rock', 'wrap'],
            'scissors': ['paper', 'cut']
        }

        if defeat[answer][0] == rand:
            self.won += 1
            return 'you win because {} will {} {}\n'.format(answer, defeat[answer][1], rand)
        else:
            self.lost += 1
            return 'you lose because {} cannot {} {}\n'.format(answer, defeat[answer][1], rand)

    def print_choice(self, option, rand):
        p = "you chose *{}* and the computer chose *{}*".format(option, rand)
        k = self.print_line(p)

        print(p + "\n" + k)

    def print_line(self, word):
        i = 0
        k = ''

        while i < len(word):
            k += '='
            i += 1

        return k

    def output_result(self, won, lost, draw):
        wrapper = "\nBye-bye, see you later"
        total = won + lost + draw

        goodbye = 'Played: {}\n'
        goodbye += 'Won: {} (' + self.percent(won, total) + ')\n'
        goodbye += 'Lost: {} (' + self.percent(lost, total) + ')\n'
        goodbye += 'Draw: {} (' + self.percent(draw, total) + ')\n'
        goodbye = goodbye.format(total, won, lost, draw) + self.print_line(wrapper) + wrapper

        print(goodbye)

    def percent(self, val, total):
        return '{:.2f}%'.format((val/total) * 100)

rps = RPS()