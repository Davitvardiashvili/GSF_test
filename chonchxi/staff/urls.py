from django.urls import path, include
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('school/', views.school, name='school'),
    path('school-delete/<event_id>', views.delete_school, name='delete-school'),
    path('school-update/<event_id>', views.updateSchool, name='update-school'),
    path('comp/', views.competitor, name='competitors'),
    path('comp_delete/<event_id>', views.delete_competitor, name='delete-competitor'),
    path('comp-update/<event_id>', views.updateCompetitor, name='update-competitor'),
    path('seasons/', views.season, name='seasons'),
    path('season-update/<event_id>', views.updateSeason, name='update-season'),
    path('season_delete/<event_id>', views.deleteSeason, name='delete-season'),
    path('stage/', views.stage, name='stage'),
    path('stage-update/<event_id>', views.updateStage, name='update-stage'),
    path('stage_delete/<event_id>', views.deleteStage, name='delete-stage'),
    path('group/', views.group, name='group'),
    path('group-update/<event_id>', views.updateGroup, name='update-group'),
    path('group_delete/<event_id>', views.deleteGroup, name='delete-group'),
    path('shake/', views.shake, name='shake'),
    path('shake_delete/<event_id>', views.deleteShake, name='delete-shake'),
    path('shuffle/<int:pk>', views.shuffle, name='shuffle-add'),


]
