def create_key_value_json(key, value):
    return '"{0}": "{1}"'.format(key, value)


def create_single_object_json(keys, line):
    values = line.strip().split(',')

    json_chunks = []
    for index in range(len(values)):
        json_chunks.append(create_key_value_json(keys[index], values[index]))

    return '{{{0}}}'.format(', '.join(json_chunks))


def csv_file_to_json_array(csv_file_name):
    individual_obj = []

    with open(csv_file_name) as csvFile:
        lines = csvFile.readlines()

        props = lines[0].strip().split(',')

        for line in lines[1:]:
            individual_obj.append(create_single_object_json(props, line))

    return '[' + ',\n'.join(individual_obj) + ']'


if __name__ == '__main__':
    json_array = csv_file_to_json_array('historic_site_visits.csv')
    print(json_array)
