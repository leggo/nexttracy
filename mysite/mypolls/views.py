from django.shortcuts import render, render_to_response

def home(request):
	number = 3
	object_name = "Objecto Name"
	
	return render_to_response('index.html', {
		'number': number,
		'object_name': object_name,
	})
#    return render_to_response('index.html')