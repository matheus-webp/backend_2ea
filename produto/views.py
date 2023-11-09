from django.shortcuts import redirect, render
from .forms import ProdutoForm

def create_product(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:127.0.0.1:8000/')
    else: 
        form = ProdutoForm()
    return render(request, 'index.html', {'form': form})

