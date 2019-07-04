from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Tag
from django.db.models import Q
from django.contrib import messages
from .forms import ShareForm
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


class BlogHome(generic.ListView):

    model = Post

    paginate_by = 4

    template_name = 'post/home.html'

class PostDetailView(generic.DetailView):

    model = Post

class SearchView(generic.View):

    def get(self, request):

        data = request.GET.get('q', None)

        queryset = Post.objects.filter(
            Q(title__icontains=data)|
            Q(content__icontains=data)|
            Q(author__username__icontains=data)|
            Q(tags__name__icontains=data)

        )

        ctx = {
            "object_list":queryset
        }

        messages.info(request,f"Search result for {data}")

        return render(request,'post/home.html', ctx)

def share_post_view(request, pk):

    form = ShareForm(request.POST or None)

    instance = None

    if pk:
        
        # instance = Post.objects.get(pk=pk)

        instance = get_object_or_404(Post, pk=pk)

    context = {
        'form':form,
        'instance': instance
    }

    if request.method == "POST":
        
        if form.is_valid():
        
            cd = form.cleaned_data


            name = cd.get('name')
            
            to_email = cd.get('to')
            
            from_email = cd.get('email')
            
            message = cd.get('message')
            
            link = reverse('post:detail', kwargs={"slug":instance.slug})

            subject = f"{name} ({from_email}) recommend you reading {instance.title}"

            body = f"Read {instance.title} at {link}\n\n{message}"
            
            send_mail(subject,body,'myblog@myblog.com',[to_email])

            context['email_sent'] =  True

    return render(request, 'post/share_post.html', context)
