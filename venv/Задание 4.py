def insertion_sort(bookshelf):
    for i in range(1, len(bookshelf)):
        current_book = bookshelf[i]
        j = i - 1
        while j >= 0 and current_book < bookshelf[j]:
            bookshelf[j + 1] = bookshelf[j]
            j -= 1
        bookshelf[j + 1] = current_book
bookshelf1 = ["Smith", "Johnson", "Brown", "Doe", "Adams"]
bookshelf2 = ["Wilson", "Lee", "Davis", "Anderson", "White"]
bookshelf3 = ["Wilson", "Lee", "Davis", "Anderson", "White"]
insertion_sort(bookshelf1)
insertion_sort(bookshelf2)
insertion_sort(bookshelf3)
print("Полка 1 после сортировки:", bookshelf1)
print("Полка 2 после сортировки:", bookshelf2)
print("Полка 3 после сортировки:", bookshelf3)