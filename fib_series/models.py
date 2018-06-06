from django.db import models

class FibonacciSeries(models.Model):
	num = models.IntegerField()
	value = models.TextField()
	computation_time = models.DecimalField(max_digits=20, decimal_places=4)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return str(self.num)
	
