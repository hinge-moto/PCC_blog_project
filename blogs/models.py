from django.db import models

class BlogPost(models.Model):
    """A blog post created by a user."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the blog post title?""" # Maybe change this.........
        return self.title