from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    author = models.TextField()
    location = models.TextField()
    postion = models.TextField()
    benefits = models.TextField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '''
        Title: {}
        Job Desciption: {}
        Postion: {}
        Location: {}
        Benefits: {}
        Author: {}
        Date: {}
        
        '''.format(self.title, self.body, self.postion, self.location,
                   self.benefits, self.author, self.date)

    @staticmethod
    def submit_post(title, author, location, postion, benefits, body):
        BlogPost(
            title=title,
            author=author,
            location=location,
            postion=postion,
            benefits=benefits,
            body=body).save()
    


class BlogComment(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return '''
        Title: {}
        Author: {}
        Body: {}
        Date: {}
        Comment for Blog #: {}
        '''.format(self.title, self.author, self.body, self.date,
                   self.blog_post)

    @staticmethod
    def submit_comment(title, body, author, blog_post_id):
        BlogComment(
            title=title, body=body, author=author,
            blog_post_id=blog_post_id).save()