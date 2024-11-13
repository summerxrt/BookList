from django.db import models

# Create your Book model here.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title attribute with CharField, max_length = 255
    author = models.CharField(max_length=255)  # Author attribute with CharField, max_length = 255
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price attribute with DecimalField, max_digits = 5, decimal_places = 2

    # Create Meta class inside the Book model
    class Meta:
        indexes = [
            models.Index(fields=['price']),  # Adding an index on the 'price' field
        ]

    def __str__(self):
        # Optional: This method helps display the Book objects in a more readable format
        return f"{self.title} by {self.author}"

