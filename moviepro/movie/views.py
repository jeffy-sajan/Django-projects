from movie.forms import movieform
from django.shortcuts import render
from movie.models import Movie

def home(request):
    b = Movie.objects.all()
    return render(request, 'home.html', {'movie': b})

def addmovie(request):
    form = movieform()
    if (request.method == 'POST'):
        form = movieform(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request, 'add.html', {'form': form})



def viewmoviebyid(request,p):
    b = Movie.objects.get(id=p)
    return render(request, 'view1.html', {'movie': b})

def deletemoviebyid(request,p):
    b = Movie.objects.get(id=p)
    b.delete()
    return home(request)

def editmoviebyid(request,p):
    b = Movie.objects.get(id=p)
    form = movieform(instance=b)
    if (request.method == 'POST'):
        form = movieform(request.POST, request.FILES, instance=b)
        if (form.is_valid()):
            form.save()
            return home(request)
    return render(request, 'add.html', {'form': form})











