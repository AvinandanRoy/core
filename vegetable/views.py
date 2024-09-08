from django.shortcuts import render, redirect
from .models import * 

# Create your views here.

def receipes(request):
    
    if request.method == 'POST':
        data = request.POST
        recipe_name= data.get('recipe_name')
        recipe_des = data.get('recipe_des') 
        recipe_img = request.FILES.get('recipe_img')
        print(recipe_name )
        print(recipe_des )
        print(recipe_img )
    
        Recipe.objects.create(
            recipe_name = recipe_name ,
            recipe_des = recipe_des ,
            recipe_img = recipe_img,
        )
    
        return redirect('/receipes/')
    
    queryset = Recipe.objects.all()
    context = {'receipes' : queryset}
    
    return render(request ,'receipes.html', context)
