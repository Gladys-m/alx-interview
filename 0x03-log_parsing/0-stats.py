#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys


def print_stats(total_size, status_counts):
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{:d}: {:d}".format(status_code, status_counts[status_code]))


def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0,
                     405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.strip().split()

            if len(data) >= 9:
                ip_address = data[0]
                status_code = int(data[-2])
                file_size = int(data[-1])

                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
