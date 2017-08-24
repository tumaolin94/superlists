from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item



# Create your views here.
def home_page(request):
    # return render(request, 'home.html')
    # if request.method =='POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

    # else:
    #     new_item_text=''
    # item = Item()
    # item.text = request.POST.get('item_text','')
    # item.save()
    # return render(request,'home.html',{
    #     'new_item_text':new_item_text
    # })

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})