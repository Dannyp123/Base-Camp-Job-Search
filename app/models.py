from django.db import models


# Create your models here.
class BlogPost(models.Model):
    image = models.URLField()
    title = models.TextField()
    author = models.TextField()
    postion = models.TextField()
    benefits = models.TextField()
    streetNum = models.IntegerField()
    streetName = models.TextField()
    townName = models.TextField()
    state = models.TextField()
    zipCode = models.IntegerField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '''
        Image: {}
        Title: {}
        Job Desciption: {}
        Postion: {}
        Benefits: {}
        Street Name: {}
        Street Num: {}
        Town Name: {}
        State: {} 
        Zip Code: {}
        Author: {}
        Date: {}
        
        '''.format(self.image, self.title, self.body, self.postion,
                   self.benefits, self.streetName, self.streetNum,
                   self.townName, self.state, self.zipCode, self.author,
                   self.date)

    @staticmethod
    def submit_post(image, title, author, postion, benefits, streetName,
                    streetNum, townName, state, zipCode, body):
        BlogPost(
            image=image,
            title=title,
            author=author,
            postion=postion,
            benefits=benefits,
            streetName=streetName,
            streetNum=streetNum,
            townName=townName,
            state=state,
            zipCode=zipCode,
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