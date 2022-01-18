import argparse
from pathlib import Path

from .src.processor import simple_processor
from .src.optimizer import optimizer_minoura, optimizer_sakaguchi
from .src.output import simple_output


def main():
    parser = argparse.ArgumentParser(description='optimize rotation',)
    parser.add_argument('input_path', type=str, help='path to input file')
    parser.add_argument('-o','--output_dir', default='.', type=str, help='path to output directory')
    parser.add_argument('--name', help='name of output file')
    parser.add_argument('--model', default='Minoura', type=str, help='model to fit: Minoura, Sakaguchi')
    args = parser.parse_args()

    input_path = Path(args.input_path)

    # csv/excelを読み取って成形
    processor = simple_processor(input_path)

    # inputデータの成形とoptimize
    if args.model == 'Minoura':
        processed_data = processor.process()
        model = optimizer_minoura(processed_data)
    elif args.model == 'Sakaguchi':
        processed_data = processor.process()
        model = optimizer_sakaguchi(processed_data)

    optimized_data = model.fit()
    simple_output(optimized_data).save()

    return

if __name__ == '__main__':
    main()
