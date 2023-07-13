from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Name, Lottery
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Count, Sum, Q, FloatField


# Create your views here.

class LotteryCreate(CreateView):
    model = Lottery
    fields = '__all__'
    success_url = reverse_lazy('countalllottery')


class LotteryUpdate(UpdateView):
    model = Lottery
    fields = '__all__'
    success_url = reverse_lazy('history')


def index(request):
    sum_spends = Name.objects.aggregate(sum=Sum('lottery__price'))
    sum_wins = Name.objects.aggregate(sum=Sum('lottery__result'))
    global_result = sum_wins['sum'] - sum_spends['sum']
    total_number_of_tickets = Lottery.objects.all().count()
    total_number_of_wins = Lottery.objects.filter(Q(result__gt=1)).count()

    context = {
        'sum_spends': sum_spends,
        'sum_wins': sum_wins,
        'global_result': global_result,
        'total_number_of_tickets': total_number_of_tickets,
        'total_number_of_wins': total_number_of_wins,
    }
    return render(request, 'index.html', context)


class LotteryListView(generic.ListView):
    model = Lottery
    paginate_by = 40

    def get_queryset(self):
        return Lottery.objects.all().order_by('-date')

def countalllottery(request):
    sort = 'count'
    get = request.GET.get('sort_by', default={'sort_by': ''})
    if 'result' in get:
        sort = '-result'
    if 'math_waiting' in get:
        sort = '-math_waiting'
    name_list = Name.objects.annotate(count=Count('lottery'),
                                     summ_spends=Sum('lottery__price', default=0),
                                     summ_result=Sum('lottery__result', default=0),
                                     result=Sum('lottery__result', default=0) - Sum('lottery__price', default=0),
                                     persent_win=Count('lottery__result', filter=Q(lottery__result__gt=1)),
                                      math_waiting=((Sum('lottery__result', default=0) - Sum('lottery__price', default=0)) / Count('lottery')),
                                     ).order_by(sort)
    context = {
        'name_list': name_list,
    }

    return render(request, 'enterstat/name_list.html', context)

class LotteryJackpotUpdate(UpdateView):
    model = Name
    fields = '__all__'
    success_url = reverse_lazy('countalllottery')
