def find_min_max(arr):
    if not arr:
        raise ValueError("Array is empty. Cannot determine min and max.")

    def recursive_min_max(low, high):
        if low == high:
            return arr[low], arr[low]
        elif high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]

        mid = (low + high) // 2
        left_min, left_max = recursive_min_max(low, mid)
        right_min, right_max = recursive_min_max(mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    return recursive_min_max(0, len(arr) - 1)


def find_kth_min(array, k):
    if not array:
        raise ValueError("Array is empty. Cannot determine k-th minimum.")
    if k < 1 or k > len(array):
        raise IndexError("k is out of range.")

    def partition(arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(arr, left, right, k):
        if left == right:
            return arr[left]
        pivot_index = left + (right - left) // 2
        pivot_index = partition(arr, left, right, pivot_index)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(arr, left, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, right, k)

    return select(array, 0, len(array) - 1, k - 1)
