# def algo():
#     # closedSet = {}
#
#     openSet = set()
#     openSet.append(nummer())
#     while not bool(openSet):
#         if er_utgang():
#             gaa_ut()
#             exit()
#         n = nummer()
#         plukk_opp()
#         openSet.remove(n)
#         # closedSet.append(n)
#
#         if n+n-1 not in openSet:
#             openSet.append(n+n-1)
#         if 2*n not in openSet:
#             openSet.append(2n)


# def df(node):
#     if node is not None:
#         df(node.left)
#         df(node.right)
#         print(node.value)
n = nummer()
print(n)
def df(n):
    if n is not None:
        df(2*n+1)
        df(2*n)
        print(nummer())
df(n)
