def create_key_value_json(key, value):
    return '"{0}": "{1}"'.format(key, value)


def create_single_object_json(keys, line):
    values = line.strip().split(',')

    json_chunks = [create_key_value_json(key, value) for key, value in zip(keys, values)]

    return '{{{0}}}'.format(', '.join(json_chunks))


def csv_lines_to_json(csv_lines):

    props = csv_lines[0].strip().split(',')

    individual_obj = [create_single_object_json(props, line) for line in csv_lines[1:]]

    return '[' + ',\n'.join(individual_obj) + ']'


def get_csv_lines(csv_file_name):
    with open(csv_file_name) as csv_file:
        return csv_file.readlines()


if __name__ == '__main__':
    lines = get_csv_lines('historic_site_visits.csv')
    json_array = csv_lines_to_json(lines)
    print(json_array)
