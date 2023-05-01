from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'application/home.html',context=context)