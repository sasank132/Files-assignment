import Json_file_loading

def save_books_by_category(data, category, textfile):
    with open(textfile, 'w') as file:
        file.write(f"Books in the {category} category:\n")
        for record in data:
            adoptions = record.get('adoptions', [])
            for adoption in adoptions:
                book = adoption.get('book', {})
                if book.get('category') == category:
                    file.write(f"{book['title']}\n")

category=input('Enter category: ').title()
textfile=input('Enter textfile name you would like to assign: ')
save_books_by_category(Json_file_loading.data, category, textfile)