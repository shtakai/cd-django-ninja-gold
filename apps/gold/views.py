from django.shortcuts import render, redirect
import random
import datetime


def index(request):
    context = {}
    return render(request, 'gold/index.html', context)


def process_money(request):

    if not request.session.get('gold'):
        request.session['gold'] = 0

    if not request.session.get('activities'):
        request.session['activities'] = []

    if request.POST['house_type'] == 'farm':
        earn_gold = random.randint(10, 20)
        request.session['gold'] += random.randint(10, 20)
    elif request.POST['house_type'] == 'cave':
        earn_gold = random.randint(10, 20)
    elif request.POST['house_type'] == 'house':
        earn_gold = random.randint(10, 20)
    elif request.POST['house_type'] == 'casino':
        earn_gold = random.randint(-50, 50)

    if earn_gold < 0:
        earn_plus = False
        css_class = 'text-danger'
        activity = 'Entered a {} and lost {} gold(s)... Ouch... ({})'.format(
            request.POST['house_type'],
            earn_gold,
            datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p'))
    else:
        earn_plus = True
        css_class = 'text-info'
        activity = 'Earned {} gold(s) from the {} ({})'.format(
            earn_gold,
            request.POST['house_type'],
            datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p'))

    request.session['gold'] += earn_gold
    request.session['activities'].insert(0,
        {
            'activity': activity,
            'css_class': css_class,
        }
    )

    return redirect('/')
