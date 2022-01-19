from django.shortcuts import render,redirect,Http404, HttpResponse
from .forms import ItemForm
from .models import Item
import csv


# Create your views here.

def create(request): 
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:   
        form = ItemForm()
        return render(request,'create.html',{'form':form})

def read(request):
    items = Item.objects.all()
    return render(request, 'index.html',{'items':items})

def update(request,id):
    item = Item.objects.get(itemcode=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance =item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemForm(instance = item)
        return render(request,'update.html',{'form':form})

def delete(request,id):
        item = Item.objects.get(itemcode=id)
        item.delete()
        return redirect('/empty')

def export_to_csv(request):
    items = Item.objects.all()
    
    if items.exists():
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
    
        writer = csv.writer(response)
        column_names = ['Name', 'Category', 'Quantity','Description', 'Itemcode']
        writer.writerow(column_names)
        for item in items:
            writer.writerow([item.name, item.category, item.quantity, item.description, item.itemcode])
        return response

    else:
       return render(request, 'empty.html',{'items':items})


