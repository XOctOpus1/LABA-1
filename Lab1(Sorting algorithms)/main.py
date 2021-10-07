# Задача №2 Денис Гордійчук група К28
import algorithms as ag

x = []         #7

# 12
# 56
# 85
# -120
# 0
# 987
# -56

n = int(input("Enter number of elements : "))
print("input elements")
for i in range(0, n):
     ele = int(input())

     x.append(ele)

y = int(input(" Please enter what type of sorting algorithm U want to use: '\n''\t'1.Insertion '\n''\t'2.Bucket '\n''\t'3.Merge '\n''\t'4.Quick '\n''\t'5.Bubble '\n''\t'6.Selection '\n''\t'7.Built-in Python function '\n''\t'0.Exit"'\n'))

if y == 1:
     print("Insertion :")
     print(ag.insertionSort(x))
if y == 2:
     print("Bucket :")
     ag.bucketSort(x)
     print(ag.bucketSort(x))
if y == 3:
     print("Merge :")
     ag.mergeSort(x)
     print(x)
if y == 4:
     print("Quick :")
     ag.quickSort(x, 0, n - 1)
     print(x)
if y == 5:
     print("Bubble :")
     print(ag.bubble_sort(x))
if y == 6:
     print("Selection :")
     ag.selectionSort(x)
     print(x)
if y == 7:
     print("Built-in Python function :")
     x.sort()
     print(x)
if y == 0:
     exit()

