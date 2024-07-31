from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

with app.app_context():
    db = SQLAlchemy(Base)
    
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    title: Mapped[str] = mapped_column(String(250), nullable= False, unique= True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

# Now we can use the db.session to add, delete or select the objects
# This is called the CRUD (Create, Read, Update, Delete) operation
# First, for the create operation:
with app.app_context():
    book = Books(
        id = 1,
        title = "Harry Potter",
        author = "JK Rowling",
        rating = 8.5
    )
    db.session.add(book)
    db.session.commit()
# I had to add the context here because I'm running this outside of a function that
# belongs to the app context
# We can also skip the primary key and it will be auto generated

# Now for the Read operation:
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    # I was getting an error which took me long to realize that we needed to pass in
    # the table class itself and not the name string
    all_books = result.scalars()
    # This is a ScalarResult object and cannot be directly used
    # If we want to get a specific record, we can use:
    specific_book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    # We use scalar for single record, and scalars for multiple
    # and this scalar is an object <Tablename id>

# For update operation:
# By query:
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book.title = "Harry Potta"
    db.session.commit()
# By primary key:
with app.app_context():
    book_id = 1
    # We can use similar structure as above to select the book, or we can use:
    book = db.get_or_404(Books, book_id)
    book.title = "Harry Potter"
    db.session.commit()

# Finally, for the delete operation:
with app.app_context():
    book_to_dlt = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    db.session.delete(book_to_dlt)
    db.session.commit()