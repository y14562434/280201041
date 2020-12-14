books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for book in books:
  charact = len(book)
  unique_charact = len(set(book))
  value = (charact, unique_charact)
  book_dict[book] = value
  
