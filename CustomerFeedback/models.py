from django.db import models

class CustomerFeedback(models.Model):

    comment_titles = [
        ("Compliment","Compliment"),
        ("Complaint","Complaint")        
    ]

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_No = models.CharField(max_length=10)
    comment_dropdown = models.CharField(choices=comment_titles, max_length=30, default='Compliment' )
    comments = models.TextField(max_length=500)


    