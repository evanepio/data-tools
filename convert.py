def create_key_value_json(key, value):
    return '"{0}": "{1}"'.format(key, value)


def print_json(csv_file_name):
    with open(csv_file_name) as csvFile:
        lines = csvFile.readlines()

        props = lines[0].strip().split(',')

        print("[")

        for line in lines[1:]:
            values = line.strip().split(",")

            json_chunks = []
            for index in range(len(values)):
                json_chunks.append(create_key_value_json(props[index], values[index]))

            print('{{{0}}}'.format(', '.join(json_chunks)))

        print("]")


if __name__ == '__main__':
    print_json('historic_site_visits.csv')
