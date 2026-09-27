import csv


class CSVReader:

    @staticmethod
    def read_csv(file_path):

        data = []

        with open(
            file_path,
            "r",
            encoding="utf-8",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        return data