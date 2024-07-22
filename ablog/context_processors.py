from .models import Category

def categories_context_processor(request):
    cat_menu = Category.objects.all()
    return {'cat_menu': cat_menu}