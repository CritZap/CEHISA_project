from django import forms
from models import Menu

class Meta:
	model = Menu
	fields = ['text']
