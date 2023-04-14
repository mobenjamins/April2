from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def result(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        return render(request, 'result.html', context={'user_stuff': user_input})
    else:
        return render(request, 'result.html')
