#!/usr/bin/env python3
"""
Reads from stdin line by line and computes metrics.
"""

import sys
import re
from collections import defaultdict

# Define expected status codes
VALID_STATUS_CODES = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Regex pattern to match valid log lines
log_pattern = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

# Initialize counters
total_size = 0
status_counts = defaultdict(int)
line_count = 0

def print_stats():
    """Print the accumulated stats."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code, file_size = match.groups()
            try:
                total_size += int(file_size)
                if status_code in VALID_STATUS_CODES:
                    status_counts[status_code] += 1
            except ValueError:
                continue  # skip lines with non-integer file size

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
