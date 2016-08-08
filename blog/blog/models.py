from django.db import models

short_text = 300

class Article(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    # user = models.ForeignKey(User)

    def  __str__(self):
        return self.tittle

    def short(self):
        if len(self.text) > short_text:
            return self.text[:short_text]
        else:
            return self.text