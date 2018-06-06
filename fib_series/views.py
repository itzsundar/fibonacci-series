from django.shortcuts import render
from .caches import cache
from django.views.decorators.csrf import csrf_protect
from time import time
from fib_series.models import FibonacciSeries

@csrf_protect
def index(request):
	if request.method == 'POST':
		num = int(request.POST['num'])
		value = 0
		computaion_time = 0.0

		if num <= 0:
		    raise ValueError("Must be enter the Positive Number.")
		else:
			t0 = time() 
			value = fibb(num)
			computation_time = round(time()-t0, 4) 

			fibina = FibonacciSeries.objects.filter(num=num).first()
			if not fibina:
				FibonacciSeries.objects.create(num=num, value=value, computation_time=computation_time)

        	context = {'number':num, 'value':value, 'computation_time':computation_time}
		return render(request,'index.html', context)
	else:
		context = {'number': '___!', 'value':'Must be Enter a Valid Integer value!', 'computation_time':'___!'} 
		return render(request,'index.html', context)

@cache('default')
def fibb(num):
    if num in (0,1):
        return num
    else:
        return fibb(num -1) + fibb(num - 2)