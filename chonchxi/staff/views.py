from django.shortcuts import render, redirect
from .forms import CompetitorForm, SchoolForm, SeasonForm, StageForm, ShakeForm, GroupForm
from .models import Competitor, School, Season, Stage, Group, Shake, Discipline
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .filters import Orderfilter, GroupFilter, ShakeFilter


@login_required(login_url='login')
def school(request):
    form = SchoolForm()

    if request.method == "POST":
        pDict = request.POST.copy()
        form = SchoolForm(pDict)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/school')

    regions = School.objects.all()
    count = School.objects.all().count()

    context = {'form': form, 'regions': regions, 'count': count}
    return render(request, 'staff/School.html', context)


@login_required(login_url='login')
def updateSchool(request, event_id):
    skola = School.objects.get(pk=event_id)
    form = SchoolForm(instance=skola)

    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=skola)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/school/')

    context = {'form': form}
    return render(request, 'staff/School.html', context)


@login_required(login_url='login')
def delete_school(request, event_id):
    skola = School.objects.get(id=event_id)
    if request.method == 'POST':
        skola.delete()
        return redirect('school')
    return render(request, 'staff/delete.html', {'obj': skola})


@login_required(login_url='login')
def competitor(request):
    form = CompetitorForm()

    if request.method == 'POST':
        form = CompetitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/comp/')

    competitors = Competitor.objects.all()
    myfilter = Orderfilter(request.GET, queryset=competitors)
    competitors = myfilter.qs
    count = Competitor.objects.all().count()

    context = {'form': form, 'competitors': competitors, 'count': count, 'myfilter': myfilter}
    return render(request, 'staff/index.html', context)


@login_required(login_url='login')
def updateCompetitor(request, event_id):
    competitor = Competitor.objects.get(id=event_id)
    form = CompetitorForm(instance=competitor)

    if request.method == 'POST':
        form = CompetitorForm(request.POST, instance=competitor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/comp/')

    context = {'form': form}
    return render(request, 'staff/index.html', context)


@login_required(login_url='login')
def delete_competitor(request, event_id):
    competitor = Competitor.objects.get(pk=event_id)
    if request.method == "POST":
        competitor.delete()
        return redirect('competitors')
    return render(request, 'staff/delete.html', {'obj': competitor})


@login_required(login_url='login')
def season(request):
    form = SeasonForm()
    if request.method == "POST":
        pDict = request.POST.copy()
        form = SeasonForm(pDict)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/seasons')

    seasons = Season.objects.all()
    count = Season.objects.all().count()

    context = {'form': form, 'seasons': seasons, 'count': count}
    return render(request, 'staff/season.html', context)


@login_required(login_url='login')
def updateSeason(request, event_id):
    sezoni = Season.objects.get(pk=event_id)
    form = SeasonForm(instance=sezoni)

    if request.method == 'POST':
        form = SeasonForm(request.POST, instance=sezoni)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/seasons')

    context = {'form': form}
    return render(request, 'staff/season.html', context)


@login_required(login_url='login')
def deleteSeason(request, event_id):
    sezoni = Season.objects.get(id=event_id)
    if request.method == 'POST':
        sezoni.delete()
        return redirect('seasons')
    return render(request, 'staff/delete.html', {'obj': sezoni})


@login_required(login_url='login')
def stage(request):
    form = StageForm()

    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/stage')

    stages = Stage.objects.all()

    count = Stage.objects.all().count()

    context = {'form': form, 'stages': stages, 'count': count}
    return render(request, 'staff/stage.html', context)


@login_required(login_url='login')
def updateStage(request, event_id):
    etapi = Stage.objects.get(pk=event_id)
    form = StageForm(instance=etapi)

    if request.method == 'POST':
        form = StageForm(request.POST, instance=etapi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/stage')

    context = {'form': form}
    return render(request, 'staff/stage.html', context)


@login_required(login_url='login')
def deleteStage(request, event_id):
    etapi = Stage.objects.get(pk=event_id)
    if request.method == "POST":
        etapi.delete()
        return redirect('stage')
    return render(request, 'staff/delete.html', {'obj': etapi})


@login_required(login_url='login')
def group(request):
    form = GroupForm()

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/group')

    groups = Group.objects.all()
    group_filter = GroupFilter(request.GET, queryset=groups)
    groups = group_filter.qs
    count = Group.objects.all().count()

    context = {'form': form, 'groups': groups, 'count': count, 'group_filter': group_filter}
    return render(request, 'staff/group.html', context)


@login_required(login_url='login')
def updateGroup(request, event_id):
    jgufi = Group.objects.get(pk=event_id)
    form = GroupForm(instance=jgufi)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=jgufi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/group')

    context = {'form': form}
    return render(request, 'staff/group.html', context)


@login_required(login_url='login')
def deleteGroup(request, event_id):
    jgufi = Group.objects.get(pk=event_id)
    if request.method == "POST":
        jgufi.delete()
        return redirect('group')
    return render(request, 'staff/delete.html', {'obj': jgufi})


@login_required(login_url='login')
def shake(request):
    form = ShakeForm()
    groups = Group.objects.all()
    seasons = Season.objects.all()
    stages = Stage.objects.all()
    discipline = Discipline.objects.all()

    if request.method == 'POST':
        form = ShakeForm(request.POST)
        if form.is_valid():
            form.save()
            return (HttpResponseRedirect('/staff/shake'))

    competitor_groups = Shake.objects.all()
    shake_filter = ShakeFilter(request.GET, queryset=competitor_groups)
    competitor_groups = shake_filter.qs
    count = Shake.objects.all().count()

    context = {'form': form, 'groups': groups, 'shake_filter': shake_filter,
               'seasons': seasons, 'stages': stages, 'discipline': discipline,
               'competitor_groups': competitor_groups, 'count': count}
    return render(request, 'staff/shake.html', context)


@login_required(login_url='login')
def deleteShake(request, event_id):
    korn = Shake.objects.get(pk=event_id)
    if request.method == "POST":
        korn.delete()
        return redirect('shake')
    return render(request, 'staff/delete.html', {'obj': korn})


@login_required(login_url='login')
def shuffle(request, pk):
    room = Shake.objects.filter(pk=pk)
    competitors = Competitor.objects.all()
    myfilter = Orderfilter(request.GET, queryset=competitors)
    competitors = myfilter.qs
    context = {'myfilter': myfilter, 'room': room, 'competitors': competitors}

    return render(request, 'staff/shuffle-add.html', context)
