from django.http import JsonResponse
from django.shortcuts import render
from .models import User,Content,Follow,Like
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

def get_users():
    user_list = User.objects.raw('SELECT DISTINCT id,username FROM auth_user')
    return JsonResponse({'user_list':[{'id':x["id"],"username":x["username"]} for x in user_list]})

def get_user_content(user_id,page_num=1):
    content_list = Content.objects.raw('SELECT DISTINCT c.*,u.username FROM data_api_content c JOIN auth_user u ON c.user_id=u.id WHERE c.user_id = %s ORDER BY c.created_at LIMIT %s,10;', [user_id, (page_num-1)*10])
    return content_list

def get_user_followee_content(user_id,page_num=1):
    content_list = Content.objects.raw('SELECT * FROM data_api_content WHERE user_id IN (SELECT followee_id FROM data_api_follow WHERE follower_id = %s) ORDER BY created_at LIMIT %s,10;', [user_id, (page_num-1)*10])
    return content_list
