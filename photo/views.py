from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    photos = Photo.objects.all() # Photo 모델의 데이터를 모두 가져왔다. 
    return render(request, 'photo/photo_list.html', {'photos': photos})
    # 데이터베이스에서 데이터를 꺼내 템플릿으로 전달하기도 하지만, 템플릿을 보이게 하는 역할을 한다.
     
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo':photo})

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html', {'form':form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form':form})

