def create_key_value_json(key, value):
    return '"{0}": "{1}"'.format(key, value)


def create_single_object_json(keys, line):
    values = line.strip().split(',')

    json_chunks = []
    for index in range(len(values)):
        json_chunks.append(create_key_value_json(keys[index], values[index]))

    return '{{{0}}}'.format(', '.join(json_chunks))


def csv_file_to_json_array(csv_lines):
    individual_obj = []

    props = csv_lines[0].strip().split(',')

    for line in csv_lines[1:]:
        individual_obj.append(create_single_object_json(props, line))

    return '[' + ',\n'.join(individual_obj) + ']'


def get_csv_lines(csv_file_name):
    with open(csv_file_name) as csv_file:
        return csv_file.readlines()


if __name__ == '__main__':
    csv_lines = get_csv_lines('historic_site_visits.csv')
    json_array = csv_file_to_json_array(csv_lines)
    print(json_array)
