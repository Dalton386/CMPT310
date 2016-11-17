#!python3.4
from parser import *


def backward_chaining(goals, rules):
    if goals == success:
        return True
    a = goals.pop(0)
    print("the next sub-goal is:", a)
    for r in rules:
        header = r[0]
        body = r[1]
        if header == a:
            print("the possible valid rule is: ", end="")
            if body:
                print(' ^ '.join(body), "->", header)
            else:
                print(header)

            if not goals.extend(body) and backward_chaining(goals, rules):
                print("successfully inferred with rule: ", end="")
                if body:
                    print(' ^ '.join(body), "->", header)
                else:
                    print(header)
                return True

            else:
                for b in body:
                    if b in goals:
                        goals.remove(b)

    print("cannot reason sub-goal")
    return failure

failure = list()
success = list()

if __name__ == '__main__':
    # goals = ['p', 'q', 'r']
    # rules = [['p', []],
    #          ['q', ['p']],
    #          ['r', ['p', 'q']],
    #          ['r', ['s']]]

    # filename = input("please enter the input filename: ")
    filename = "data.txt"
    with open(filename, 'r') as infile:
        data = infile.read()

    goals = list()
    rules = list()
    parser(data, goals, rules)
    print("the goal is:", ' ^ '.join(goals))
    print("the KB is: ")
    for r in rules:
        header = r[0]
        body = r[1]
        if body:
            print(' ^ '.join(body), "->", header)
        else:
            print(header)
    print("the reasoning process is: ")
    print("************************************************")

    if backward_chaining(goals, rules):
        print("************************************************")
        print("Success: the goal can be reasoned from KB")
    else:
        print("************************************************")
        print("Failure: the goal cannot be reasoned from KB")