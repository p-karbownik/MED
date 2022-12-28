from time_measure import measure_time
from time_measure import save_result_to_csv


def main():
    dataset_paths = [['ksiazki.csv', 1],
                     ['movies.csv', 1],
                     ['muzyka.csv', 24],
                     ['politics.csv', 1],
                     ['cinema.csv', 2]]

    for p in dataset_paths:
        rows = measure_time("../dataset/" + p[0], p[1])
        save_result_to_csv(rows, "../results/time/" + p[0])


if __name__ == '__main__':
    main()
