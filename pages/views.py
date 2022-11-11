from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("This is a great site for e-commerce resources. Coming soon!")
