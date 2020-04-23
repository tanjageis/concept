from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Phrase, Concept, Token

def home(request):
	context = {
		'first_name': 'Tanja',
		'last_name': 'Geis',
		'concepts': Concept.objects.all(),
		'phrases': Phrase.objects.all(),
	}
	return render(request, 'home.html', context)

class TokenList(ListView):
	model = Token

class TokenDetail(DetailView):
	model = Token

class CreateToken(CreateView):
	model = Token
	fields = ('color', 'is_primary')
	success_url = ('/tokens/')

class UpdateToken(UpdateView):
	model = Token
	fields = ('concept',)