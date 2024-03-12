from django.shortcuts import render

# Create your views here.



from app.forms import *


from django.http import HttpResponse

def register(request):

    uf = userform()
    pf = userprofileform()

    if request.method == 'POST' and request.FILES:

        print("post method is activated")

        ufd = userform(request.POST)
        upfd = userprofileform(request.POST,request.FILES)

        if  ufd.is_valid() and upfd.is_valid():

            pw = ufd.cleaned_data['password']

            uo = ufd.save(commit=False)

            uo.set_password(pw)


            uo.save()

            upo  =  upfd.save(commit=False)

            upo.user = uo   


            upo.save()

            return HttpResponse("data saved successfully")

        else:


            return HttpResponse("data is not valid")

    return render(request,'register.html',{'uf':uf,'pf':pf})


