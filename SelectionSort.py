def SelectionSort(arr):
    for i in range(0,len(arr)):
        MinValue=i;
        for j in range(i+1,len(arr)):
            if (arr[j] < arr[MinValue]):
                MinValue = j;
        if (i != MinValue):
            arr[MinValue], arr[i]=arr[i],arr[MinValue];
def main():
    global arr;
    arr = [1,7,9,2,3,0,16,654,98];
    SelectionSort(arr);
    print("Sorted arra is:",end=" ")
    for i in range(len(arr)):
        print(arr[i], " ", end=" ");
if __name__=="__main__":
    main()
