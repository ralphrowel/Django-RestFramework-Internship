from django.db import models

class Questions(models.Model):
    Questions_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date:')

    def __str__(self):
        return self.Questions_text

class Choices(models.Model):
    Questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 
    def __str__(self):
        return self.choice_text