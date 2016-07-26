from django.db import models

# Create your models here.

Filters=( ('BLUR','BLUR'),('CONTOUR','CONTOUR'),('DETAIL','DETAIL'),('EDGE_ENHANCE','EDGE_ENHANCE'))

# Create your models here.
class Images(models.Model):
	Image=models.ImageField(upload_to='images/')
	Filter=models.CharField(max_length=100,choices=Filters,default='BLUR')
	 
	def __unicode__(self):
		return self.Filters

