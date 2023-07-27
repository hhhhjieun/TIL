number_of_books = 100

def decrease_book(num):
    global number_of_books
    number_of_books -= num
    print('남은 책의 수 : ', number_of_books)
    
