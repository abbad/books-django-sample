# Books api.

Django with DRF Books API sample.


To run application: 

1. Install Docker 
2. run `docker-comopose up`

To populate database with fake users run:
1. `docker-compose exec web bash -c "./manage.py create_fake_users"`

I have written a books app that has a model with the following fields:

- book id: A primary field increments automatically.
- book title: Char field that is required.
- book author: Foreign key to user tables. It would be better to create a new author table rather than using user .
- book isbn: ISBN ISO standard unique field.
- book price: Decimal Field representing the price.
- book short description: Text field representing short description of the book
