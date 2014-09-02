from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.forms import ModelForm
from fb.models import *

# Create your views here.
import json
def main(request):
	action = str(request.GET.get("action",''))
	print("action: ")
	print(action)
	if action == 'login':
		print('FACEBOOKLOGIN')
		userDataJSON = str(request.POST.get("jsonStr",''))											
		userData = json.loads(userDataJSON)
		if FBUser.objects.filter(id=userData['id']).count() == 0:
			print('this user dont exists')
			fbU = FBUser(id=userData['id'], name=userData['name'], firstName=userData['first_name'], lastName=userData['last_name'], link=userData['link'])
			fbU.save()
			user= User(name=userData['name'],email=userData['email'],fbUser=fbU)
			user.save()
		else:
			print('this user already exists')
	return render_to_response("index.html",context_instance=RequestContext(request))