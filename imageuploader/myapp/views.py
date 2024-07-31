from django.shortcuts import render
from .models import Image
from .froms import ImageForm
def home(request):
    #logic to upload the image on database

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    #to display the image in fomtend part
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img':img ,'form': form})
