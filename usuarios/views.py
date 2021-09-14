from django.shortcuts import redirect, render

def cadastro(request):
    if request.method == 'POST':
        print('PAssou')
        redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashbord(request):
    pass    
    