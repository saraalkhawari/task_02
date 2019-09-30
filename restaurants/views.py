from django.shortcuts import render

# Create your views here.

def page1 (request):

	context = {

		'msg': 'Hello World !'
	}

	return render(request,'page1.html',context)