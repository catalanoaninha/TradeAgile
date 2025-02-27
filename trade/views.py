from django.shortcuts import render, redirect
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor
from .forms import ClienteForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User
def home(request):
    return render(request, 'trade/home.html')

def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'trade/cadastro_clientes.html', {'form': form})

def demonstrativo_tabelas(request):
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'trade/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })

def galeria_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})

def realizar_venda(request):
    if request.method == 'POST':
        # Lógica simplificada para processar a venda
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()  # Supondo que há um vendedor padrão
        fornecedor = produto.idforn

        valor_venda = produto.valorprod * int(quantidade)
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('venda_concluida')

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'trade/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })

#View da tela de login
def login_view(request):
    if request.method == "POST": #Método POST (inserir ou alterar dados)
        form = AuthenticationForm(request, data=request.POST) #Autenticação
        if form.is_valid(): #Se o formulário for válido (cumprir os requesitos)
            # Pega o usuário e senha
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #Vê se existe e se está igual os dados inseridos no banco de dados
            if user is not None:
                login(request, user)
                return redirect('home') #E redireciona pra tela de bem-vindo
    else:
        form = AuthenticationForm()
    return render(request, 'trade/login.html', {'form': form}) #Renderização do Django para a página de login


def register_view(request):
        if request.method == "POST": #Método POST (inserir ou alterar dados)
            form = UserRegisterForm(request.POST)
            if form.is_valid(): #Se o formulário for válido (cumprir os requesitos)
                user = form.save() #Salva
                login(request, user)
                return redirect('home') #Redireciona pra tela de bem-vindo
        else:
            form = UserRegisterForm()
        return render(request, 'trade/register.html', {'form': form}) #Renderização do Django


def user_list_view(request):
    users = User.objects.all() #Vai pegar todos os dados dos usuários e colocar na variável "user"
    return render(request, 'trade/user_list.html', {'users': users})  #Renderização do Django

def obrigado(request):
    clientes = Cliente.objects.all()
    return render(request,'trade/obrigado.html', {'clientes': clientes})