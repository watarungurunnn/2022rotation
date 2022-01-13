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
    parser.add_argument('--model', default='Minoura', type=str, help='model to fit: Minoura, Sakaguchi')
    args = parser.parse_args()

    input_path = Path(args.input_path)
    input_data = simple_input(input_path).process()

    if args.model == 'Minoura':
        model = optimize_minoura(input_data)
    elif args.model == 'Sakaguchi':
        model = optimize_sakaguchi(input_data)
    opt_data = model.fit()
    simple_output(opt_data).save()

    return

if __name__ == '__main__':
    main()
