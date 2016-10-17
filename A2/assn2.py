#!python3.4
from FindNextVet_dgr import *
from heapq import *


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
csp[1] = [2,3,4,6,7,10]
csp[2] = [1,3,4,5,6]
csp[3] = [1,2]
csp[4] = [1,2]
csp[5] = [2,6]
csp[6] = [1,2,5,7,8]
csp[7] = [1,6,8,9,10]
csp[8] = [6,7,9]
csp[9] = [7,8,10]
csp[10] = [1,7,9]

vetset = [1,2,3,4,5,6,7,8,9,10]
vertcnt = 10
colocnt = 4

print(BacktrackSearch())


#csp is the graph of vertices, arcs and color domain
#vertcnt is the amount of vertices

#find the variable seems to fail (prune), find the value seem to success
#csp = (10,4,(1,2,3,4,6,7,10),(2,1,3,4,5,6),(3,1,2),(4,1,2),(5,2,6),(6,1,2,5,7,8),(7,1,6,8,9,10),(8,6,7,9),(9,7,8,10),(10,1,7 ,9))
'''
Function Backtracking-Search(csp) returns solution/failure
    return Recursive-Backtracking({ }, csp)

Function Recursive-Backtracking(assignment, csp) returns soln/failure
    if assignment is complete then return assignment
    var ←Select-Unassigned-Variable(Variables[csp], assignment, csp)
    for each value in Order-Domain-Values(var, assignment, csp) do
        if value is consistent with assignment given Constraints[csp] then
            add {var = value} to assignment
            result ←Recursive-Backtracking(assignment, csp)
            if result != failure then
                return result
            remove {var = value} from assignment
    return failure
'''
'''
Function AC-3(csp) returns the CSP, possibly with reduced domains
    inputs: csp a binary CSP with variables {X1, X2, . . . , Xn}
    local variables: queue a queue of arcs, initially all the arcs in csp
    while queue is not empty do
        (Xi, Xj) ←Remove-First(queue)
        if Remove-Inconsistent-Values(Xi, Xj) then
            for each Xk in Neighbors[Xi] do add (Xk , Xi) to queue

Function Remove-Inconsistent-Values(Xi, Xj) returns removed?
    removed? ←false
    for each x in Domain[Xi] do
        if no y ∈ Domain[Xj] allows (x,y) to satisfy the Xi, Xj constraint
            then delete x from Domain[Xi]; removed? ←true
    return removed?
'''