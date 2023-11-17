from django.shortcuts import render


def index(request):
    context_dict = {'text': 'Hello world', 'number': 101}
    return render(request, 'basic_app/index.html', context_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
