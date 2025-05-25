from django.urls import reverse_lazy

from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview_image")
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "content", "preview_image")

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs = { 'pk': self.object.pk,})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
