#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(total_size, status_codes):
    """Prints stats"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parses a line"""
    parts = line.split()
    if len(parts) < 7:
        return None
    ip, _, _, _, status_code, file_size = parts[:6]
    if not status_code.isdigit():
        return None
    return ip, int(status_code), int(file_size)


def process_logs():
    """Processes logs"""
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed is None:
                continue
            ip, status_code, file_size = parsed
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise KeyboardInterrupt


if __name__ == "__main__":
    process_logs()
