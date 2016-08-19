import sys, json, csv


def get_keys_and_values_list(csv_file_name):
    all_rows = []
    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file, dialect='excel')
        for row in reader:
            all_rows.append(row)
    return all_rows[0], all_rows[1:]


if __name__ == '__main__':
    keys, values_list = get_keys_and_values_list(sys.argv[1])
    objects = [dict(zip(keys, values)) for values in values_list]
    print(json.dumps(objects, indent=4, separators=(',', ': ')))
