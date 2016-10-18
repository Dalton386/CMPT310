#!python3.4
import sys
from parser import *


def BacktrackSearch():
    assignment = dict()
    return RecursiveBS(assignment)


def RecursiveBS(assignment):
    if len(assignment) == vertcnt :
        return assignment
    remainval = GetRV(assignment)
    vet = FindNextVet(assignment,vetset,remainval,csp)
    value = LCV(vet,remainval)
    for val in value:
        # if IsArcConsistency(vet,val):
        assignment[vet] = val
        result = RecursiveBS(assignment)
        if result != failure:
            return result
        assignment.pop(vet,0)
    return failure


def LCV(vet,remainval):
    lcvalue = list()
    lcvheap = list()
    value = remainval[vet]
    for val in value:
        adjcnt = 0
        for adjvet in csp[vet]:
            if val in remainval[adjvet]:
                adjcnt += 1
        heappush(lcvheap,(adjcnt,val))
    while lcvheap:
        lcvalue.append(heappop(lcvheap)[1])
    return lcvalue


def GetRV(assignment):
    remainval = dict()
    for vet in vetset:
        remainval[vet] = list()
        for rv in range(-colocnt, 0):
            remainval[vet].append(rv)

    for vet in assignment.keys():
        value = assignment[vet]
        remainval[vet].remove(value)
        for adjvet in csp[vet]:
            if value in remainval[adjvet]:
                remainval[adjvet].remove(value)

    return remainval

failure = dict()
csp = dict()
vetset = list()

if __name__ == '__main__':
    filename = input("please enter the data filename: ")
    with open(filename, "r") as datafile:
        data = datafile.read().replace('\n', '')

    parse_result = parser(data, csp)

    vertcnt = parse_result[0]
    colocnt = parse_result[1]
    for item in csp.keys():
        vetset.append(item)

    hmode = input('test with MRV: please enter \'m\'\n'
                  'test with degree: please enter \'d\'\n')
    if hmode == 'm':
        from FindNextVet_mrv import *
    elif hmode == 'd':
        from FindNextVet_dgr import *
    else:
        print("the test mode is illegal")
        sys.exit()

    print(BacktrackSearch())


