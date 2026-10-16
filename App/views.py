from django.shortcuts import redirect, render
from App.models import*

# Create your views here.



def project(request):
    hello=Data.objects.all()
    context={'data':hello}
    return render(request,"project1.html",context)  

def header2(request):
    queryset=Data.objects.all()
    context={'form':queryset}
    return render(request,"header2.html",context) 


def project2(request):
    hello=Data.objects.all()
    context={'data':hello}
    return render(request,"project2.html",context)


def dashboard(request):
    hello=Data.objects.all()
    context={'data':hello}
    return render(request,"dashboard.html",context)






def detail(request):
    if request.method == "POST":
        name = request.POST.get("name")
        prize = request.POST.get("prize")
        image = request.FILES.get("image")

        Data.objects.create(
            name=name,
            prize=prize,
            image=image,
        )
        return redirect('dashboard')
    hello=Data.objects.all()
    context={'data':hello}
    return render(request, "detail.html",context)


def delete_data(request, id):
    item =Data.objects.get( id=id)
    item.delete()
    return redirect('dashboard')


def update2(request,id):
    item=Data.objects.get(id=id)
    if request.method == "POST":
        name=request.POST.get("name")
        prize=request.POST.get("prize")
        
        image = request.FILES.get("image")
        item.name = name
        item.prize = prize
        if image:
            item.image=image
            item.save()

        return redirect('dashboard')
   
    context={'detail':item}
    return render(request,"update2.html",context)

    




  

   
    

