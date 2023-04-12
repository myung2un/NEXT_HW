from django.shortcuts import render, redirect
from .models import Post, Comment


def home(request):
   posts = Post.objects.all()


   return render(request, 'home.html', {'posts':posts})


def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content)
       return redirect('detail', new_post.pk)
  
   return render(request, 'new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        content = request.POST['content']
        parent_id = request.POST.get('parent_id', None)

        if parent_id:
            parent = Comment.objects.get(pk=parent_id)
            Comment.objects.create(
                post=post,
                content=content,
                parent=parent,
            )
        else:
            Comment.objects.create(
                post=post,
                content=content
            )
        return redirect('detail', post_pk)

    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'detail.html', context)
   #return render(request, 'detail.html', {'post':post})





def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('detail', post_pk)


   return render(request, 'edit.html', {'post':post})




def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()


   return redirect('home')

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail',post_pk)

def delete_reply(request, post_pk, comment_pk, reply_pk):
    comment = Comment.objects.get(pk=comment_pk)
    reply = Comment.objects.get(pk=reply_pk)
    reply.delete()
    return redirect('detail', post_pk)
