from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# Models have a built-in method called save() that writes the data contained within to the database
# You can instantiate your model and give it some data at the same time, then call save() on the instance
# to write the data to the database.

# When you want to list all the items in a table, you can use some static methods on your class that 
# extends Model.  The objects.all() method returns a list of your objects.  So in our case, we get a 
# list of Book if we call Book.objects.all().  Then you can access the individual items in the list 
# the usual way. e.g. Book.objects.all()[0] is an instance of book and you can access its attributes
# with Book.objects.all()[0].title for example.

# Note: to save your changes to the database, you can make a variable point to a single
# element from the list exposed by Book.objects.all().  Then call the save() method
# on the object.  If the entry is new, Django will add a row, else it will update an
# existing record.

# Create vs Save.  To add entries to the database there are 2 ways
# 1) Create an instance of the model class and then call .save()
#    - This is 2 steps
# 2) Call Book.objects.create(...)
#    - This writes directly to the database 

# Book.objects.get() is another way to get a single element from the DB
# the "id" field is automatically added to all the objects, autoincrement
# You can use id to look up elements Book.objects.get(id=1)
# Or you can use Book.objects.get(title="Harry Potter")
# But get() is for returning only a single entity
# filter() can return multiple results.  e.g. filter(is_bestselling=True)
# If you want to use >= or > etc with filter, then use the __lte or __lt modifiers
# e.g. filter(rating_lt==5)  will find all books where rating less than 5
# Another modifier is __contains.  This does a LIKE in SQL.

# If you want to search your table/list using conditons joined by OR, then 
# you need the Q class from django.db.models. 
# By wrapping your filter() conditions with Q() you can then OR them together 
# with the usual | operator.  If you want AND and OR in a filter, then use 
# a , for the AND and | for the OR.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating}/5)"
    