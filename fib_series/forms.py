from django import forms

from .models import FibonacciSeries

class FibonacciSeriesForm(forms.ModelForm):
	class Meta:
		model = FibonacciSeries
		fields = [
			"num"
		]