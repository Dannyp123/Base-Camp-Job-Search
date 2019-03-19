from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class BlogPost(models.Model):
    image = models.URLField()
    title = models.TextField()
    author = models.TextField()
    companyName = models.TextField()
    salary = models.IntegerField()
    postion = models.TextField()
    benefits = models.TextField()
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    phoneNum = models.CharField(validators=[phone_regex], max_length=10)
    streetNum = models.IntegerField()
    streetName = models.TextField()
    townName = models.TextField()
    state = models.TextField(max_length=2)
    zipCode = models.IntegerField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '''
        Image: {}
        Title: {}
        Company Name: {}
        Salary: {}
        Job Desciption: {}
        Postion: {}
        Benefits: {}
        Email: {}
        Phone Number: {}
        Street Name: {}
        Street Num: {}
        Town Name: {}
        State: {} 
        Zip Code: {}
        Author: {}
        Date: {}
        
        '''.format(self.image, self.title, self.companyName, self.salary,
                   self.body, self.postion, self.benefits, self.email,
                   self.phoneNum, self.streetName, self.streetNum,
                   self.townName, self.state, self.zipCode, self.author,
                   self.date)

    @staticmethod
    def submit_post(image, title, companyName, salary, author, postion,
                    benefits, email, phoneNum, streetName, streetNum, townName,
                    state, zipCode, body):
        BlogPost(
            image=image,
            title=title,
            companyName=companyName,
            salary=salary,
            author=author,
            postion=postion,
            benefits=benefits,
            email=email,
            phoneNum=phoneNum,
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