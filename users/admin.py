from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from users.models import User


class UserCreationForm(forms.ModelForm):
    """
    Класс для формы регистрации пользователя.
    """

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        """
        Метод проверяет введенные пароли.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Введенные пароли не совпадают")
        return password2

    def save(self, commit=True):
        """
        Метод сохраняет пароль пользователя.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    """
    Класс для настройки admin-панели.
    """

    add_form = UserCreationForm

    list_display = ['username', 'first_name', 'last_name', ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Информация о пользователе', {'fields': ('first_name', 'last_name',)}),
        ('Права доступа', {'fields': ("is_active", "is_staff", "is_superuser",)}))

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
