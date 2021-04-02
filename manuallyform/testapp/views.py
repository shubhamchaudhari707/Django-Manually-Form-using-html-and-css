from django.shortcuts import render
from testapp.models import User

# Create your views here.
def showdata(request):
    if request.method == 'POST':
        # print('ye post method se aa ra hai ')
        # print(request.POST.get('email'))
        # print(request.POST.get('passward'))
        
        nm = request.POST.get('email')
        pw = request.POST.get('passward')
        reg = User(email=nm, passward=pw)
        reg.save()

    else:
        return render(request, 'testapp/index.html')
    return render(request, 'testapp/index.html')

