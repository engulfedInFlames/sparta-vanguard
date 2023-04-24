phone_book = {
    "John": "123-4567",
    "Jane": "234-5678",
    "Max": "345-6789",
}


def search():
    gyeong_su = yield
    while True:
        if gyeong_su in phone_book:
            phone_number = phone_book.get(gyeong_su)
        else:
            phone_number = "Cannot find the name in the phone book."
        gyeong_su = yield phone_number


search_coroutine = search()
next(search_coroutine)

result = search_coroutine.send("John")
print(result)

result = search_coroutine.send("Jane")
print(result)

result = search_coroutine.send("Sarah")
print(result)
