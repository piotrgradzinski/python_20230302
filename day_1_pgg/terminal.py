# import sys
# print(123)
#
# print(sys.argv)

import argparse

parser = argparse.ArgumentParser('terminal')
parser.add_argument('file', type=str, nargs='+', help='Paths for files to display')
parser.add_argument('-s', '--start-with', type=int, nargs=1, default=1, help='Start counting from. Default 1.')
parser.add_argument('-n', '--hide-line-numbers', action='store_true')

print(parser.parse_args())