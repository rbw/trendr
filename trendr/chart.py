# -*- coding: utf-8 -*-


class TrendChart(object):
    def __init__(self, reader, width=500, height=50, padding=1):
        """SVG trend chart API

        :param reader: Instance of :class:`EventsReader`
        :param width: Chart width
        :param padding: Bar padding
        """

        self.width = width
        self.height = height
        self.padding = padding
        self.reader = reader
        self.states = list(reader.states)
        self._start = reader.p_start
        self._end = reader.p_end

    @property
    def _width_ratio(self):
        """Returns width ratio used to scale the chart dynamically

        Calculates total bar width, including padding along with start-end delta in seconds.

        :returns: (chart_width - bars_width) / delta_secs
        """

        # Chart period in seconds
        delta_secs = float(self._end.ts - self._start.ts)

        # Bars min-width
        bars_width = len(self.states) * self.padding

        return float(self.width - bars_width) / delta_secs

    @property
    def head(self):
        """SVG header, styling etc"""

        r = self.reader
        utc_start = r.p_start.utc
        utc_end = r.p_end.utc

        return [
            "<?xml version='1.0' encoding='utf-8'?>",
            "<svg viewBox='0 0 {0} {1}' version='1.1' xmlns='http://www.w3.org/2000/svg'>"
            .format(self.width, self.height),
            "<text class='desc' x='50%' y='-5' alignment-baseline='middle' text-anchor='middle'>",
            "[{0} - {1}]".format(utc_start, utc_end),
            "</text>'",
            "<style>",
            ".desc {font-size: 40%; font-family: monospace;}",
            ".test:hover .bar {fill: blue; opacity: 0.6;}",
            "</style>"
        ]

    @property
    def body(self):
        """yields the actual chart content"""

        pos_x = 0

        for status, start, end in self.states:
            width = (end.ts - start.ts) * self._width_ratio + self.padding

            if status == 'True':
                color = 'green'
                tooltip_head = '[ STATUS: OK ]'
            else:
                color = 'red'
                tooltip_head = '[ STATUS: ERR ]'

            yield ''.join([
                "<g class='test'>",
                "<rect class='bar' x='{0}' y='0' width='{1}' height='50' fill='{2}'>"
                .format(pos_x, width, color),
                "<title>{0}\n\nStart: {1}\nEnd: {2}</title>"
                .format(tooltip_head, start.utc, end.utc),
                "</rect>",
                "</g>"
            ])

            pos_x += width

    @property
    def tail(self):
        return ["</svg>"]

    def __str__(self):
        """returns SVG str rep"""
        return ''.join(self.head + list(self.body) + self.tail)
