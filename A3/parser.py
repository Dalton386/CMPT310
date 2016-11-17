def parser(data, goals, rules):
    data_list = data.splitlines()
    goals.extend(data_list.pop(0).split())
    for meta in data_list:
        rule = meta.split()
        r = list()
        r.append(rule.pop(0))
        r.append(rule)
        rules.append(r)

