import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .constants import DRINKS_PRICE
from .forms import SaleForm, ReportForm
from .models import Drink, Staff


def sale_form(request):
    if request.method == 'POST':

        data = request.POST.copy()
        data['price_per_cup'] = DRINKS_PRICE[data['name']]
        form = SaleForm(data)
        if form.is_valid():
            form.save(commit=False)
            form.price_per_cup = DRINKS_PRICE[form.data['name']]
            form.save()
    else:
        form = SaleForm()
    Drink_objs = Drink.objects.last()

    return render(request, 'name.html', {'form': form, 'Drink_objs':[Drink_objs]})


def report(request):
    if request.method == 'POST':
        report_objs = []
        start_date = datetime.datetime.strptime(request.POST['Start_date'],'%Y-%m-%d')
        end_date = datetime.datetime.strptime(request.POST['End_date'],'%Y-%m-%d')
        staff = Staff.objects.get(name=request.POST['User'])
        cp = staff.commission_percentage/100

        for n in range(int((end_date - start_date).days) + 1):
            created = start_date + datetime.timedelta(n)
            Drink_objs = Drink.objects.filter(
                sold_by=staff,
                created__gte=datetime.datetime.combine(created, datetime.time.min),
                created__lte=datetime.datetime.combine(created, datetime.time.max)
            )
            if Drink_objs:
                query_obj = {}
                query_obj['date'] = created
                query_obj['items'] = [obj.name for obj in Drink_objs]
                query_obj['total'] = sum([obj.price_per_cup for obj in Drink_objs])
                query_obj['commission'] = sum([obj.price_per_cup * cp for obj in Drink_objs])
                report_objs.append(query_obj)

        return render(request, 'report.html', {'Drink_objs':report_objs, 'Sales_person':staff.name} )
    else:
        form = ReportForm()
        return render(request, 'getreport.html', {'form':form})
