from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    author = models.TextField()
    location = models.TextField()
    postion = models.TextField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '''
        Title: {}
        Job Desciption: {}
        Postion: {}
        Location{}
        Author: {}
        Date: {}
        
        '''.format(self.title, self.body, self.postion, self.location,
                   self.author, self.date)

    @staticmethod
    def submit_post(title, author, location, postion, body):
        BlogPost(
            title=title,
            author=author,
            location=location,
            postion=postion,
            body=body).save()


class BlogComment(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT)

    def __str__(self):
        return '''
        Title: {}
        Author: {}
        Body: {}
        Rating: {}
        Date: {}
        Comment for Blog #: {}
        '''.format(self.title, self.author, self.body, self.rating, self.date,
                   self.blog_post)

    @staticmethod
    def submit_comment(title, body, author, rating, blog_post_id):
        BlogComment(
            title=title,
            body=body,
            author=author,
            rating=rating,
            blog_post_id=blog_post_id).save()