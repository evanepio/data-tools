with open('historic_site_visits.csv') as csvFile:
    lines = csvFile.readlines()

    props = lines[0].strip().split(',')

    print("[")

    for line in lines[1:]:
        values = line.strip().split(",")
        print('{{"{0}": "{1}","{2}": "{3}","{4}": "{5}", "{6}": "{7}"}},'.format(props[0], values[0], props[1], values[1], props[2], values[2], props[3], values[3]))

    print("]")
