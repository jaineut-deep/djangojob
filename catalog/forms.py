from django import forms
from .models import Product

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

def validate_price(price):
    if price < 0:
        raise forms.ValidationError("Цена не может быть отрицательной")


class MixinProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите наименование"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "placeholder": "Добавьте описание"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["purchase_price"].widget.attrs.update({"class": "form-control", "placeholder": "Укажите цену"})


class ProductForm(MixinProductForm, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "purchase_price"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            for forbidden_word in forbidden_words:
                if forbidden_word in name.lower():
                    raise forms.ValidationError("В Наименовании нельзя использовать запрещённые слова")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            for forbidden_word in forbidden_words:
                if forbidden_word in description.lower():
                    raise forms.ValidationError("В Описании нельзя использовать запрещённые слова")
        return description

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price < 0:
            validate_price(purchase_price)
        return purchase_price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        purchase_price = cleaned_data.get("purchase_price")
        if name and description and purchase_price:
            return cleaned_data
        return None
