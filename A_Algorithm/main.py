from tkinter import SEL
import pygame
from maze import SearchSpace
from algos import DFS, BFS
from const import RES, GREY
import argparse

def main(algo:str):
    your_name = 'A* algorithms'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')
    sc = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(GREY))

    g = SearchSpace()
    g.draw(sc)
    clock.tick(200)

    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    else:
        raise NotImplementedError('Not implemented')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__=='__main__':
    print("Select: ")
    print("  DFS")
    print("  BFS")
    print("------------------------------------------")

    while True:
        select = (input("Input select: "))
        select = select.upper()

        if select in ['DFS', 'BFS']:
            main(select)
        else:
            print("Invalid selection. Please enter 'DFS' or 'BFS'.")
            break


        parser = argparse.ArgumentParser(description='Search algorithms')
        parser.add_argument('--algo', type=str, help='Enter search algorithm', default = select)

        args = parser.parse_args()
        main(args.algo)