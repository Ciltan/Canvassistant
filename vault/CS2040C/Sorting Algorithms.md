---
tags: [CS2040C, sorting, algorithms, comparison-sort]
---

# Sorting Algorithms

## Overview

Sorting is one of the most fundamental operations in computer science. CS2040C covers comparison-based sorts (Bubble, Selection, Insertion, Merge, Quick) and non-comparison sorts (Counting, Radix). The theoretical lower bound for comparison-based sorting is $\Omega(n \log n)$.

## Comparison-Based Sorts

### Bubble Sort

Repeatedly swaps adjacent elements if they are in the wrong order.

```cpp
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // Optimization: early exit
    }
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n)$ (already sorted, with early exit) | $O(1)$ |
| Average | $O(n^2)$ | $O(1)$ |
| Worst | $O(n^2)$ | $O(1)$ |

> [!note] Properties
> - **Stable**: Yes (equal elements maintain relative order)
> - **In-place**: Yes
> - **Adaptive**: Yes (with early termination optimization)

### Selection Sort

Finds the minimum element and places it at the beginning, then repeats for the remaining subarray.

```cpp
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }
        swap(arr[i], arr[minIdx]);
    }
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n^2)$ | $O(1)$ |
| Average | $O(n^2)$ | $O(1)$ |
| Worst | $O(n^2)$ | $O(1)$ |

> [!note] Properties
> - **Stable**: No (swapping can change relative order of equal elements)
> - **In-place**: Yes
> - **Minimum swaps**: Only $O(n)$ swaps (useful when writes are expensive)

### Insertion Sort

Builds the sorted array one element at a time by inserting each element into its correct position.

```cpp
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n)$ (already sorted) | $O(1)$ |
| Average | $O(n^2)$ | $O(1)$ |
| Worst | $O(n^2)$ (reverse sorted) | $O(1)$ |

> [!important] Why Insertion Sort Matters
> - Best for small arrays (used as base case in hybrid sorts like Timsort/Introsort)
> - Best for nearly sorted data
> - Online algorithm: can sort data as it arrives
> - Stable and in-place

### Merge Sort

Divide-and-conquer: split array in half, recursively sort each half, then merge.

```cpp
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1, n2 = right - mid;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n \log n)$ | $O(n)$ |
| Average | $O(n \log n)$ | $O(n)$ |
| Worst | $O(n \log n)$ | $O(n)$ |

> [!note] Properties
> - **Stable**: Yes
> - **In-place**: No (requires $O(n)$ auxiliary space)
> - **Guaranteed** $O(n \log n)$: Unlike Quick Sort, no worst case degradation
> - Recurrence: $T(n) = 2T(n/2) + O(n)$

### Quick Sort

Divide-and-conquer: choose a pivot, partition so elements less than pivot go left and greater go right, then recurse.

```cpp
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Last element as pivot
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n \log n)$ | $O(\log n)$ stack |
| Average | $O(n \log n)$ | $O(\log n)$ stack |
| Worst | $O(n^2)$ (sorted input, bad pivot) | $O(n)$ stack |

> [!warning] Avoiding Worst Case
> - **Randomized pivot**: Pick a random element as pivot
> - **Median-of-three**: Choose median of first, middle, last elements
> - **3-way partition**: Handle many duplicate keys efficiently (Dutch National Flag)

> [!note] Properties
> - **Stable**: No (partitioning can rearrange equal elements)
> - **In-place**: Yes (only $O(\log n)$ stack space)
> - In practice, often fastest due to cache locality and low constant factors

## Non-Comparison Sorts

> [!important] Lower Bound
> Any comparison-based sorting algorithm requires $\Omega(n \log n)$ comparisons in the worst case. Non-comparison sorts bypass this by exploiting the structure of the data.

### Counting Sort

Counts the occurrences of each value. Works when the range of values $k$ is not too large.

```cpp
void countingSort(int arr[], int n, int maxVal) {
    vector<int> count(maxVal + 1, 0);
    vector<int> output(n);

    for (int i = 0; i < n; i++) count[arr[i]]++;
    for (int i = 1; i <= maxVal; i++) count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    for (int i = 0; i < n; i++) arr[i] = output[i];
}
```

| Complexity | Value |
|-----------|-------|
| Time | $O(n + k)$ where $k$ is the range of values |
| Space | $O(n + k)$ |
| Stable | Yes |

### Radix Sort

Sorts digit by digit (LSD or MSD) using a stable sub-sort (typically counting sort).

```cpp
void radixSort(int arr[], int n) {
    int maxVal = *max_element(arr, arr + n);
    for (int exp = 1; maxVal / exp > 0; exp *= 10) {
        countingSortByDigit(arr, n, exp); // Stable sort on digit
    }
}
```

| Complexity | Value |
|-----------|-------|
| Time | $O(d \cdot (n + k))$ where $d$ = digits, $k$ = base |
| Space | $O(n + k)$ |
| Stable | Yes (must use stable sub-sort) |

## Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| Selection Sort | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| Insertion Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | Yes |
| Heap Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Yes |
| Counting Sort | $O(n+k)$ | $O(n+k)$ | $O(n+k)$ | $O(n+k)$ | Yes | No |
| Radix Sort | $O(dn)$ | $O(dn)$ | $O(dn)$ | $O(n+k)$ | Yes | No |

## Related Notes

- [[Complexity Analysis]] - Big-O fundamentals used throughout
- [[Heaps and Priority Queues]] - Heap Sort details
- [[Arrays and Linked Lists]] - underlying data structures for sorting
