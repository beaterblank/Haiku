from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from data_api.models import User,Follow,Content
from data_api.views import get_user_content
from django.http import Http404
# Create your views here.

def user(request,username,page=1):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    

    is_self = False
    if request.user.id == user.id:
        is_self = True
    
    is_following = Follow.objects.filter(follower_id=request.user.id,followee_id=user.id).exists()

    if(request.method == 'POST'):
        print("posting",is_self,is_following)

    if(request.method == 'POST' and not is_self):
        if not is_following:
            Follow(follower_id=request.user.id,followee_id=user.id).save()
            is_following = True
        else:
            Follow.objects.filter(follower_id=request.user.id,followee_id=user.id).delete()
            is_following = False

    context = {
        'user': user,
        'data': {
            'follower_count': Follow.objects.filter(followee_id=user.id).count(),
            'followee_count': Follow.objects.filter(follower_id=user.id).count(),
            'content_list': [ {'id':x.content_id,'body':x.body,'created_at':x.created_at,'username':x.username} for x in get_user_content(user.id,page)],
            'page':page,
            'is_self':is_self,
            'is_following':is_following
        }       
    }
    return render(request, 'application/user.html',context=context)

@login_required
def post(request):
    if(request.method == 'POST'):
        Content(user_id=request.user.id,body=request.POST['body']).save()
        return redirect(f'/user/{request.user.username}/1')
    return render(request, 'application/post.html')