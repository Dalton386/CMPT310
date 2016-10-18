from heapq import heappop,heappush


def FindNextVet(assignment, vetset, remainval, csp):
    vetheap = list()
    for vet in vetset:
        if vet not in assignment.keys():
            heappush(vetheap,(len(remainval[vet]),vet))
    return heappop(vetheap)[1]