from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from crud.models import Funcionario
from crud.forms import FuncionarioForm


def index(request):
    funcionarios = Funcionario.objects.all()
    paginator = Paginator(funcionarios, 2)

    page = request.GET.get('p')

    funcionarios = paginator.get_page(page)

    context = {'funcionarios': funcionarios}

    return render(request, 'portal/index.html', context)


def adicionar_funcionario(request):
    form = FuncionarioForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'portal/adicionar_funcionario.html', context)


def editar_funcionario(request, funcionario_pk):
    funcionario = Funcionario.objects.get(pk=funcionario_pk)

    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'funcionario_pk': funcionario_pk,
    }

    return render(request, 'portal/editar_funcionario.html', context)


def deletar_funcionario(request, funcionario_pk):
    funcionario = Funcionario.objects.get(pk=funcionario_pk)
    funcionario.delete()
    messages.info(request, 'Funcionário excluído com sucesso!')
    return redirect('index')
