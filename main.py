import re
import argparse
import json

REGEX = '[a-zA-Z0-9-_/.]*.php:[0-9]{2,4}'

def get_file_lines(filepath):
    with open(filepath,'r',encoding='ISO-8859-1') as file:
        content = file.read()
    return re.findall(REGEX, content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Xdebug file path')
    parser.add_argument('output', help='output file')
    args = parser.parse_args()
    result = get_file_lines(args.filepath)
    with open(args.output, 'w+') as file:
        json.dump(result, file, indent=4)