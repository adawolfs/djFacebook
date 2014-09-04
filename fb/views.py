from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.forms import ModelForm
from fb.models import *
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
import json
import facebook
import os
@ensure_csrf_cookie
def main(request):
	print('main')
	print(request.session['userName'])
	print(request.session['login'])
	return render_to_response("index.html",locals())

def test(request):
	print('test')
	return render_to_response('test.html',locals())

def login(request):
	userfbs = facebook.get_user_from_cookie(self.request.cookies, key, secret)
	print('login')
	if request.method == 'POST':
		userDataJSON = str(request.POST["jsonStr"])	
		
		if userfbs:
		    graph = facebook.GraphAPI(user["access_token"])
		    profile = graph.get_object("me")
		    friends = graph.get_connections("me", "friends")	
		print(userfbs	)
		userData = json.loads(userDataJSON)
		fbUser = FBUser.objects.get(id=userData['id'])
		user = fbUser.user
		if user is  None:
			print('this user dont exists')
			fbU = FBUser(id=userData['id'], name=userData['name'], firstName=userData['first_name'], lastName=userData['last_name'], link=userData['link'])
			fbU.save()
			user= User(name=userData['name'],email=userData['email'],fbUser=fbU)
			user.save()
		else:
			print('this user already exists')
			user = FBUser.objects.get(id=userData['id'])
		request.session['login'] = 'True'
		request.session['userName'] = user.name
		url = reverse('home')
		return HttpResponse(url)
	else:
		print('isn\'t post')
	print('aqui');
	return render_to_response("index.html",locals(),context_instance=RequestContext(request))

def logout(request):
	request.session['login'] = False
	request.session['userName'] = ''
	print(request.session['userName'])
	print(request.session['login'])
	return render_to_response("index.html",locals())