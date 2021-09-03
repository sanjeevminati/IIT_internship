from django.shortcuts import render, redirect

from .models import Image
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# def upload(request):
# 	if request.method == "POST":
# 		form = ImageForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			images = form.instance
# 			return render(request=request, template_name="main/upload.html", context={'form':form , 'images':images})
# 	else:
# 		form = ImageForm()
# 	return render(request=request, template_name="main/upload.html", context={'form':form })



#
# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'main/upload.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'main/upload.html', {'form': form})
def upload(request):
    return render(request, 'main/upload.html')


def upload_save(request):
    images = request.FILES.getlist("file[]")
    for img in images:
        fs = FileSystemStorage()
        file_path = fs.save(img.name, img)
        images = Image(image=file_path)
        images.save()

    return redirect('caption')



def caption(request):
    return render(request,'caption.html')
