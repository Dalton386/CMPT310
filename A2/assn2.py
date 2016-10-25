#!python3.4
import time
from parser import *
from heapq import heappop,heappush


def FindNextVet_mrv(assignment, vetset, remainval):
    vetheap = list()
    vetlist = list()
    for vet in vetset:
        if vet not in assignment.keys():
            heappush(vetheap,(len(remainval[vet]),vet))
    vetlist.append(heappop(vetheap)[1])
    while vetheap:
        vetitr = heappop(vetheap)
        if vetitr[0] == len(remainval[vetlist[0]]):
            vetlist.append(vetitr[1])
        else:
            break

    return vetlist


def FindNextVet_dgr(assignment, vetset, csp):
    vetheap = list()
    for vet in vetset:
        if vet not in assignment.keys():
            heappush(vetheap,(- len(csp[vet]),vet))
    return heappop(vetheap)[1]


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


def BacktrackSearch():
    assignment = dict()
    return RecursiveBS(assignment)


def RecursiveBS(assignment):
    if len(assignment) == vertcnt :
        return assignment
    remainval = GetRV(assignment)
    vetlist = FindNextVet_mrv(assignment,vetset,remainval)
    if len(vetlist) == 1:
        vet = vetlist[0]
    else:
        vet = FindNextVet_dgr(assignment,vetlist,csp)
    value = LCV(vet,remainval)
    for val in value:
        # if IsArcConsistency(vet,val):
        assignment[vet] = val
        result = RecursiveBS(assignment)
        if result != failure:
            return result
        assignment.pop(vet,0)
    return failure


def naiveBacktrackSearch():
    assignment = dict()
    return RecursiveBS(assignment)


def naiveRecursiveBS(assignment):
    if len(assignment) == vertcnt :
        return assignment
    vet = vetset.pop()
    value = csp[vet]
    for val in value:
        # if IsArcConsistency(vet,val):
        assignment[vet] = val
        result = RecursiveBS(assignment)
        if result != failure:
            return result
        assignment.pop(vet,0)
    return failure


failure = dict()
csp = dict()
answer = dict()
naive_answer = dict()
vetset = list()
REPEATTIME = 10000

if __name__ == '__main__':
    # filename = input("please enter the data filename: ")
    filename = "textfile.txt"
    with open(filename, "r") as datafile:
        data = datafile.read().replace('\n', '')

    parse_result = parser(data, csp)

    vertcnt = parse_result[0]
    colocnt = parse_result[1]
    for item in csp.keys():
        vetset.append(item)

    startime = time.time()
    for i in range(REPEATTIME):
        vetset = list()
        for item in csp.keys():
            vetset.append(item)
        answer = BacktrackSearch()
    duratime = time.time() - startime

    startime = time.time()
    for i in range(REPEATTIME):
        vetset = list()
        for item in csp.keys():
            vetset.append(item)
        naive_answer = BacktrackSearch()
    naive_duratime = time.time() - startime

    if answer and naive_answer:
        print("Note: each negative number means a kind of color")
        print("REPEATTIME is ", REPEATTIME)
        print("with heuristic\n",answer)
        print("time consumption: ",duratime)
        print("without heuristic\n",naive_answer)
        print("time consumption: ", naive_duratime)
    else:
        print("Cannot paint this map!")


