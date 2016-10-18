import re


def parser(data, vetgraph):
    result = re.split('([\(\)])', data)
    split_result = list()

    for index, item in enumerate(result):
        if item == '(':
            split_result.append(result[index+1].split())

    for index, item in enumerate(split_result):
        for ix, i in enumerate(item):
            split_result[index][ix] = int(i)

    parse_result = split_result.pop(0)
    for item in split_result:
        vetgraph[item.pop(0)] = item
    parse_result.append(vetgraph)

    return parse_result







