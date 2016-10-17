from heapq import *


def FindNextVet(assignment, vetset, remainval, csp):
    vetheap = list()
    for vet in vetset:
        if vet not in assignment.keys():
            heappush(vetheap,(- len(csp[vet]),vet))
    return heappop(vetheap)[1]