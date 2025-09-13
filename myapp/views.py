from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Video


# User

def user_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        avatar = request.FILES.get('avatar')
        User.objects.create(first_name=first_name, last_name=last_name, email=email, avatar=avatar)
        return redirect('user_list')
    return render(request, 'user_create.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_detail.html', {'user': user})


def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        if request.FILES.get('avatar'):
            user.avatar = request.FILES.get('avatar')
        user.save()
        return redirect('user_list')
    return render(request, 'user_create.html', {'user': user})


def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user_list')


# Video

def video_create(request):
    users = User.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        user_id = request.POST.get('user_id')
        Video.objects.create(title=title, description=description, file=file, user=User.objects.get(id=user_id))
        return redirect('video_list')
    return render(request, 'video_create.html', {'users': users})



def video_list(request):
    
    user_id = request.GET.get('user_id')
    exclude_user_id = request.GET.get('exclude_user_id')

    users = User.objects.all()

    videos = Video.objects.all()

    if user_id:
        videos = videos.filter(user__id=user_id)
    if exclude_user_id:
        videos = videos.exclude(user__id=exclude_user_id)

    return render(request, 'video_list.html', {'videos': videos, 'users': users, 'user_id': user_id})



def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    return render(request, 'video_detail.html', {'video': video})


def video_update(request, id):
    video = get_object_or_404(Video, id=id)
    users = User.objects.all()
    if request.method == 'POST':
        video.title = request.POST.get('title')
        video.description = request.POST.get('description')
        if request.FILES.get('file'):
            video.file = request.FILES.get('file')
        video.user = get_object_or_404(User, id=request.POST.get('user_id'))
        video.save()
        return redirect('video_list')
    return render(request, 'video_create.html', {'video': video, 'users': users})


def video_delete(request, id):
    video = get_object_or_404(Video, id=id)
    video.delete()
    return redirect('video_list')
