from random import *
from django.shortcuts import render

# Create your views here.
def lotto(request):
    lotto = sample(range(1, 46), 6)
    while True:
        bonus = randint(1, 46)
        if not bonus in lotto:
            break
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for _ in range(1000):
        numbers = sample(range(1, 46), 6)
        if set(numbers) == set(lotto):
            one += 1
        cnt = 0
        for i in numbers:
            if i in lotto:
                cnt += 1
        if cnt == 3:
            five += 1
        if cnt == 4:
            four += 1
        if cnt == 5:
            three += 1
        if cnt == 5:
            if bonus in numbers:
                two += 1
    die = 1000 - (one+two+three+four+five)
            
    context = {
        'lotto': lotto,
        'bonus': bonus,
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five,
        'die': die,
    }
    return render(request, 'pages/lotto.html', context)