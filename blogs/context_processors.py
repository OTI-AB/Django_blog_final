from assignments.models import Social
from blogs.models import Category, Blog



def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social(request):
    social = Social.objects.all()
    return dict(social = social)

def get_blogs(request):
    posts = Blog.objects.all()
    return dict(posts=posts)
