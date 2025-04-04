# TODO_BACKEND|


/api/   rest_framework.routers.APIRootView      api-root
/api/<drf_format_suffix:format> rest_framework.routers.APIRootView      api-root
/api/tasks/     myproject.urls.TaskViewSetRestricted    task-list
/api/tasks/<pk>/        myproject.urls.TaskViewSetRestricted    task-detail
/api/tasks/<pk>\.<format>/      myproject.urls.TaskViewSetRestricted    task-detail
/api/tasks\.<format>/   myproject.urls.TaskViewSetRestricted    task-list
