from django.contrib import admin
from django import forms

from Nlp.models import MyUser, diary_entries


class MyUserCreationForm(forms.ModelForm):
    """A form for creating new users.  Includes all the required fields, plus a repeated password."""

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class MyUserChangeForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['username',  'first_name', 'last_name', 'email', 'password']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    # The fields to be used in displaying the CocoUser model.
    # These override the definitions on the base UserAdmin that reference specific fields on auth.User.
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'password')

    fieldsets = (
        (None, {'fields': ('username', 'is_staff', 'first_name', 'last_name', 'email', 'password', 'is_superuser', 'paid_subscription', 'is_active')}),
    )

    search_fields = ('id', 'email', 'first_name', 'last_name',)
    ordering = ('last_name', 'first_name',)
    filter_horizontal = ()


class diary_entriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'time_create', 'time_update', 'user')
    list_display_links = ('id', 'text', 'user')
    search_fields = ('text', 'user')


# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)

admin.site.register(diary_entries, diary_entriesAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'
