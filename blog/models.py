from django.db import models


class Blog(models.Model):	
	title = models.CharField(default='正文标题', max_length=50)
	date = models.DateField()
	image = models.ImageField(default='default.png',upload_to='image/')
	text = models.CharField(default='正文', max_length=50)
    
    # def __str__(self):
    # 	return self.title
    
    # def blog_page(self):
    #     return self.text[:88] + '...'
