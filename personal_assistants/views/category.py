from django.shortcuts import render, get_object_or_404
from personal_assistants.forms import CategoryForm
from personal_assistants.models import Category
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView


def category_list(request):
    categs = Category.objects.order_by('name')
    return render(request, 'personal_assistants/category.html', {"categs": categs})

def category_detail(request, pk):
    categ = get_object_or_404(Category, pk=pk)
    return render(request, 'personal_assistants/category_detail.html', {"categ": categ})

def category_new(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            categ = category_form.save()
            return redirect('category_detail', pk=categ.pk)
    else:
        category_form = CategoryForm()
    return render(request, 'personal_assistants/category_new.html', {'category_form': category_form})



def category_edit(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    context = {'form': form}
    return render(request, 'personal_assistants/category_edit.html', context)
