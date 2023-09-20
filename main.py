from game import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

def main():

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
