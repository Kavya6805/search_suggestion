from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


names = [
    "Anna", "Brittany", "Cinderella", "Diana", "Eva", "Fiona", "Gunda", "Hege",
    "Inga", "Johanna", "Kitty", "Linda", "Nina", "Ophelia", "Petunia", "Amanda",
    "Raquel", "Cindy", "Doris", "Eve", "Evita", "Sunniva", "Tove", "Unni",
    "Violet", "Liza", "Elizabeth", "Ellen", "Wenche", "Vicky"
]


def searchSuggestion(request):
    return render(request,"index.html")


def getSuggestion(request):
    q=request.GET.get('query','').lower()
    print(q)
    for name in names:
        if name.lower().startswith(q):
            hint=name
            print(hint)
            return JsonResponse(hint,safe=False)
    return JsonResponse('no suggestion',safe=False)