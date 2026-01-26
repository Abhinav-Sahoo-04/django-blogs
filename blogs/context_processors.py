

from blogs.models import Category


def get_context(request):
    categories=Category.objects.all()
    return dict(categories=categories)