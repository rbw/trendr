# -*- coding: utf-8 -*-

import argparse
from os import path
from sys import stdout

from trendr import TrendChart, EventsReader, Date


def events_to_svg(events_file, *times):
    """Takes a file with a list of events:
    1428997830 False
    1428997921 False
    1428997947 True
    1428998025 False
    1428998051 False
    ...

    ...and produces a str representation of :class:`TrendChart`

    :param events_file: file containing events
    :returns: SVG chart
    """

    with open(events_file) as lines:
        reader = EventsReader(lines, *times)
        tc = TrendChart(
            reader,
            width=500,
            padding=1
        )

        return tc.__str__(), len(tc.states)


parser = argparse.ArgumentParser(description='SVG trend graph generator')
parser.add_argument('--input', type=str, help='input file containing events', required=True)
parser.add_argument('--output', type=str, help='SVG output file', required=True)
parser.add_argument('--start', type=int, help='Period start (Unix Timestamp)', required=True)
parser.add_argument('--end', type=int, help='Period end (Unix Timestamp)', required=True)

args = parser.parse_args()

with open(args.output, 'w') as output:
    start, end = map(Date, [args.start, args.end])

    summary = [
        '\n[ generating chart ]',
        'start: {0}',
        'end: {1}\n'
    ]

    stdout.write('\n'.join(summary).format(start.utc, end.utc))

    chart, state_cnt = events_to_svg(args.input, start.ts, end.ts)

    output.write(chart)
    stdout.write(
        '...done\n\nsuccess: {1} states ({0} bytes) written to: {2}\n'
        .format(path.getsize(args.output), state_cnt, args.output)
    )


