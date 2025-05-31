from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product
from catalog.constants import FORBIDDEN_WORDS

forbidden_list = FORBIDDEN_WORDS

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):

        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip().lower()
        words_in_name = name.split()

        for word in words_in_name:
            if word in FORBIDDEN_WORDS:
                raise ValidationError (f"Введено  недопустимое  слово '{word}'.")
        return cleaned_data.get('name')

    def clean_description(self):

        cleaned_data = super().clean()
        description = cleaned_data.get('description').strip().lower()
        words_in_description = description.split()

        for word in words_in_description:
            if word in forbidden_list:
                raise ValidationError (f"Введено  недопустимое  слово '{word}'.")
        return cleaned_data.get('description')

    def clean_price(self):

        cleaned_data = super().clean()
        data = cleaned_data.get('price')
        price = float(data)

        if price < 0:
            raise ValidationError (f"Цена не может быть отрицательной.")
        return price

