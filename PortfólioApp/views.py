from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

def Home(request):
    return render(request, 'Home-Page.html')

def send_email(request):
    if request.method == "POST":
        nome = request.POST.get('Nome')
        sobrenome = request.POST.get('Sobrenome')
        email = request.POST.get('Email')
        telefone = request.POST.get('Telefone')
        mensagem = request.POST.get('Mensagem')

        subject = 'Formulário de Contato'
        message = f'Nome: {nome}\nSobrenome: {sobrenome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}'
        from_email = 'portfolioryannascimento@gmail.com'
        recipient_list = ['ryandonascimentobezerra@gmail.com']  # Substitua com seu e-mail

        try:
            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse('E-mail enviado com sucesso!')
        except Exception as e:
            return HttpResponse(f'Ocorreu um erro: {str(e)}')

    return render(request, 'contato.html')  # Certifique-se de ter uma página de sucesso ou mensagem adequada



