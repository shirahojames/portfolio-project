from django.db import models

# Create your models here.
class Blog(models.Model):
#dfsa
      Title = models.CharField(max_length=200)
      pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
      Body = models.TextField()
      image = models.ImageField(upload_to='images/')

      def __str__(self):
          return self.Title
      def summary(self):#creating a method summary which will be used to desplay the first 50 characters only
          return self.Body[:10]

      def pub_date_pretty(self):
         return self.pub_date.strftime('%b %e %Y')
