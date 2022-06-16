import math
import builtins
range = builtins.range

list1 = [0,1,2,3,4,5,6,7,8,9,10]
target = 9
list2 = list(range(1, 100))



#Gehe Schritt für Schritt durch die Liste durch und überprüfe ob Item == target

def linear_search(list_object, target):
    counter = 0
    for i in range(len(list_object)):
        counter += 1
        print(counter)
        if list_object[i] == target:
            print("Tagret: ", list_object[i])
            break
    return None

    #print("Needed steps: ", counter)


#linear_search(list2, 50)
#print(list2)
#Starte bei Halbierung der Liste. Wenn target derselbe Wert ist wie die Mitte der Liste dann gib mitte zurück
#Wenn nicht, überprüfe ob item_list in der Mitte kleiner als das target ist. Wenn ja dann setze den anfangspunkt auf +1 ab der Hälfte
#Bei end == 100 wäre das 51. Alles was davor in der Liste ist, wird nicht betrachtet
#Wenn item_list nicht kleiner als target ist, dann ist es größer. in dem fall setze die end variable auf middle -1.
#D.h. alles was nach der Mitte kommt, wird nicht betrachtet. Bei end == 100 wäre das 49.
#Wiederhole bis das Objekt gefunden ist

def binary_search(item_list, target):
    first = 0
    end = len(item_list) -1
    counter = 0
    while first <= end:

        counter = counter + 1

        middle = (end + first) //2
        if item_list[middle] == target:
            print("Needed steps: ", counter)
            return middle
            

        elif item_list[middle] < target:
            first = middle + 1
        else:
            end = middle -1
    
    return None


print(binary_search(list2, 22))

def verify(index):
    if index is not None:
        print('Index found at position: ', index)
    else:
        print('Target not found in List')


result1 = binary_search(list2, 22)
result2 = binary_search(list2, 101)
verify(result1)
verify(result2)

def binary_search_recursion(item_list, target):
    counter = 0

    if len(item_list) == 0:
        return False
    else:
        counter = counter + 1
        midpoint = (len(item_list))//2
        if item_list[midpoint] == target:
            print("Needed steps: ", counter)
            return True
        else:
            if item_list[midpoint] < target:
                return binary_search_recursion(item_list[midpoint+1:], target)
            else:
                return binary_search_recursion(item_list[:midpoint], target)

result3 = binary_search_recursion(list2, 22)
print(result3)


