from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .price_search import bookoff_price,valuebooks_price
# Create your views here.

def mainPage(request):
    return render(request,'huruhonApp/index.html')


class MainPage(TemplateView) :

    template_name = 'huruhonApp/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
    def post(self,request,*args,**kwargs):
        workname = request.POST['workname']
        authername = request.POST['authername']
        publishername = request.POST['publishername']
        bookoff_dict = bookoff_price.bookoff_search(workname,authername,publishername)
        valuebooks_dict = valuebooks_price.valuebooks_search(workname,authername,publishername)
        self.kwargs['books'] = {'booktitle' : workname ,
            'bookoff' : { 'usedOrNew' : bookoff_dict['usedOrNew'] , 'price' : bookoff_dict['price'] },
            'valuebooks' : {'usedOrNew' : valuebooks_dict['usedOrNew'] , 'price' : valuebooks_dict['price'] }
            }
        
        
        return render(request,self.template_name, context=self.kwargs)
        
    """
        {'books' : [{'booktitle' : '△','bookoff' : {'usedOrNew' : '中古','price' : ooo},'valuebooks' : {'usedOrNew' : '中古','price' : xxx}}]}
        <ul>
            <li>{{ direct_dict.name }}</li>
            {% for key, value in direct_dict.kinds.items %}
            <ul>
                <li>{{ key }} - {{ value }}</li>
            </ul>
            {% endfor %}
        </ul>
    """