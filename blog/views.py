from django.shortcuts import render, get_object_or_404
from .models import Post , Author, Tag
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blogs/index.html", {
      "posts": latest_posts
    })

def add_post(request):
     authors = Author.objects.all()
     tag = Tag.objects.all()
     return render(request, "blogs/add_post.html",{'authors': authors, 'tags': tag})

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blogs/all-posts.html", {
      "all_posts": all_posts
    })

def save_post(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        excerpt = request.POST.get('excerpt')
        image_name = request.POST.get('image')
        content = request.POST.get('content')
        author_id = request.POST.get('author')
        tag_ids = request.POST.getlist('tag') 

        post = Post.objects.create(
            title=title,
            excerpt=excerpt,
            image_name=image_name,
            content=content,
            author_id=author_id,
        )

        post.tags.add(*tag_ids)
        response_data = {'message': 'Post saved successfully.'}
        messages.success(request, response_data['message'])
     else:
        response_data = {'message': 'Post Not Saved!!'}
        messages.error(request, response_data['message'])
     return JsonResponse(response_data)

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    print (identified_post)
    return render(request, "blogs/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tags.all()
    })

def delete_post(request, post_id):
       post = Post.objects.get(id=post_id)
       post.delete()
       response_data = {'message': 'Post deleted successfully!!'}
       messages.error(request, response_data['message'])
       return JsonResponse(response_data)