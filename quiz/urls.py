from django.urls import path, include
from . import views
from . import api
urlpatterns = [
    path('add/', views.add_quiz, name="add_quiz"),
    path('search-ques/', views.search_ques, name="search-ques"),
    path('list/', views.quiz_list, name="quiz_list"),
    path('profile/', views.select_quiz_profile_api, name = 'select_quiz_profile_api'),

    path('add_ques/', views.add_ques, name="add_ques"),
    path('ques_list/', views.ques_list, name="ques_list"),

    path('api/select-questions/', views.select_question_api, name = 'select_question_api'),
    path('api/add-quiz-question/', views.add_quiz_question_api, name = 'add_quiz_question_api'),
    path('api/del-quiz-question/', views.del_quiz_question_api, name = 'del_quiz_question_api'),
    path('api/get-quiz-questions/', views.get_quiz_questions_api, name = 'get_quiz_questions_api'),
    path('api/quiz-attempt/questions/', views.attempt_quiz_questions_api, name="attempt_quiz_questions_api"),
    path('api/attempt-quiz-answer/', views.attempt_quiz_answer, name="attempt_quiz_answer"),

    path('attempt-quiz/<str:quiz_id>/', views.attempt_quiz, name="attempt_quiz"),

    path('api/evaluate-quiz/', views.evaluate_quiz_master, name="evaluate_quiz_master"),
    path('getcsv/', views.getCSV, name="csv"),


    path('getResponseCSV/', views.getResponseCSV, name="res_csv"),
    path('graph/quiz/<str:quiz_id>/', api.latest_quiz_graph, name="latest_quiz_graph"),
    path('graph/level/<str:quiz_id>/', api.get_level_graph, name="get_level_graph"),

    path('quiz-analysis/', views.quiz_analysis, name="quiz_analysis"),

]