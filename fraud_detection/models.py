from django.db import models
from usermanagement.models import CustomUser


class LinksToReview(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='apps/%Y/%m/%d/',blank = True)
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return  self.name
    

class UserReviewed(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    review_link = models.ForeignKey(LinksToReview,on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=4,decimal_places=3,blank=True,default=1)
    review = models.TextField()
    sentiment_analysis = models.CharField(max_length=10,default="")
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "Review"