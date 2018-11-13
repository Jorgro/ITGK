<<<<<<< current

# k = int(input('Hvilket ledd? '))
# f = [0, 1]
# for y in range(k-1):
#     y=int(f[-1])+int(f[-2])
#     f.append(int(y))
# print(f)
# print(sum(f))
# print(f[-1])
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#
# sumfibo = sum(fib(i) for i in range(1, k+1))
# print(sumfibo)
print(fib(35))
=======

k = int(input('Hvilket ledd? '))
f = [0, 1]
for y in range(k-1):
    y=int(f[-1])+int(f[-2])
    f.append(int(y))

print(f[-1])
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(40))
>>>>>>> before discard
