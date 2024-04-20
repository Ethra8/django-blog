from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Post


# Create your views here.

# def my_blog(request):
#     return HttpResponse("Hello, Blog!")

class PostList(generic.ListView):
    # model = Post --> does exactly the same as queryset = Post.objects.all() but NO FILTERS
    queryset = Post.objects.filter(status=1)  # noqa does the same as model = Post but YES FILTERS
    # queryset = Post.objects.all().order_by("created_on")  # noqa POWERFUL .order_by() method // add - to reverse order ("-created_on")
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )