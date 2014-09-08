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
	print(request.COOKIES.get('fb_access_token'))
	return render_to_response("index.html",locals())

def test(request):
	print('test')
	return render_to_response('test.html',locals())

def login(request):
	fb_access_token = request.COOKIES.get('fb_access_token')
	fb_graph = facebook.GraphAPI(fb_access_token)
	fb_user = fb_graph.get_object("me")
	args = {"height":"50","type":"normal","width":"50"}
	fb_img = fb_graph.get_object("me/picture",**args)
	print(fb_user)
	print(fb_user['id'])
	try:
		fbUser = FBUser.objects.get(id=fb_user['id'])
		user = fbUser.user
	except FBUser.DoesNotExist:
		user = None
	if user is  None:
		print('this user dont exists')
		fbU = FBUser(id=fb_user['id'], name=fb_user['name'], firstName=fb_user['first_name'], lastName=fb_user['last_name'], link=fb_user['link'])
		fbU.save()
		user= User(name=fb_user['name'],email='',fbUser=fbU)
		user.save()
	else:
		print('this user already exists')
		user = FBUser.objects.get(id=fb_user['id'])
	request.session['login'] = 'True'
	request.session['userName'] = user.name
	request.session['userImg'] = fb_img['url']
	print(fb_access_token)
	print(request.session['userImg'])
	return HttpResponseRedirect("/")

def logout(request):
	print('logout')
	request.session.flush()
	#request.session['login'] = False
	#request.session['userName'] = ''
	#delete(request)
	return HttpResponseRedirect("/")

def delete(request):
	fb_access_token = request.COOKIES.get('fb_access_token')
	fb_graph = facebook.GraphAPI(fb_access_token)
	args = {"method":"delete"}
	print("before")
	fb_page = fb_graph.request("me/permissions",**args)
	print(fb_page)