def libraryFine(returndate, duedate):
    if returndate[2] < duedate[2]: return 0 #year check
    if returndate[2] > duedate[2]: return 10000
    if returndate[1] < duedate[1]: return 0 #month check
    if returndate[1] > duedate[1]: return 500 * (returndate[1] - duedate[1])
    if returndate[0] < duedate[0]: return 0 #day check
    if returndate[0] > duedate[0]: return 15 * (returndate[0] - duedate[0])
    else: return 0

if __name__ == '__main__':
    returndate = [int(i) for i in input().strip().split()]
    duedate = [int(i) for i in input().strip().split()]
    print(libraryFine(returndate, duedate))
