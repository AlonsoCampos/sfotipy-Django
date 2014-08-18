from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm


def signup(request):
	# Dice que se crea si llaga por Post o sino es vacio
	form = UserCreationEmailForm(request.POST or None)
	
	if form.is_valid():
		form.save()

	return render(request,'signup.html',{'form':form})

def singin(request):
	form = EmailAuthenticationForm(request.POST or None)

	#if form.is_valid():
		#logerar

	return render(request, 'singin.html',{'form':form})