# quicksort algorithmus
def quicksort(arr, left, right):
    # prüft, ob linkes subarray kleiner als rechtes ist
    if left < right:
        partPosition = part(arr, left, right)
        quicksort(arr, left, partPosition - 1)
        quicksort(arr, partPosition + 1, right)


# gibt das pivot element nach jedem schritt zurück
def part(arr, left, right):
    i = left    # linker part des zu sortierenden arrays
    j = right-1    # rechter part des zu sortierenden arrays
    pivot = arr[right]    # pivot element

    # solange i und j sich nicht kreuzen
    while i < j:
        # i nach rechts bewegen, bis größeres als pivot gefunden
        while i < right and arr[i] < pivot:
            i += 1
        # j nach rechts bewegen, bis kleineres als pivot gefunden
        while j > left and arr[j] >= pivot:
            j -= 1

        # i und j tauschen, wenn sie sich nicht gekreuzt haben
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # i und rechtes element tauschen, wenn i und j sich nicht gekreuzt haben
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arrayToSort = ["Dattel", "Ananas", "Kirsche", "Banane", "Kiwi"]
print(arrayToSort)
quicksort(arrayToSort, 0, len(arrayToSort) - 1)
print(arrayToSort)
