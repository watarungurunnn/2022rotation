import argparse
from pathlib import Path

from .src.input import simple_input
from .src.optimize import optimize_minoura, optimize_sakaguchi
from .src.output import simple_output


def main():
    parser = argparse.ArgumentParser(description='optimize rotation',)
    parser.add_argument('input_path', type=str, help='path to input file')
    parser.add_argument('-o','--output_dir', default='.', type=str, help='path to output directory')
    parser.add_argument('--name', help='name of output file')
    parser.add_argument('--model', default='Minoura', type=str, help='model to fit')
    args = parser.parse_args()

    simple_input()



if __name__ == '__main__':
    main()
