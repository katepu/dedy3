from django.shortcuts import render
from myapp1.models import Worker, Equipment

# тут принимаются запросы и возвращаются ответы

def index_page(request):
    all_workers = Worker.objects.all() #получить все записи из таблицы Worker = все обьекты нашей модели
    #workers_filtered = Worker.objects.filter(age=37) #отфильтровать по возрасту
    #print(workers_filtered)
    #all_equipment = Equipment.objects.all()
    # print(all_equipment)

    return render(request, 'index.html', context={'workers': all_workers})
    #context - это словарь, в котором ключи - это переменные в шаблоне, а значения - это значения этих переменных
    #в шаблоне мы обращаемся к переменным через {{}}
