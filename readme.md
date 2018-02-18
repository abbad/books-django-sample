# Books api.

Django Books API sample.

To Run the code:

``` Install postgres and create a new user and database schema```
``` 1. pip install -r requirements.txt ```
``` 2. python manage.py migrate ```
``` 3. python manage.py runserver and go to http://127.0.0.1:8000/api/v1/books/ ```
``` 4. For Tests run python manage test ```

Or you can run it through ```run_server.sh```

I have written a books app that has a model with the following fields:

- book id: A primary field increments automatically.
- book title: Char field that is required.
- book author: Foreign key to user tables. It would be better to create a new author table rather than using user.
- book isbn: I Found an isbn field package. I used it to run validation and made ISBN unique.
- book price: Decimal Field representing the price.
- book short description: Text field representing short description of the book.
