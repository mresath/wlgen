import argparse
from itertools import product

def main(args: argparse.Namespace) -> int:

    file = args.file
    output = args.output
    depth = args.depth
    if not depth: depth = 2
    
    words = ""
    
    with open(file, 'r') as f:
        words = [line.strip() for line in f.readlines()]
    words += [word.upper() for word in words]
    
    if output:
        with open(output, 'w') as f:
            for word in product(words, repeat=depth):
                f.write(''.join(word) + '\n')
    else:
        print(''.join([''.join(word) + '\n' for word in product(words, repeat=depth)]))
    
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="wlgen",
        description="Generate a list of possible passwords based on given keyword file.",
    )
    parser.add_argument('file', metavar='file', type=str, help="File containing a list of keywords.")
    parser.add_argument('-o', '--output', type=str, help="File to output into (optional, will print out otherwise).")
    parser.add_argument('-d', '--depth', type=int, help="How many keywords to combine into each password, default and recommended value is 2.")
    args = parser.parse_args()
    
    exit(main(args))
