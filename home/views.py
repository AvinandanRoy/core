from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {'familyName': 'Roy Family', 'name' :'Avinandan Roy', 'age': 22},
        { 'familyName': 'Roy Family', 'name' :'Pranta Roy', 'age': 18},
        { 'familyName': 'Roy Family','name' :'Krishna Roy', 'age': 50},
        { 'familyName': 'Roy Family','name' :'Lipi Roy', 'age': 40},
        { 'familyName': 'Gopal Family','name' :'Rudra Roy', 'age': 13},
    ]
    
    text = "This is Avinandan Roy Django Project, who is very inteligent boy. His father name is Krishna Kanta Roy. His mother name is Lipika Rani Roy.He is from Daffodil International University."
    
    vegetable = ['Potato', 'Cucumber', 'Pumpkin', 'Shosha']
    
    return render(request, "./home/index.html", context= {'peoples' : peoples, 'text' : text, 'vegetable': vegetable, 'page': 'Home'})


def about(request):
    context = {'page' : 'About'}
    return render(request,'./home/about.html',context  )


def contact(request):
    context = {'page' : 'Contact'}
    return render(request,'./home/contact.html', context)

def success_page(request):
    print('Avinandan Roy Print version.')
    return HttpResponse('<h1>Bloddy Fucker</h1>')