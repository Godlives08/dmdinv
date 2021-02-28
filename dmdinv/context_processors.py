from django.shortcuts import get_object_or_404, render
from home.models import Grupo_Itemurl
from user.models import User
from django.db.models import Q
from django.db import connection 
#print (connection.queries)

def grupomenu(request):
    user = get_object_or_404(User,username = request.user)
    niveladmin = user.niveladmin
    nivelsecurity = user.nivelsecurity
    suser = user.is_staff
    grupo_itemurl = Grupo_Itemurl.objects.filter(Q(active=True), (Q(itemurl__niveladmin__lte=niveladmin) | Q(itemurl__nivelsecurity__lte=nivelsecurity) | Q(itemurl__is_staff=suser))).order_by('order')
    context = {'grupo_itemurl': grupo_itemurl}
    #print(Grupo_Itemurl.objects.filter(Q(active=True), (Q(itemurl__niveladmin__lte=niveladmin) | Q(itemurl__nivelsecurity__lte=nivelsecurity)| Q(itemurl__is_staff=suser))).order_by('order').query)
    return context

