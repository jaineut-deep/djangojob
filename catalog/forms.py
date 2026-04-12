import re
from django import forms
from .models import Product

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

def validate_price(price):
    if price < 0:
        raise forms.ValidationError("Цена не может быть отрицательной")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            for forbidden_word in forbidden_words:
                pattern = re.compile(forbidden_word)
                if re.search(pattern, name, flags=re.IGNORECASE):
                    raise forms.ValidationError("В Наименовании нельзя использовать запрещённые слова")
        return name

    @classmethod
    def clean_description(cls, cleaned_data=None):
        description = cleaned_data.get("description")
        if description:
            for forbidden_word in forbidden_words:
                pattern = re.compile(forbidden_word)
                if re.search(pattern, description, flags=re.IGNORECASE):
                    raise forms.ValidationError("В Описании нельзя использовать запрещённые слова")
        return description

    purchase_price = forms.IntegerField(validators=[validate_price])

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        purchase_price = cleaned_data.get("purchase_price")
        if name and description and purchase_price:
            return cleaned_data
        return None
