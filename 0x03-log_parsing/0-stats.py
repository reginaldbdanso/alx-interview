#!/usr/bin/python3
"""Log parsing"""
import sys


class LogParser:
    """Log parsing class"""
    def __init__(self):
        """Constructor function for LogParser class"""
        self.status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }
        self.file_size = 0
        self.line_count = 0

    def parse_line(self, line):
        """ Read, parse and grab data"""
        try:
            parsed_line = line.split()
            # print(parsed_line, len(parsed_line))
            if len(parsed_line) < 9 or parsed_line[-2] is None or\
                    parsed_line[-1] is None:
                return 0
            status_code = parsed_line[-2]
            if status_code in self.status_codes:
                self.status_codes[status_code] += 1
            return int(parsed_line[-1])
        except Exception as e:
            return 0

    def print_stats(self):
        """print stats in ascending order"""
        print("File size: {}".format(self.file_size))
        for key in sorted(self.status_codes.keys()):
            if self.status_codes[key]:
                print("{}: {}".format(key, self.status_codes[key]))

    def reset_status_codes(self):
        """reset stats"""
        self.status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }

    def process_logs(self):
        try:
            for line in sys.stdin:
                self.file_size += self.parse_line(line)
                self.line_count += 1
                if self.line_count % 10 == 0:
                    self.print_stats()
                    self.reset_status_codes()

        except KeyboardInterrupt:
            self.print_stats()
            self.reset_status_codes()
            raise


if __name__ == "__main__":
    log_parser = LogParser()
    log_parser.process_logs()
