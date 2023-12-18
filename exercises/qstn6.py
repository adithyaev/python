library_catalog ={
     'book1': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1925,
        'genre': 'Classic Fiction',
    },
    'book2': {
        'title': 'Beloved',
        'author': 'Toni Morrison',
        'year': 1960,
        'genre': 'Fiction',
    },
    'book3': {
        'title': '1984',
        'author': 'George Orwell',
        'year': 1949,
        'genre': 'Dystopian Fiction',
    }

}

library_catalog['book4'] = {'title': 'A Passage to India',
        'author': 'E. M. Forster',
        'year': 1920,
        'genre': 'novel'}
   
print(library_catalog)

library_catalog['book1']['author']='Leo Tolstoy'
print(library_catalog)


