from django import forms
from product.models import Category, Product 


# Create your forms here.
class productForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','price','category','description','search_tags','available','image')

class categoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__' 