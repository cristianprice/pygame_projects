import argparse
from PIL import Image


def parse_args():
    parse = argparse.ArgumentParser('Remove Sprite Steps')
    parse.add_argument('--img', required=True) 
    parse.add_argument('--size', required=True) 
    parse.add_argument('--coord', required=True)     
    return parse.parse_args()

def backup_img(args):
    pass

def remove_sprite_parts(args):
    img = Image.open(args.img)
    print(img.size)

if __name__ == '__main__':
    args = parse_args()
    remove_sprite_parts(args)
    print('Done ...')