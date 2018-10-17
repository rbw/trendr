# -*- coding: utf-8 -*-

from datetime import datetime


class Date(object):
    def __init__(self, timestamp):
        """Helper for timestamp conversion

        :param timestamp: unix timestamp (str)
        """

        self.ts = timestamp

    @property
    def utc(self):
        return datetime.utcfromtimestamp(self.ts)


class Period(object):
    """Keeps track of a period"""
    def __init__(self, status, timestamp):
        self.status = status
        self.start = Date(timestamp)


class EventsReader(object):
    def __init__(self, lines, ts_start, ts_end):
        """Takes a list of events (lines) and produces states

        :param lines: Events iterable
        :param ts_start: Event window start
        :param ts_end: Event window end
        """

        self.lines = lines
        self.p_start = Date(ts_start)
        self.p_end = Date(ts_end)

    @property
    def states(self):
        """Expects a list of events in the following format:
        {Timestamp}\s{Status}\n

        :returns: (status, start, end)
        """

        last_ts = None
        period = Period(None, 0)

        for line in self.lines:
            timestamp = int(line[:10])
            status = line[11:].strip()

            # skip irrelevant lines
            if timestamp <= self.p_start.ts:
                continue
            elif timestamp >= self.p_end.ts:
                break

            # yield previous period, then create new
            if period.status != status:
                if last_ts:
                    # previous `Period` exists; yield
                    yield period.status, period.start, last_ts

                # Status has changed; create new Period to track it
                period = Period(status, timestamp)

            # store last TS for ref in next iteration
            last_ts = Date(timestamp)

        yield period.status, period.start, last_ts
