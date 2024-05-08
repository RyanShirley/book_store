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

# adding a comment

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
    