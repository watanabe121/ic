from django.db.models import Model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from icorder.forms import PrintLamiCreateFormSet, PrintLamiCreateForm, PlateCreateFormSet, PlateCreateForm
from .models import Customer, PlateCustomer
from django.db.models import Q


class IndexView(TemplateView):
    template_name = "index.html"


class SearchResultView(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Customer.objects.filter(
                Q(customer_name__icontains=q_word) | Q(order_number__icontains=q_word))
        else:
            object_list = Customer.objects.all()
        return object_list


class PlateSearchResultView(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = PlateCustomer.objects.filter(
                Q(customer_name__icontains=q_word) | Q(order_number__icontains=q_word))
        else:
            object_list = PlateCustomer.objects.all()
        return object_list


def add_panel(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        panel_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if panel_formset.is_valid():
            post.save()
            panel_formset.save()
            return redirect('/')

        else:
            context['panel_formset'] = panel_formset

    else:
        context['panel_formset'] = PrintLamiCreateFormSet()

    return render(request, "panel_create.html", context)


def add_gom(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        gom_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if gom_formset.is_valid():
            post.save()
            gom_formset.save()
            return redirect('/')

        else:
            context['gom_formset'] = gom_formset

    else:
        context['gom_formset'] = PrintLamiCreateFormSet()

    return render(request, 'icorder/gom_create.html', context)


def add_sheet(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        sheet_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if sheet_formset.is_valid():
            post.save()
            sheet_formset.save()
            return redirect('/')

        else:
            context['sheet_formset'] = sheet_formset

    else:
        context['sheet_formset'] = PrintLamiCreateFormSet()

    return render(request, 'icorder/sheet_create.html', context)


def add_window(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        window_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if window_formset.is_valid():
            post.save()
            window_formset.save()
            return redirect('/')

        else:
            context['window_formset'] = window_formset

    else:
        context['window_formset'] = PrintLamiCreateFormSet()

    return render(request, 'icorder/window_create.html', context)


def add_yuka(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        yuka_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if yuka_formset.is_valid():
            post.save()
            yuka_formset.save()
            return redirect('/')

        else:
            context['yuka_formset'] = yuka_formset

    else:
        context['yuka_formset'] = PrintLamiCreateFormSet()

    return render(request, 'icorder/yuka_create.html', context)


def add_printlami(request):
    form = PrintLamiCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        printlami_formset = PrintLamiCreateFormSet(request.POST, files=request.FILES, instance=post)
        if printlami_formset.is_valid():
            post.save()
            printlami_formset.save()
            return redirect('/')

        else:
            context['printlami_formset'] = printlami_formset

    else:
        context['printlami_formset'] = PrintLamiCreateFormSet()

    return render(request, 'icorder/printlami_create.html', context)


def add_plate(request):
    form = PlateCreateForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        plate_formset = PlateCreateFormSet(request.POST, files=request.FILES, instance=post)
        if plate_formset.is_valid():
            post.save()
            plate_formset.save()
            return redirect('/')

        else:
            context['plate_formset'] = plate_formset

    else:
        context['plate_formset'] = PlateCreateFormSet()

    return render(request, 'icorder/plate_create.html', context)
