from django.shortcuts import render, redirect

def index(request, room_name):
    context = {
        'room_name': room_name
    }
    return render(request, 'chat/index.html', context)

def create_room(request):
    if request.method == 'POST':
        return redirect('chat:index', room_name=request.POST['room_name'].replace(' ', '-'))

    return redirect('login_reg:index')