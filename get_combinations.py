import argparse
import csv

from itertools import combinations

"""
usage
python get_combinations.py -a 74 -b 114 -c 194 -r 1240 -e 5

a, b, c = values to make combinations of
r = maximum value
e - error in %. 5 = +- 5% (only positive)

"""


def get_combinations(a, b, c, result, error):

    for value in a, b, c, result, error:
        assert value > 0, 'Value should be positive. {}'.format(value)

    d = {}
    result_max = result * (1 + error / 100)
    result_min = result * (1 - error / 100)

    for number in a, b, c:
        max_divisor = result // number
        for index in range(max_divisor + 1):
            key = '{}*{}'.format(number, index)
            d[key] = number * index

    exhaustive_search = combinations(d, 3)

    # with open('result.txt', 'w') as f:
    #     for a, b, c in exhaustive_search:
    #         value = d[a] + d[b] + d[c]
    #         if result_min <= value <= result_max:
    #             c_error = (value - result) / result * 100
    #             f.write('{} + {} + {} = {} {:.0f}  ({:+.1f}%) \n'.
    #                     format(a, b, c, value, abs(value - result), c_error))

    with open('combinations.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['a', 'b', 'c', 'result', 'left', 'deviation (%)'])
        for a, b, c in exhaustive_search:
            value = d[a] + d[b] + d[c]
            if result_min <= value <= result_max:
                c_error = (value - result) / result * 100
                left = abs(value - result)
                writer.writerow([a, b, c, value, left, round(c_error, 1)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store', type=int, required=True,
                        help='First number of combination')
    parser.add_argument('-b', action='store', type=int, required=True,
                        help='Second number of combination')
    parser.add_argument('-c', action='store', type=int, required=True,
                        help='Third number of combination')
    parser.add_argument('-r', action='store', type=int, required=True,
                        help='Maximum value')
    parser.add_argument('-e', action='store', type=int, required=True,
                        help='Allowed deviation in %. E.g.: 5 = 5%')
    args = parser.parse_args()

    get_combinations(args.a, args.b, args.c, args.r, args.e)
