from .models import *

menu = [{'title': "Додати запис", 'url_name': 'add'},
        {'title': "Мої записи", 'url_name': 'my'},
        {'title': "Про сайт", 'url_name': 'about'},
        {'title': "Підписка", 'url_name': 'pay'}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
        #
        #
        # context['cats'] = cats
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context
