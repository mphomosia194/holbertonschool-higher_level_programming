#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file data to JSON and save it in data.json."""
    try:
        with open(csv_filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
