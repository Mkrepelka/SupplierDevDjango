from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html',{})

def about(request):
	return render(request, 'about.html',{})	

def service(request):
	return render(request, 'service.html',{})	

def blog(request):
	return render(request, 'blog.html',{})	

def blog_details(request):
	return render(request, 'blog-details.html',{})

def pricing(request):
	return render(request, 'pricing.html',{})		

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send email
		send_mail(
			'Message from Supplier Development Website', # subject used to say message_name
			message, # message
			message_email, # from email;
			['TSupplierDev@gmail.com'], # to email
			fail_silently=False,
			)


		return render(request, 'contact.html',{'message_name': message_name})

	else:
		# Return the page
		return render(request, 'contact.html',{})

		# Return the about page
		return render(request, 'about.html',{})

		# Return the Service page
		return render(request, 'service.html',{})

		# Return the Blog page
		return render(request, 'blog.html',{})

		# Return the Blog details page
		return render(request, 'blog-details.html',{})

		# Return the Pricing page
		return render(request, 'pricing.html',{})