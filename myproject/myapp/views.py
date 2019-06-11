from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.
def main(request):
    post_list = Post.objects.all()
    return render(request, 'main.html', {'post_list':post_list})

def detail(request, post_id):
    post=Post.objects.get(id=post_id)
    comments = post.comment_set.all().order_by('-pub_date')
    return render(request,"detail.html", {'post':post, 'comments': comments})

def create(request):
    if request.method=="POST":
        post=Post()
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('main')

    else:
        return render(request, 'create.html')

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    # 각 글의 고유한 아이디를()에 넣어야함, id=는 변수, post_id=상수값. 
    post.delete()
    return redirect('main')

#어려운 부분: 갱신하기
def edit(request,post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('')       

    else:
        post=Post.objects.get(id=post_id)
        return render (request, 'edit.html',{"post": post})

def comment_create(request, post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        comment=Comment(post=post)
        # 파랑포스트는 models에 있는 변수 post, 흰 포스트는 객체의 값 특정된 것(엄마=엄마이름)
        comment.content=request.POST['content']
        comment.save()
        
        return redirect('detail',post_id)

def result(request):
        text= request.GET['fulltext']
        words=text.split()
        # 텍스트를 공백기준으로 나눠 스트링으로 만들어줌
        word_dic = {}

        for word in words:
                if word in word_dic:
                # increase
                         word_dic[word]+=1
                else:
                        # add to dic
                        word_dic[word]=1

        return render(request, 'result.html', {'full': text, 'total':len(words), 'dic': word_dic.items()})

# len(words)=원문을 공백 기준으로 나눴을 때 생긴 단어들을 리스트에 넣은 뒤, 리스트의 길이를 세면 총 단어수!
