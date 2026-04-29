def bubble_sort(arr):
    """
    氣泡排序法 (Bubble Sort)

    原理: 比較相鄰元素，若順序錯誤則交換，反覆執行直到排序完成
    時間複雜度: O(n²)
    空間複雜度: O(1)
    穩定性: 穩定
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始陣列:", data)
    print("排序後:", bubble_sort(data))
