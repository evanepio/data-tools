import sys, json, csv


def get_rows_from_csv_file(csv_file_name):
    all_rows = []
    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file, dialect='excel')
        for row in reader:
            all_rows.append(row)
    return all_rows


if __name__ == '__main__':
    rows = get_rows_from_csv_file(sys.argv[1])
    objects = [dict(zip(rows[0], current_row)) for current_row in rows[1:]]
    print(json.dumps(objects, indent=4, separators=(',', ': ')))
