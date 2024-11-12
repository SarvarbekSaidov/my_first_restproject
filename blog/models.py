from django.db import models

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogAuthor(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='author_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)

    def __str__(self):
        return self.title

class PostComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.username} on {self.post}"