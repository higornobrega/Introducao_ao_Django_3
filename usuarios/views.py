from django.shortcuts import redirect, render
from django.contrib.auth.models import User
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        print(nome, email, senha, senha2)
        if not nome.strip():
            print("O componente não pode ficar em Branco")
            return redirect('cadastro')
        if not email.strip():
            print("O campo nome não pode ficar em Branco")
            return redirect('cadastro')   
        if senha != senha2:
            print("Senha diferente da confimação")
            return redirect('cadastro')     
        if User.objects.filter(email=email).exists():
            print("Usuário já cadastrado")
            return redirect('cadastro')   

        user = User.objects.create_user(username=nome, email=email, password=senha) 
        user.save()
        print('Usuario cadastrado') 
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashbord(request):
    pass    
    