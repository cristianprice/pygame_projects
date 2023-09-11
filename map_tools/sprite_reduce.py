import pygame
import argparse
from utils import PyGameApp


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')


if __name__ == '__main__':
    args = parse_arguments()
