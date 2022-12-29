import csv
import time
import os

from declat.bit_declat import BitDECLATRunner
from declat.bit_declat import get_max_support_value
from declat.readBitDataset import read_bit_data_set


def measure_time(path_to_dataset: str, min_support: int):
    print('Loading dataset')
    ds = read_bit_data_set(path_to_dataset)
    print('Finding support values in the database')
    bdr = BitDECLATRunner(ds, min_support)
    max_support_value = get_max_support_value(bdr.run())
    print('Max support value: ' + str(max_support_value))
    rows = list()
    for support in range(min_support, max_support_value + 1):
        print("Measuring time for support: " + str(support))
        start_time = time.process_time()
        bdr = BitDECLATRunner(ds, support)
        bdr.run()
        end_time = time.process_time()
        measured_time = (end_time - start_time) * 1000
        rows.append([support, measured_time])
        print("Measured time equals: " + str(measured_time) + " ms")

    print("Time measured for all support values")
    return rows


def save_result_to_csv(rows: dict, path_to_csv: str):
    fieldnames = ['support', 'time']
    print("Saving result to csv file under path: " + path_to_csv)
    os.makedirs(os.path.dirname(path_to_csv), exist_ok=True)
    with open(path_to_csv, 'w+', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            prepared_row = {"support": row[0], "time": row[1]}
            writer.writerow(prepared_row)

