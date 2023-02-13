from player import *


class Game:
    user = User()
    ai = Ai()
    user_board = user.own_board
    ai_board = ai.own_board
    ai_board.hid = True

    def greet(self):
        print("Welcome to the sea battle game (shitcode version)")
        self.user.name = input("What's your name? ")
        print(f"Hello {self.user.name}. At first, you need do place your ships")
        self.user.place_ships()
        self.user.clean_board()
        sleep(1)
        print("And now you have to wait. Skynet is uploading on every computer in the world...")
        self.ai.place_ships()
        self.ai.opponent_board.hid = True
        print("Let the fight begin!")

    def loop(self):
        turn = 0
        sequence = False
        while True:
            turn += 1
            if not sequence:
                sequence = not self.user.move(self.ai.own_board)
            else:
                sequence = self.ai.move(self.user.own_board)
                if not sequence:
                    print("Now is your turn, human!")
                sleep(1)

            if not self.ai.own_board.ships:
                print(f"Congratulation to you Human The Earth is saved by you {self.user.name},"
                      f" it took {turn} turns to beat Skynet")
                break
            elif not self.user.own_board.ships:
                print(f"The Earth is doomed, Skynet has just kicked your ass. It takes {turn} turns")
                break
            else:
                continue

        print("Thank you for playing! Have a nice day!")

    def start(self):
        self.greet()
        self.loop()


if __name__ == '__main__':
    game = Game()
    game.start()
