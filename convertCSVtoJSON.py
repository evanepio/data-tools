import sys, json


def create_object_from_csv_line(keys, line):
    values = line.strip().split(',')

    return dict(zip(keys, values))


def create_array_of_objects_from_csv_lines(csv_lines):
    object_properties = csv_lines[0].strip().split(',')

    return [create_object_from_csv_line(object_properties, line) for line in csv_lines[1:]]


def get_csv_lines(csv_file_name):
    with open(csv_file_name) as csv_file:
        return csv_file.readlines()


if __name__ == '__main__':
    lines = get_csv_lines(sys.argv[1])
    json_array = create_array_of_objects_from_csv_lines(lines)
    print(json.dumps(json_array, indent=4, separators=(',', ': ')))
