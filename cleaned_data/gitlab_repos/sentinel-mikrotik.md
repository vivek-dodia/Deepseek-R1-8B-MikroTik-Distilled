# Repository Information
Name: sentinel-mikrotik

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/optic-telecom/sistemas/sentinel-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mikrotik.service
================================================
[Unit]
Description=gunicorn mikrotik daemon
After=syslog.target
After=network.target
[Service]
PIDFile=/run/gunicorn/pid
User=devel
Group=devel
WorkingDirectory=/home/devel/sites/sentinel-mikrotik/bin/
ExecStart=/bin/bash mikrotik_start.sh
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true
[Install]
WantedBy=multi-user.target
================================================

File: mikrotik_start.sh
================================================
#!/bin/bash
NAME="190.113.247.215" # Name of the application
DJANGODIR=/home/devel/sites/sentinel-mikrotik/sentinel-mikrotik # Django project directory
LOGFILE=/var/log/gunicorn/gunicorn_mikrotik.log
LOGDIR=$(dirname $LOGFILE)
SOCKFILE=/home/devel/sites/sentinel-mikrotik/run/gunicorn.sock # we will communicate using this unix socket
LOGDIR_PROJECT=/home/devel/sites/sentinel-mikrotik/logs # we will communicate using this unix socket
USER=devel # the user to run as
GROUP=devel # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.local # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi
TIMEOUT=600
#mikrotik si escuchara por ip
ADDRESS=0.0.0.0:8080
echo "Starting $NAME as `whoami`"
# Activate the virtual environment
#source /home/devel/sites/environments/sentinel/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Create the run directory if it doesn't exist for logs sentinel
test -d $LOGDIR_PROJECT || mkdir -p $LOGDIR_PROJECT
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
    --workers $NUM_WORKERS \
    --bind=$ADDRESS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
================================================

File: mikrotik_start_development.sh
================================================
#!/bin/bash
NAME="190.113.247.219" # Name of the application
DJANGODIR=/home/devel/sites/sentinel-mikrotik/sentinel-mikrotik # Django project directory
LOGFILE=/var/log/gunicorn/gunicorn_mikrotik.log
LOGDIR=$(dirname $LOGFILE)
SOCKFILE=/home/devel/sites/sentinel-mikrotik/run/gunicorn.sock # we will communicate using this unix socket
LOGDIR_PROJECT=/home/devel/sites/sentinel-mikrotik/logs # we will communicate using this unix socket
USER=devel # the user to run as
GROUP=devel # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=config.settings.local # which settings file should Django use
DJANGO_WSGI_MODULE=config.wsgi
TIMEOUT=600
#mikrotik si escuchara por ip
ADDRESS=0.0.0.0:8080
echo "Starting $NAME as `whoami`"
alias python='/usr/bin/python3.6'
#alias gunicorn='/home/devel/.local/bin/gunicorn'
# Activate the virtual environment
#source /home/devel/sites/environments/sentinel/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Create the run directory if it doesn't exist for logs sentinel
test -d $LOGDIR_PROJECT || mkdir -p $LOGDIR_PROJECT
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--workers $NUM_WORKERS \
--bind=$ADDRESS \
--user=$USER --group=$GROUP \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE
================================================

File: README.md
================================================
# sentinel-mikrotik
================================================

File: admin.py
================================================
from django.contrib import admin, messages
from import_export.admin import ImportExportModelAdmin
class BaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    date_hierarchy = 'created'
    actions = ['change_activation','change_status']
    def change_activation(self, request, queryset):
        model = self.model._meta.verbose_name
        n = queryset.count()
        message = "%(count)d %(model)s cambiadas." % {"count": n ,"model":model}
        self.message_user(request, message, messages.SUCCESS)   
        for item in queryset:
            if item.status_field:
                item.status_field = False
            else:
                item.status_field = True
            item.save()
        return queryset
    change_activation.short_description = 'Cambia el estado de la activacion'
    def change_status(self, request, queryset):
        if hasattr(self.model,'status'):
            model = self.model._meta.verbose_name
            n = queryset.count()
            message = "%(count)d %(model)s cambiadas." % {"count": n ,"model":model}
            self.message_user(request, message, messages.SUCCESS)   
            for item in queryset:
                if item.status:
                    item.status = False
                else:
                    item.status = True
                item.save()
        return queryset
    change_status.short_description = 'Cambia estatus'
================================================

File: backends.py
================================================
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import BaseAuthentication, CSRFCheck
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
User = get_user_model()
class EmailAuthBackend(ModelBackend):
    """Allow users to log in with their email address"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Some authenticators expect to authenticate by 'username'
        email = username
        if email is None:
            email = kwargs.get('username')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user.backend = "%s.%s" % (self.__module__, self.__class__.__name__)
                return user
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
================================================

File: mixins.py
================================================
import json
from django.views.generic.base import TemplateView
from django.shortcuts import get_list_or_404
from django.utils.html import escape
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django_datatables_view.base_datatable_view import DatatableMixin
from django_datatables_view.mixins import JSONResponseView,JSONResponseMixin, LazyEncoder
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
User = get_user_model()
@method_decorator(csrf_exempt, name='dispatch')
class DataTable(DatatableMixin, JSONResponseMixin, TemplateView):
    def get_initial_queryset(self):
        try:
            return self.model.objects.actives()
        except:
            return self.model.objects.filter(status_field=True)
    def render_column(self, row, column):
        """ Renders a column on a row. column can be given in a module notation eg. document.invoice.type
        """
        # try to find rightmost object
        obj = row
        parts = column.split('.')
        for part in parts[:-1]:
            if obj is None:
                break
            obj = getattr(obj, part)
        # try using display_OBJECT for choice fields
        if hasattr(self, 'display_%s' % parts[-1]):
            value = getattr(self, 'display_%s' % parts[-1])(obj)
        else:
            value = getattr(obj, parts[-1], None)
            if self.escape_values:
                value = escape(value)            
            if value and hasattr(obj, 'get_absolute_url'):
                return '<a href="%s">%s</a>' % (obj.get_absolute_url(), value)
            if value is None:
                value = self.none_string
        return value
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            self.pk = kwargs['pk']
        if 'uuid' in kwargs:
            self.uuid = kwargs['uuid']
        return JSONResponseMixin.get(self, request=request, *args,**kwargs)
        # token = self.request.META.get("HTTP_AUTHORIZATION")
        # try:
        #     decode = jwt_decode_handler(token)
        #     user = User.objects.get(username=decode['username'])
        #     return JSONResponseMixin.get(self, request=request, *args,**kwargs)
        # except Exception as e:
        #     response = {'result': 'error',
        #                 'sError': str(e),
        #                 'text': str(e)}
        #     print ("in get datatable", e)
        #     dump = json.dumps(response, cls=LazyEncoder)
        #     return self.render_to_response(dump)
class MixinListRetrive(object):
    lookup_url_kwarg = 'uuid'
    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )        
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        queryset = get_list_or_404(self.queryset, **filter_kwargs)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class ButtonDataTable(object):
    def __call__(self):
        return self.sep.join(self.list_btn)
    def __init__(self, **options):
        self.template = '<a href="{link}" type="button" class="btn btn-{class_css}" title="{title}"><i class="fa fa-{ico}"></i></a>'
        self.template_btn = '<a type="button" class="btn btn-{class_css}" onclick="{fn}" title="{title}"><i class="fa fa-{ico}"></i></a>'
        self.list_btn = []
        self.sep = options.pop('sep','&nbsp') 
    def href(self, link, class_css, ico, title=''):
        self.list_btn.append(self.template.format(link=link,class_css=class_css,ico=ico,title=title))
    def click(self, fn, class_css, ico, title=''):
        self.list_btn.append(self.template_btn.format(fn=fn,class_css=class_css,ico=ico,title=title))
    def __str__(self):
        return self.sep.join(self.list_btn)
================================================

File: models.py
================================================
#import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords
class BaseModelWithoutHistory(models.Model):
    created = models.DateTimeField(auto_now_add = True, editable=True)
    modified = models.DateTimeField(auto_now = True)
    status_field = models.BooleanField(default = True)
    id_data = models.UUIDField(db_index = True,
                               null = True, blank = True,
                               editable = settings.DEBUG)
    class Meta:
        abstract = True
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add = True, editable=True)
    modified = models.DateTimeField(auto_now = True)
    status_field = models.BooleanField(default = True)
    id_data = models.UUIDField(db_index = True,
                               null = True, blank = True,
                               editable = settings.DEBUG)
    history = HistoricalRecords(inherit = True)
    class Meta:
        abstract = True
================================================

File: pagination.py
================================================
from rest_framework import pagination
from rest_framework.response import Response
class LinkHeaderPagination(pagination.PageNumberPagination):
    "http://www.django-rest-framework.org/api-guide/pagination/#header-based-pagination"
    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()
        go_next = None
        go_prev = None
        if next_url is not None and previous_url is not None:
            link = '<{next_url}>; rel="next", <{previous_url}>; rel="prev"'
            go_next = self.page.next_page_number()
            go_prev = self.page.previous_page_number()
        elif next_url is not None:
            link = '<{next_url}>; rel="next"'
            go_next = self.page.next_page_number()
        elif previous_url is not None:
            link = '<{previous_url}>; rel="prev"'
            go_prev = self.page.previous_page_number()
        else:
            link = ''
        link = link.format(next_url=next_url, previous_url=previous_url)
        headers = {'Link': link} if link else {}
        if go_next or go_prev:
            headers['go_prev'] = go_prev if go_prev else 0
            headers['go_next'] = go_next if go_next else 0
        return Response(data, headers=headers)
class LargeResultsSetPagination(LinkHeaderPagination):
    page_size = 1000
================================================

File: serializers.py
================================================
from rest_framework import serializers
class QueryFieldsMixin(object):
    # https://github.com/wimglenn/djangorestframework-queryfields/blob/master/drf_queryfields/mixins.py
    # If using Django filters in the API, these labels mustn't conflict with any model field names.
    include_arg_name = 'fields'
    exclude_arg_name = 'fields!'
    # Split field names by this string.  It doesn't necessarily have to be a single character.
    # Avoid RFC 1738 reserved characters i.e. ';', '/', '?', ':', '@', '=' and '&'
    delimiter = ','
    def __init__(self, *args, **kwargs):
        super(QueryFieldsMixin, self).__init__(*args, **kwargs)
        try:
            request = self.context['request']
            method = request.method
        except (AttributeError, TypeError, KeyError):
            # The serializer was not initialized with request context.
            return
        if method != 'GET':
            return
        try:
            query_params = request.query_params
        except AttributeError:
            # DRF 2
            query_params = getattr(request, 'QUERY_PARAMS', request.GET)
        includes = query_params.getlist(self.include_arg_name)
        include_field_names = {name for names in includes for name in names.split(self.delimiter) if name}
        excludes = query_params.getlist(self.exclude_arg_name)
        exclude_field_names = {name for names in excludes for name in names.split(self.delimiter) if name}
        if not include_field_names and not exclude_field_names:
            # No user fields filtering was requested, we have nothing to do here.
            return
        serializer_field_names = set(self.fields)
        fields_to_drop = serializer_field_names & exclude_field_names
        if include_field_names:
            fields_to_drop |= serializer_field_names - include_field_names
        for field in fields_to_drop:
            self.fields.pop(field)
================================================

File: urls.py
================================================
from django.urls import path, re_path
from rest_framework import routers
from utp.datatables import DatatableUTP, DatatableCPEUTP, DatatablePlan, DatatableProfile, \
							DatatableRadius, DatatableSystemProfile
from dashboard.datatables import DatatableLOG
urlpatterns = [
    path('datatables/utp', DatatableUTP.as_view() , name="datatable_utp"),
    path('datatables/logs/', DatatableLOG.as_view() , name="datatable_logs"),
    re_path(r'^datatables/utp_logs/(?P<uuid>[-\w]+)/$', DatatableLOG.as_view() , name="datatable_utp_logs"),
    re_path(r'^datatables/utp_cpe/(?P<uuid>[-\w]+)/$', DatatableCPEUTP.as_view() , name="datatable_cpe_utp"),
    path('datatables/utp_cpe', DatatableCPEUTP.as_view() , name="datatable_cpeutp_list"),
    path('datatables/planes', DatatablePlan.as_view() , name="datatable_plan"),
    re_path(r'^datatables/profiles/(?P<uuid>[-\w]+)/$', DatatableProfile.as_view() , name="datatable_profile"),
    path('datatables/systemprofiles', DatatableSystemProfile.as_view() , name="datatable_profile"),
    path('datatables/radius', DatatableRadius.as_view() , name="datatable_radius"),
]
================================================

File: utils.py
================================================
from colorama import Fore, Back, Style, init
def timedelta_format(td):
    if td.days > 365:
        year = td.days//365
        days = td.days - (year * 365)
        result = year, days , td.seconds//3600, (td.seconds//60)%60, td.seconds%60
        return "{}a {}d {}h {}m {}s".format(*result)
    else:
        result = td.days, td.seconds//3600, (td.seconds//60)%60, td.seconds%60
        return "{}d {}h {}m {}s".format(*result)
def green(*args):
    init(autoreset=True)
    print(Style.BRIGHT + Fore.GREEN + ' '.join(str(e) for e in args))
def red(*args):
    init(autoreset=True)
    print(Style.BRIGHT + Fore.RED + ' '.join(str(e) for e in args))
def cyan(*args):
    init(autoreset=True)
    print(Style.BRIGHT + Fore.CYAN + ' '.join(str(e) for e in args))
def blue(*args):
    init(autoreset=True)
    print(Style.BRIGHT + Fore.BLUE + ' '.join(str(e) for e in args))
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL 
# print(Fore.RED + 'some red text') 
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
================================================

File: views.py
================================================
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers
from rest_framework.response import Response
class MySchemaGenerator(SchemaGenerator):
    title = 'REST API Index'
    def get_link(self, path, method, view):
        link = super(MySchemaGenerator, self).get_link(path, method, view)
        link._fields += self.get_core_fields(view)
        return link
    def get_core_fields(self, view):
        if hasattr(view, "get_core_fields"):
            return getattr(view, 'get_core_fields')(coreapi, coreschema)
        return ()
class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True
    permission_classes = [AllowAny]
    renderer_classes = [
        CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    def get(self, request):
        generator = MySchemaGenerator(
            title="Sentinel API",
            # url=url,
            # patterns=patterns,
            # urlconf=urlconf
        )
        schema = generator.get_schema(request=request)
        if not schema:
            raise exceptions.ValidationError(
                'The schema generator did not return a schema Document'
            )
        return Response(schema)   
================================================

File: celery.py
================================================
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
app = Celery('sentinel')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    print('Request id: {0!r}'.format(self.request.id))
================================================

File: base_sentinel.py
================================================
"""
Django settings for sentinel project.
Generated by 'django-admin startproject' using Django 2.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path
from datetime import timedelta, datetime
from os.path import dirname, abspath, join
from dotenv import load_dotenv
from . import get_env_variable
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
BASE_DIR_LOG = join(dirname(BASE_DIR), 'logs')
SECRET_KEY = get_env_variable('SECRET_KEY')
DEBUG = False
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_jwt',
    'rest_framework_swagger',    
    'common',
    'utp',
    'celery',
    'corsheaders',
    'dynamic_preferences',
    'dynamic_preferences.users.apps.UserPreferencesConfig',
    'import_export',    
    'dashboard',  
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'config.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',#  IsAuthenticated
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.LinkHeaderPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'NUM_PROXIES': 2,
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '700/hour'
    },
    #token
    'JWT_EXPIRATION_DELTA': timedelta(hours=48),
    "JWT_ALLOW_REFRESH": True,
}
AUTHENTICATION_BACKENDS = (
    'common.backends.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
)
SITE_NAME = "sentinel"
CSRF_COOKIE_NAME = 'csrftoken_' + SITE_NAME
SESSION_COOKIE_NAME = 'scn_' + SITE_NAME
NAME_JWT = 'tok_' + SITE_NAME
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'USE_SESSION_AUTH': False
}
ADMINS = [('Jovan', 'jovan.pacheco@optic.cl')]
MANAGERS = ADMINS
now_log = "{0.year}-{0.month}-{0.day}-{0.hour}".format(datetime.now()) 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-.3s %(asctime)s %(module)s %(name)s %(message)s \n\n'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            #'filename': join(BASE_DIR_LOG, 'debug_django_%s.log' % str(now_log)),
            'filename': join(BASE_DIR_LOG, 'debug_django.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'rotating' : {
        #     'level' : 'INFO',
        #     'class' : 'logging.handlers.RotatingFileHandler',
        #     'filename' : join(BASE_DIR_LOG, 'django_rotating.log'),
        #     'maxBytes' : 1024*1024*1, # 1MB
        #     'backupCount' : 10,
        #     'formatter' : 'verbose',
        # },        
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file','console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
SENTINEL_VERSION = '0.3.1'
DYNAMIC_PREFERENCES = {
    # a python attribute that will be added to model instances with preferences
    # override this if the default collide with one of your models attributes/fields
    'MANAGER_ATTRIBUTE': 'preferences',
    # The python module in which registered preferences will be searched within each app
    'REGISTRY_MODULE': 'preferences',
    # Allow quick editing of preferences directly in admin list view
    # WARNING: enabling this feature can cause data corruption if multiple users
    # use the same list view at the same time, see https://code.djangoproject.com/ticket/11313
    'ADMIN_ENABLE_CHANGELIST_FORM': True,
    # Customize how you can access preferences from managers. The default is to
    # separate sections and keys with two underscores. This is probably not a settings you'll
    # want to change, but it's here just in case
    'SECTION_KEY_SEPARATOR': '__',
    # Use this to disable caching of preference. This can be useful to debug things
    'ENABLE_CACHE': True,
    # Use this to disable checking preferences names. This can be useful to debug things
    'VALIDATE_NAMES': True,
}
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://190.113.247.215",
    "http://190.113.247.219",
    "http://sentinel.devel7.cl",
    "https://sentinel.devel7.cl",
    "http://sentinel7.cl",
    "https://sentinel7.cl",    
]
sentry_sdk.init(
    dsn=get_env_variable('DSN'),
    integrations=[DjangoIntegration()]
)
================================================

File: __init__.py
================================================
import os
from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]
    except KeyError:
        return default
def get_env_variable_required(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
================================================

File: urls.py
================================================
"""sentinel URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from common.views import SwaggerSchemaView
from common.urls import urlpatterns as router_common
from utp.urls import router as router_utp
from utp.views import updateCpeUtp, updateProfile
from dashboard.urls import router as router_dashboard
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/(?P<version>[-\w]+)/', include(router_utp.urls)), 
    re_path(r'^api/(?P<version>[-\w]+)/', include(router_dashboard.urls)),  
    re_path(r'^api/(?P<version>[-\w]+)/update_list_cpe', updateCpeUtp),
    re_path(r'^api/(?P<version>[-\w]+)/update_list_radiusprofile', updateProfile),
    path('api/docs', SwaggerSchemaView.as_view()),
    path('', include(router_common)),   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    import sys
    if "debug_toolbar" in sys.modules:
        import debug_toolbar
        urlpatterns = [
                          path('__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
================================================

File: wsgi.py
================================================
"""
WSGI config for config project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
================================================

File: __init__.py
================================================
from .celery import app as celery_app
__all__ = ['celery_app']
================================================

File: actions.py
================================================
ADD_ACTION = 1
CHANGE_ACTION = 2
FIND_AUTOFIND_ACTION = 3
DELETE_ACTION = 4
COUNTERS_UPDATE_ACTION = 5
SHELL_ACTION = 6
GET_ACTION = 7
ACTION_CHOICES = (
    (ADD_ACTION,'ADD_ACTION'),
    (CHANGE_ACTION,'CHANGE_ACTION'),
    (FIND_AUTOFIND_ACTION,'FIND_AUTOFIND_ACTION'),
    (DELETE_ACTION,'DELETE_ACTION'),
    (COUNTERS_UPDATE_ACTION,'COUNTERS_UPDATE'),
    (SHELL_ACTION,'SHELL_ACTION'),
    (GET_ACTION,'GET_ACTION')
)
LEVEL_CHOICES = (
	(50,'CRITICAL'),
	(40,'ERROR'),
	(30,'WARNING'),
	(20,'INFO'),
	(10,'DEBUG'),
	(0,'NOTSET'),
)
================================================

File: admin.py
================================================
from django.contrib import admin
from common.admin import BaseAdmin
from .models import TaskModel, LogSentinel, TypeAction, Entity
# @admin.register(Node)
# class NodeAdmin(BaseAdmin):
#     list_display = ('name', 'address', 'community', 'devices','devices_cpes')
#     list_editable = ('devices','devices_cpes')
# @admin.register(Feedback)
# class FeedbackAdmin(BaseAdmin):
#     list_display = ('platform', 'user_agent', 'commentary', )
#     list_filter = ('platform',) 
#     search_fields = ['platform', 'user_agent', 'commentary']
@admin.register(LogSentinel)
class LogSentineladmin(BaseAdmin):
    list_display = ('created', 'action', 'by_representation',
                    'entity_representation','id_value','description','level')
    list_filter = ('action','id_value','entity','id_data')
@admin.register(TaskModel)
class TaskModelAdmin(BaseAdmin):
    list_display = ('name', 'id_obj', 'model_obj','status','time','transcurrido')
    list_filter = ('model_obj','status')
    def time(self, obj):
        try:
            return obj.date_done - obj.created
        except Exception as e:
            return None
    def transcurrido(self, obj):
        from django.utils import timezone
        return timezone.now() - obj.created 
@admin.register(TypeAction)
class TypeActionAdmin(BaseAdmin):
    list_display = ('created', 'type_action',)
@admin.register(Entity)
class EntityAdmin(BaseAdmin):
    list_display = ('created', 'entity',)
# @admin.register(Variable)
# class VariableAdmin(BaseAdmin):
#     list_display = ('nombre','valor','namespace')
#     list_filter = ('namespace',)
================================================

File: apps.py
================================================
from django.apps import AppConfig
class DashboardConfig(AppConfig):
    name = 'dashboard'
================================================

File: datatables.py
================================================
from django.db.models import Q
from common.mixins import DataTable
from .models import LogSentinel
# class DatatableNode(DataTable):
#     model = Node
#     columns = ['name','address','community','devices','devices_cpes']
#     order_columns = columns
#     max_display_length = 1000
#     def filter_queryset(self, qs):
#         search = self.request.POST.get(u'search[value]', None)
#         if search:
#             qs = self.model.objects.filter(
#                 Q(name__icontains=search) |
#                 Q(address__icontains=search)
#             )
#         return qs
class DatatableLOG(DataTable):
    model = LogSentinel
    columns = ['created', 'by_representation', 'entity', 'entity_representation',
               'id_value', 'action', 'description']
    order_columns = columns
    max_display_length = 1000
    def display_created(self, obj):
        return obj.created.strftime("%d-%m-%Y %H:%M:%S")
    def get_initial_queryset(self):
        try:
            #qs = self.model.objects.none()
            # get_onu = False
            # get_olt = False
            # get_port = False
            # get_vlans = False
            # get_interfaces = False
            # filter_type_log = self._querydict.get('filter_type_log', None)
            # filter_type_action = self._querydict.get('filter_type_action', None)            
            # if filter_type_action:
            #     try:
            #         int(filter_type_action)
            #     except Exception as e:
            #         filter_type_action = None
            # if filter_type_log:
            #     if filter_type_log == 'ONU':
            #         get_onu = True
            #     elif filter_type_log == 'INTERFACE':
            #         get_interfaces = True
            #     elif filter_type_log == 'PORTOLT':
            #         get_port = True
            #     elif filter_type_log == 'OLTVLAN':
            #         get_vlans = True
            #     elif filter_type_log == 'OLT':
            #         get_olt = True                    
            #     elif filter_type_log == 'Tipo':
            #         get_onu = True
            #         get_port = True
            #         get_vlans = True
            #         get_interfaces = True
            #         get_olt = True
            # else:
            #     get_onu = True
            #     get_port = True
            #     get_vlans = True
            #     get_interfaces = True
            #     get_olt = True
            qs = self.model.objects.filter(id_value='none_field')
            #if get_olt and filter_type_action:
            #    qs =  self.model.objects.filter(id_value=self.uuid,action__type_action=filter_type_action)
            #elif get_olt:
            qs = self.model.objects.filter(id_value=self.uuid)
            nqs = None
            # if filter_type_action is None and filter_type_log == 'Tipo':
            #     print ('adfgfdd')
            #     return self.model.objects.filter()
            # if get_olt:
            #     nqs = self.model.objects.filter(
            #             Q(id_value=self.pk, id_field='id')
            #     )
            # if get_onu:
            #     from devices.models import ONU
            #     pks = ONU.objects.filter(status_field=True,olt__uuid=self.uuid).values_list('id', flat=True)
            #     nqs = self.model.objects.filter(
            #             Q(id_value__in=list(pks), entity__entity='ONU')#id_field='id', 
            #          )
            # if get_port:
            #     from devices.models import PortOLT
            #     pks = PortOLT.objects.filter(status_field=True, interface__olt__uuid=self.uuid).values_list('id', flat=True)
            #     nqs = self.model.objects.filter(
            #             Q(id_value__in=list(pks), entity__entity='PORTOLT')#id_field='id', 
            #          )
            # if get_vlans:
            #     from devices.models import OLTVLAN
            #     pks = OLTVLAN.objects.filter(status_field=True, olt__uuid=self.uuid).values_list('id', flat=True)
            #     nqs = self.model.objects.filter(
            #             Q(id_value__in=list(pks), entity__entity='OLTVLAN')#id_field='id', 
            #          )
            # if get_interfaces:
            #     from devices.models import InterfaceOLT
            #     pks = InterfaceOLT.objects.filter(status_field=True, olt__uuid=self.uuid).values_list('id', flat=True)
            #     nqs = self.model.objects.filter(
            #             Q(id_value__in=list(pks), entity__entity='INTERFACE')#id_field='id', 
            #          )
            # if nqs and filter_type_action:
            #     nqs = nqs.filter(action__type_action=filter_type_action)
            #     #
            # try:
            #     qs = qs | nqs
            # except Exception as e:
            #     pass
            return qs
        except Exception as e:
            print (e)
            qs = self.model.objects.filter(status_field=True)
            return qs 
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = qs.filter(
                Q(description__icontains=search) |
                Q(entity_representation__icontains=search)
            )
        #qs = self.get_initial_queryset()
        return qs
================================================

File: 0001_initial.py
================================================
# Generated by Django 2.1.3 on 2019-07-08 16:13
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalTaskModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=180)),
                ('id_obj', models.PositiveIntegerField(default=0)),
                ('model_obj', models.CharField(max_length=180)),
                ('status', models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50, verbose_name='state')),
                ('result', models.BooleanField(default=False)),
                ('date_done', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='done at')),
                ('traceback', models.TextField(blank=True, null=True, verbose_name='traceback')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=180)),
                ('id_obj', models.PositiveIntegerField(default=0)),
                ('model_obj', models.CharField(max_length=180)),
                ('status', models.CharField(choices=[('FAILURE', 'FAILURE'), ('PENDING', 'PENDING'), ('RECEIVED', 'RECEIVED'), ('RETRY', 'RETRY'), ('REVOKED', 'REVOKED'), ('STARTED', 'STARTED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=50, verbose_name='state')),
                ('result', models.BooleanField(default=False)),
                ('date_done', models.DateTimeField(auto_now=True, null=True, verbose_name='done at')),
                ('traceback', models.TextField(blank=True, null=True, verbose_name='traceback')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
================================================

File: 0002_auto_20190709_1400.py
================================================
# Generated by Django 2.1.3 on 2019-07-09 14:00
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('entity', models.CharField(max_length=35)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LogSentinel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('by_representation', models.CharField(max_length=135)),
                ('entity_representation', models.CharField(max_length=135)),
                ('id_field', models.CharField(default='id', max_length=135)),
                ('id_value', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('level', models.PositiveIntegerField(choices=[(50, 'CRITICAL'), (40, 'ERROR'), (30, 'WARNING'), (20, 'INFO'), (10, 'DEBUG'), (0, 'NOTSET')], default=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('type_action', models.PositiveIntegerField(choices=[(1, 'ADD_ACTION'), (2, 'CHANGE_ACTION'), (3, 'FIND_AUTOFIND_ACTION'), (4, 'DELETE_ACTION'), (5, 'COUNTERS_UPDATE'), (6, 'SHELL_ACTION'), (7, 'GET_ACTION')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='logsentinel',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.TypeAction'),
        ),
        migrations.AddField(
            model_name='logsentinel',
            name='by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logsentinel',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Entity'),
        ),
    ]
================================================

File: 0003_variable.py
================================================
# Generated by Django 2.1.3 on 2019-08-21 21:18
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0002_auto_20190709_1400'),
    ]
    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=135)),
                ('valor', models.TextField()),
                ('namespace', models.CharField(max_length=135)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
================================================

File: models.py
================================================
# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
from common.models import BaseModel, BaseModelWithoutHistory
from celery import states
from .actions import ACTION_CHOICES, LEVEL_CHOICES
ALL_STATES = sorted(states.ALL_STATES)
TASK_STATE_CHOICES = sorted(zip(ALL_STATES, ALL_STATES))
class TaskModel(BaseModel):
    uuid = models.UUIDField(db_index=True,
                            default=uuid.uuid4,
                            editable=settings.DEBUG)    
    name = models.CharField(max_length=180)
    id_obj = models.PositiveIntegerField(default=0)
    model_obj = models.CharField(max_length=180)
    status = models.CharField(_('state'), max_length=50,
                              default=states.PENDING, choices=TASK_STATE_CHOICES)
    result = models.BooleanField(default=False)
    date_done = models.DateTimeField(_('done at'), blank=True, null=True,
                                     auto_now=True)
    traceback = models.TextField(_('traceback'), blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["id"]
class TypeAction(BaseModelWithoutHistory):
    type_action = models.PositiveIntegerField(default=0, choices=ACTION_CHOICES)
    def __str__(self):
        return ACTION_CHOICES[self.type_action-1][1]
        return str(self.type_action)
class Entity(BaseModelWithoutHistory):
    entity = models.CharField(max_length=35) 
    def __str__(self):
        return self.entity
class LogSentinel(BaseModelWithoutHistory):
    action = models.ForeignKey(TypeAction, on_delete=models.DO_NOTHING)
    by = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.DO_NOTHING,
                            null=True, blank=True)
    by_representation = models.CharField(max_length=135) 
    entity = models.ForeignKey(Entity,on_delete=models.DO_NOTHING)
    entity_representation = models.CharField(max_length=135)
    id_field = models.CharField(max_length=135, default='id')
    id_value = models.CharField(max_length=80)
    description = models.TextField()
    level = models.PositiveIntegerField(default=20, choices=LEVEL_CHOICES)
    def __str__(self):
        return ('%s - %s') % (self.entity_representation, self.description)
    class Meta:
        ordering = ["id"]
class Variable(models.Model):
    """ Para utilizar en simulaciones y algunas configuraciones"""
    created = models.DateTimeField(auto_now_add = True)
    nombre = models.CharField(max_length=135)
    valor = models.TextField()
    namespace = models.CharField(max_length=135)
    active = models.BooleanField(default = True)
================================================

File: serializers.py
================================================
from rest_framework.serializers import Serializer
from dashboard.models import LogSentinel
__all__ = ['LogSerializer']
class LogSerializer(Serializer):
    class Meta:
        model = LogSentinel
        fields = ('id', 'action','by','by_representation','entity',
                    'entity_representation','id_field','id_value',
                    'description','level')
================================================

File: simulate.py
================================================
import json
from common import Attrs
from dashboard.models import Variable
class Simulate(object):
	def __init__(self, namespace, nombre, ajax=False):
		self.namespace = namespace
		self.nombre = nombre
		self.response = False
		self.ajax = ajax
	def __enter__(self):
		v = Variable.objects.filter(nombre=self.nombre,
									namespace=self.namespace,
									active=True)
		if v.exists():
			try:
				values = json.loads(v[0].valor)
				if self.ajax:
					self.response = values
				else:
					self.response = Attrs(**values)
			except Exception as e:
				print (e)
		return self
	def __exit__(self, *args):
		del self.response
================================================

File: tests.py
================================================
from django.test import TestCase
# Create your tests here.
================================================

File: urls.py
================================================
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'log', LogViewSet, 'log_api')
================================================

File: utils.py
================================================
import os
import requests
from django.conf import settings
from ua_parser.user_agent_parser import Parse
from dynamic_preferences.registries import global_preferences_registry
from .models import LogSentinel, Entity, TypeAction
from dashboard.actions import *
global_preferences = global_preferences_registry.manager()
class LOG(object):
    model = LogSentinel
    _ent = None
    _method = None
    def __getattr__(self, attr):
        name = attr.upper()
        actions = ['ADD','CHANGE','FIND_AUTOFIND','DELETE',
                  'DEL','ERASE','SUP','COUNTERS_UPDATE','SHELL']
        if name in actions:
            self._method = name
            return self
        self._ent = name
        return self
    def get_action_method(self):
        r = None
        if self._method == 'ADD':
            r = ADD_ACTION
        if self._method == 'CHANGE':
            r = CHANGE_ACTION
        if self._method == 'FIND_AUTOFIND':
            r = FIND_AUTOFIND_ACTION
        if self._method in ['DELETE','DEL','ERASE','SUP']:
            r = DELETE_ACTION
        if self._method == 'COUNTERS_UPDATE':
            r = COUNTERS_UPDATE_ACTION
        if self._method == 'SHELL':
            r = SHELL_ACTION
        if self._method == 'GET':
            r = GET_ACTION
        print ('RRRRRRRRRR',r)
        return r
    def __call__(self, *args, **values):
        if len(args) == 1:
            return self.save_args(*args, **values)
        action = self.get_action_method()
        if action:
            return self.save_log(action, **values)
        print ('me estan llamando sin funcion',values,self._method, self._ent)
    def save_args(self, *args, **values):
        data_local = dict(args[0])
        data_send = {}
        action = self.get_action_method()
        if action:
            data_send['id_data']=data_local.get('_id_data', None)
            if 'obj_to_log' in data_local:
                data_send['by_representation'] = data_local['obj_to_log']['by_representation']
            if SHELL_ACTION == action:
                if 'e' in data_local:
                    sms = f'No se pudo conectar -> {data_local["e"]}'
                    data_send['level'] = 30
                else:
                    sms = 'Nueva conexión'
                data_send['description']=sms
                data_send['id_value']=data_local.get('olt').uuid
                data_send['entity_representation']=repr(data_local.get('olt'))
                return self.save_log(SHELL_ACTION,**data_send)
            if ADD_ACTION == action:
                data_send['description']='Añadido con exito'
                if self._ent == 'INTERFACE':
                    data_send['entity_representation']=repr(data_local.get('interface'))
                    data_send['id_value']=data_local.get('interface').id
                return self.save_log(SHELL_ACTION,**data_send)
    def save_log(self, action_method, **values):
        print ('save_log',action_method,values)
        if self._ent != 'OLT':
            #exit()
            pass
        entity, c = Entity.objects.get_or_create(entity=self._ent)
        action, c = TypeAction.objects.get_or_create(type_action = values.get('action', action_method))
        entity_representation = values.get('entity_representation',str(entity))
        by = values.get('by', None)
        by_representation = values.get('by_representation')
        id_field = values.get('id_field', None)
        id_value = values.get('id_value', None)
        description = values.get('description')
        id_data = values.get('id_data', None)
        level = values.get('level',None)
        data = {
            'by_representation':by_representation,
            'action':action,
            'entity_representation':entity_representation,
            'entity':entity,
            'description':description,
            'id_data':id_data
        }
        if id_value:
            data['id_value'] = id_value
        if id_field:
            data['id_field'] = id_field
        if level:
            data['level'] = level
        if by:
            data['by'] = by
        self.model.objects.create(**data)
        return True
================================================

File: views.py
================================================
from rest_framework import viewsets, mixins
from dashboard.models import LogSentinel
from dashboard.serializers import *
class LogViewSet(viewsets.ModelViewSet):
    queryset = LogSentinel.objects.all()
    serializer_class = LogSerializer
================================================

File: manage.py
================================================
#!/usr/bin/env python
import os
import sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8080"
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
================================================

File: admin.py
================================================
from django.contrib import admin, messages
from common.admin import BaseAdmin
from .models import Mikrotik, ModelDevice, CpeUtp, Operator, ProfileUTP,\
    TypePLAN,Plan, Radius, SystemProfile
from dynamic_preferences.registries import global_preferences_registry
global_preferences = global_preferences_registry.manager()
@admin.register(Mikrotik)
class MikrotikAdmin(BaseAdmin):
    list_display = ('ip','alias','model', 'description',
    	 			'cpeutps','cpeutp_active','uptime')
@admin.register(ModelDevice)
class ModelDeviceAdmin(BaseAdmin):
    list_display = ('model',)
@admin.register(CpeUtp)
class CpeUtpAdmin(BaseAdmin):
    list_display = ('ip','alias','model', 'description','uptime')
    list_filter = ('nodo_utp','model') 
@admin.register(Operator)
class OperatorAdmin(BaseAdmin):
    list_display = ('name','code')
@admin.register(SystemProfile)
class SystemProfileAdmin(BaseAdmin):
    list_display = ('name','download_speed','upload_speed','provisioning_available',
                    'limitation_name','description')
@admin.register(ProfileUTP)
class ProfileUTPdmin(BaseAdmin):
    list_display = ('name','download_speed','upload_speed','provisioning_available',
                    'limitation_name','description')
@admin.register(TypePLAN)
class TypePLANAdmin(BaseAdmin):
    list_display = ('name',)
@admin.register(Plan)
class PlanAdmin(BaseAdmin):
    list_display = ('name','operator','profile_name','matrix_plan',)
    list_filter = ('type_plan',)  
@admin.register(Radius)
class RadiusAdmin(BaseAdmin):
    list_display = ('ip','alias','model', 'description','uptime','status')
================================================

File: apps.py
================================================
from django.apps import AppConfig
class UtpConfig(AppConfig):
    name = 'utp'
================================================

File: datatables.py
================================================
import datetime 
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.db.models import Q#, Value, Sum, F
#from django.db.models.functions import Concat
#from django.db.models.fields import IntegerField
from common.utils import timedelta_format
from common.mixins import DataTable, ButtonDataTable
#from dashboard.models import TaskModel
from utp.models import Mikrotik, CpeUtp, Plan, SystemProfile,ProfileUTP, Radius
from dynamic_preferences.registries import global_preferences_registry
global_preferences = global_preferences_registry.manager()
class DatatableUTP(DataTable):
    model = Mikrotik
    id_current = 0
    columns = ['id','alias','ip','cpeutps','uptime','model.model','description','radius','botones']#]
    order_columns = ['id','alias','ip','cpeutps','uptime','model.model','description','radius']
    max_display_length = 1000
    def display_id(self, obj):
        self.id_current += 1
        return f'<a href="#/devices/utp/{obj.uuid}/" data-toggle="ajax">{self.id_current}</a>'     
    def display_alias(self, obj):
        return f'<a href="#/devices/utp/{obj.uuid}/" data-toggle="ajax">{obj.alias}</a>'       
    def btn_delete(self, row):
        t = """<a type="button" class="btn btn-danger" onclick="{fn}">
        <img style="width:18px;" src="/static/img/papelera.png"></a>"""
        return t.format(fn="delete_utp('%s')" % str(row.uuid))
    def render_column(self, row, column):
        if column == 'botones':
            btn = ButtonDataTable()
            btn.list_btn.append(self.btn_delete(row))
            return btn()
        else:
            return super().render_column(row, column)
    def display_uptime(self, obj):
        display = '<i class="fas fa-circle" style="color: green;"></i> '
        if obj.uptime:
            u = timezone.now() - obj.uptime
            display += timedelta_format(u)
        elif obj.get_uptime():
            u = timezone.now() - obj.get_uptime()
            display += timedelta_format(u)
        return display 
        diff = relativedelta(obj.time_uptime , timezone.now())
        diff = '%sd, %sh, %sm, %ss' % (diff.days, diff.hours, diff.minutes, diff.seconds)
        diff = diff.replace('-','')
        return '<i class="fas fa-circle" style="color: red;"></i> conexión pérdida hace ' + str(diff)
    def display_cpeutps(self, obj):
        return '%s/%d' % (obj.cpeutp_active, obj.cpeutps)
    def display_radius(self,obj):
        print(obj.radius)
        try:
            return obj.radius.alias
        except:
            return ""
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(alias__icontains=search) |
                Q(ip__icontains=search) |
                Q(description__icontains=search) |
                Q(model__model__icontains=search)
            )
        return qs
class DatatableCPEUTP(DataTable):
    model = CpeUtp
    id_current = 0
    columns = ['id','service_number', 'status', 'uptime', 'model.brand','model.model',
              'description','mac','ip','firmware']
    order_columns = columns
    max_display_length = 1000
    html_panel = '<a data-click="panel-lateral" data-id="%s" data-panel="panel_utpcpe_content">%s</a>'
    tempuuid = ""
    def display_id(self, obj):
        self.id_current += 1
        self.tempuuid = obj.uuid
        return self.html_panel % (obj.uuid,self.id_current)
    def display_service_number(self,obj):
        if obj.service_number == None:
            return ""
        else:
            return self.html_panel % (obj.uuid,obj.service_number)
    def display_firmware(self,obj):
        if obj.firmware == None:
            return ""
        else:
            return self.html_panel % (obj.uuid, obj.firmware)
    def get_initial_queryset(self):
        try:
            #Corregido error que se traía todo los cpe: utp -> nodo_utp
            qs = self.model.objects.filter(status_field=True,
                                           nodo_utp__uuid=self.uuid)
        except:
            qs = self.model.objects.filter(status_field=True)
        filter_status = self._querydict.get('filter_status', None)
        filter_model = self._querydict.get('filter_model', None)
        filter_utp = self._querydict.get('filter_utp', None)
        if filter_status and filter_status == 'ONLINE':
            qs = qs.filter(status=True)
        if filter_status and filter_status == 'OFFLINE':
            qs = qs.filter(status=False)
        if filter_model and filter_model !='Modelo':
            qs = qs.filter(model__pk=filter_model)
        if filter_utp and filter_utp != '0':
            try:
                #Corregido error que se traía todo los cpe: utp -> nodo_utp
                qs = qs.filter(nodo_utp__uuid=filter_utp)
            except Exception as e:
                pass
        return qs
    def display_uptime(self, obj):
        try:
            if obj.status:
                u = timezone.now() - obj.uptime
                return self.html_panel % (obj.uuid, timedelta_format(u))
            return None
        except Exception as e:
            return None
    def display_RX(self, obj):
        click_template = 'data-click="panel-lateral" data-id="{id}" data-panel="panel_utpcpe_content"'
        bar_template = """<div {click} class="progress" style="height: 10px; width:51%;">
        <div onclick="openPanel('{id}');panel_utpcpe_content('#panel_right_content','{id}');" class="progress-bar {color}" style="width: {percent}%;"></div>
        </div><div {click} style="float: right; position:relative; top: -13px;">
        &nbsp;{signal}</div>"""
        signal = float(obj.RX) if obj.RX else ''
        percent = 0
        color_bar = ''
        if signal != '':
            if (signal > -10):
                html = """<div style="color:red;" data-click="panel-lateral" data-id="{}" 
                data-panel="panel_utpcpe_content">Sobrecarga {}</div>"""
                return html.format(obj.uuid,str(signal) + ' dBm')
            elif signal == -10:
                color_bar = 'bg-lime'
                percent = 100
            elif (signal < -10) & (signal >= -18.9):
                percent = 75
                color_bar = 'bg-green-transparent-8'
            elif (signal < -18.9) & (signal >= -22) :
                color_bar = 'bg-green-transparent-8 '
                percent = 55
            elif (signal < -22) & (signal >= -24.9):
                color_bar = 'bg-red-transparent-8 '
                percent = 35
            else:
                color_bar = 'bg-red'
                percent = 5
        return bar_template.format(click=click_template.format(id=obj.uuid),
                                   id=obj.uuid, color=color_bar, percent=percent,
                                   signal=str(signal) + ' dBm')
    def display_brand(self,obj):
        try:
            #return obj.brand
            bd = obj.brand
            return self.html_panel % (self.tempuuid, bd)
        except:
            return ""
    def display_model(self,obj):
        try:
            #return obj.model
            md = obj.model
            return self.html_panel % (self.tempuuid, md)
        except:
            return ""
    def display_description(self, obj):
        return  self.html_panel % (obj.uuid, obj.description)
    def display_ip(self, obj):
        if obj.active_ip != "" and obj.active_ip != None:
            if obj.ip == obj.active_ip:
                return '<p style="color: green;">{}</p>'.format(self.html_panel % (obj.uuid, obj.active_ip))
            else:
                return '<p style="color: red;">{}</p>'.format(self.html_panel % (obj.uuid, obj.active_ip))
        return '<p style="color: red;">{}</p>'.format(self.html_panel % (obj.uuid, obj.ip))
    def display_service_number(self, obj):
        return  self.html_panel % (obj.uuid, obj.service_number)
    def display_mac(self, obj):
        if obj.active_mac != "" and obj.active_mac != None:
            if obj.mac == obj.active_mac:
                return '<p style="color: green;">{}</p>'.format(self.html_panel % (obj.uuid, obj.active_mac))
            else:
                return '<p style="color: red;">{}</p>'.format(self.html_panel % (obj.uuid, obj.active_mac))
        return '<p style="color: red;">{}</p>'.format(self.html_panel % (obj.uuid, obj.mac))
    def display_status(self, obj):
        if obj.status:
            string = '<i class="fas fa-circle" style="color: green;"></i>'
            return self.html_panel % (obj.uuid, string)
        string = '<i class="fas fa-circle" style="color: red;"></i>'    
        return self.html_panel % (obj.uuid, string)
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(ip__icontains=search) |
                Q(description__icontains=search) |
                Q(model__model__icontains=search) |
                Q(mac__icontains=search.replace(':',''))
            )
        filter_status = self._querydict.get('filter_status', None)
        filter_model = self._querydict.get('filter_model', None)
        if filter_status and filter_status == 'ONLINE':
            qs = qs.filter(status=True)
        if filter_status and filter_status == 'OFFLINE':
            qs = qs.filter(status=False)
        if filter_model and filter_model !='Modelo':
            qs = qs.filter(model__pk=filter_model)
        return qs
class DatatableSystemProfile(DataTable):
    model = SystemProfile
    id_current = 0
    columns = ['id','name','limitation_name','download_speed','upload_speed',
                'provisioning_available','description','botones']
    order_columns = ['id','name','limitation_name','download_speed','upload_speed',
                'provisioning_available','description']
    max_display_length = 1000
    def render_column(self, row, column):
        if column == 'botones':
            btn = ButtonDataTable()
            m = '<i data-placement="right" data-toggle="tooltip" title="Editar Disponible Provisión" data-html="true"><a type="button" class="btn btn-light" onclick="{fn}"><i class="fas fa-exchange-alt"></i></a></i>'
            #<img style="width:18px;" src="/static/img/papelera.png">
            if row.name:
                name=row.name
            else:
                name=""
            btn.list_btn.append(
                m.format(fn="speedUtpProvisioning(%d,'%s')" % (row.id, name))
            )
            btn.click("deleteSpeed(%d,'%s')" % (row.id,str(name)) , 'danger', 'recycle')
            return btn()
        else:
           return super().render_column(row, column)
    def display_id(self, obj):
        self.id_current += 1
        return self.id_current
    def display_provisioning_available(self, obj):
        if obj.provisioning_available:
            return '<p style="color: green;">Si</p>'
        return '<p style="color: red;">No</p>'
    def display_upload_speed(self, obj):
        if obj.upload_speed:
            return "%d Mbps" % obj.upload_speed
        return ''
    def display_download_speed(self, obj):
        if obj.download_speed:
            return "%d Mbps" % obj.download_speed
        return ''
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(name__icontains = search) |
                Q(cir__icontains = search)
            )
        return qs
class DatatableProfile(DataTable):
    model = ProfileUTP
    id_current = 0
    columns = ['id','name','limitation_name','download_speed','upload_speed',
                'provisioning_available','description','system_profile','botones']
    order_columns = ['id','name','limitation_name','download_speed','upload_speed',
                'provisioning_available','description','system_profile']
    max_display_length = 1000
    def render_column(self, row, column):
        if column == 'botones':
            btn = ButtonDataTable()
            t = '<i data-placement="right" data-toggle="tooltip" title="Cambiar System Profile" data-html="true"><a type="button" class="btn btn-info" onclick="{fn}"><i class="fas fa-exchange-alt"></i></a></i>'
            m = '<i data-placement="right" data-toggle="tooltip" title="Editar Disponible Provisión" data-html="true"><a type="button" class="btn btn-light" onclick="{fn}"><i class="fas fa-exchange-alt"></i></a></i>'
            #<img style="width:18px;" src="/static/img/papelera.png">
            speeds_system = row.system_profile.id if row.system_profile else 0
            if row.name:
                name=row.name
            else:
                name=""
            btn.list_btn.append(
                m.format(fn="speedUtpProvisioning(%d,'%s')" % (row.id, name))
            )
            btn.list_btn.append(
                t.format(fn="speedUtpSystem(%d,%d,'%s')" % (row.id, speeds_system, name))
            )
            btn.click("deleteSpeed(%d,'%s')" % (row.id,str(name)) , 'danger', 'recycle')
            return btn()
        else:
           return super().render_column(row, column)
    def display_id(self, obj):
        self.id_current += 1
        return self.id_current
    def display_system_profile(self,obj):
        if obj.system_profile:
            return obj.system_profile.name
        else:
            return ""
    def display_provisioning_available(self, obj):
        if obj.provisioning_available:
            return '<p style="color: green;">Si</p>'
        return '<p style="color: red;">No</p>'
    def display_upload_speed(self, obj):
        if obj.upload_speed:
            return "%d Mbps" % obj.upload_speed
        return ''
    def display_download_speed(self, obj):
        if obj.download_speed:
            return "%d Mbps" % obj.download_speed
        return ''
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(name__icontains = search) |
                Q(cir__icontains = search)
            )
        return qs
class DatatablePlan(DataTable):
    model = Plan 
    columns = ['id', 'operator','name','type_plan','profile_name.download_speed','profile_name.upload_speed',
                'aggregation_rate','profile_name','matrix_plan','botones']
    order_columns = columns
    max_display_length = 1000
    def display_profile_name(self,obj):
        if obj.profile_name.name:
            return obj.profile_name.name
        return ''
    def display_aggregation_rate(self, obj):
        if obj.aggregation_rate:
            return "1:%d" % obj.aggregation_rate
        return ''
    def display_upload_speed(self, obj):
        if obj.upload_speed:
            return "%d Mbps" % obj.upload_speed
        return ''
    def display_download_speed(self, obj):
        if obj.download_speed:
            return "%d Mbps" % obj.download_speed
        return ''
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(name__icontains = search) |
                Q(type_plan__name__icontains = search)
            )
        return qs
    def render_column(self, row, column):
        if column == 'botones':
            btn = ButtonDataTable()
            btn.click("editPlan('%s')" % str(row.id) , 'info', 'edit')
            #return btn()
            return ""
        else:
            return super().render_column(row, column)
class DatatableRadius(DataTable):
    model = Radius
    id_current = 0
    columns = ['id','alias','ip','uptime','model.model','description','botones']#]
    order_columns = ['id','alias','ip','uptime','model.model','description']
    max_display_length = 1000
    def display_id(self, obj):
        self.id_current += 1
        return f'<a href="#/devices/utp/radius/{obj.uuid}/" data-toggle="ajax">{self.id_current}</a>'     
        #return self.id_current
    def display_alias(self, obj):
        return f'<a href="#/devices/utp/radius/{obj.uuid}/" data-toggle="ajax">{obj.alias}</a>'   
        #return obj.alias
    def display_model(self,obj):
        try:
            return obj.model
        except:
            return ""  
    def btn_delete(self, row):
        t = """<a type="button" class="btn btn-danger" onclick="{fn}">
        <img style="width:18px;" src="/static/img/papelera.png"></a>"""
        return t.format(fn="delete_utpradius('%s')" % str(row.uuid))
    def render_column(self, row, column):
        if column == 'botones':
            btn = ButtonDataTable()
            btn.list_btn.append(self.btn_delete(row))
            return btn()
        else:
            return super().render_column(row, column)
    def display_uptime(self, obj):
        display = '<i class="fas fa-circle" style="color: green;"></i> '
        if obj.uptime:
            u = timezone.now() - obj.uptime
            display += timedelta_format(u)
        elif obj.get_uptime():
            u = timezone.now() - obj.get_uptime()
            display += timedelta_format(u)
        return display 
        diff = relativedelta(obj.time_uptime , timezone.now())
        diff = '%sd, %sh, %sm, %ss' % (diff.days, diff.hours, diff.minutes, diff.seconds)
        diff = diff.replace('-','')
        return '<i class="fas fa-circle" style="color: red;"></i> conexión pérdida hace ' + str(diff)
    def filter_queryset(self, qs):
        search = self.request.POST.get(u'search[value]', None)
        if search:
            qs = self.model.objects.filter(
                Q(alias__icontains=search) |
                Q(ip__icontains=search) |
                Q(description__icontains=search) #|
                #Q(model__model__icontains=search)
            )
        return qs
================================================

File: 0001_initial.py
================================================
# Generated by Django 2.1.3 on 2019-07-05 07:13
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalMikrotik',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=80)),
                ('address', models.TextField()),
                ('devices', models.PositiveIntegerField(default=0)),
                ('devices_cpes', models.PositiveIntegerField(default=0)),
                ('ip', models.CharField(db_index=True, max_length=15)),
                ('mac', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('mac_secondary', models.CharField(blank=True, max_length=17, null=True)),
                ('alias', models.CharField(db_index=True, max_length=80)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('firmware', models.CharField(blank=True, max_length=100, null=True)),
                ('cpeutp_total', models.PositiveSmallIntegerField(default=0)),
                ('cards', models.PositiveSmallIntegerField(default=0)),
                ('cpeutp_active', models.PositiveSmallIntegerField(default=0)),
                ('cards_active', models.PositiveSmallIntegerField(default=0)),
                ('ram', models.CharField(blank=True, max_length=10, null=True)),
                ('ram_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('cpu', models.CharField(blank=True, max_length=10, null=True)),
                ('cpu_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('temperature_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('watts', models.PositiveSmallIntegerField(default=0)),
                ('time_uptime', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical mikrotik',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalModelDevice',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('model', models.CharField(max_length=80)),
                ('brand', models.CharField(blank=True, max_length=80, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical model device',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Mikrotik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=80)),
                ('address', models.TextField()),
                ('devices', models.PositiveIntegerField(default=0)),
                ('devices_cpes', models.PositiveIntegerField(default=0)),
                ('ip', models.CharField(db_index=True, max_length=15)),
                ('mac', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('mac_secondary', models.CharField(blank=True, max_length=17, null=True)),
                ('alias', models.CharField(db_index=True, max_length=80)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('firmware', models.CharField(blank=True, max_length=100, null=True)),
                ('cpeutp_total', models.PositiveSmallIntegerField(default=0)),
                ('cards', models.PositiveSmallIntegerField(default=0)),
                ('cpeutp_active', models.PositiveSmallIntegerField(default=0)),
                ('cards_active', models.PositiveSmallIntegerField(default=0)),
                ('ram', models.CharField(blank=True, max_length=10, null=True)),
                ('ram_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('cpu', models.CharField(blank=True, max_length=10, null=True)),
                ('cpu_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('temperature', models.CharField(blank=True, max_length=10, null=True)),
                ('temperature_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('watts', models.PositiveSmallIntegerField(default=0)),
                ('time_uptime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['alias'],
            },
        ),
        migrations.CreateModel(
            name='ModelDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('model', models.CharField(max_length=80)),
                ('brand', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.ModelDevice'),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.ModelDevice'),
        ),
        migrations.AlterUniqueTogether(
            name='mikrotik',
            unique_together={('alias', 'ip')},
        ),
    ]
================================================

File: 0002_auto_20190705_1740.py
================================================
# Generated by Django 2.2 on 2019-07-05 17:40
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0001_initial'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='address',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='cards',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='cards_active',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='cpu_secondary',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='devices',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='devices_cpes',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='mac_secondary',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='name',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='ram_secondary',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='temperature_secondary',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='time_uptime',
        ),
        migrations.RemoveField(
            model_name='historicalmikrotik',
            name='watts',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='address',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='cards',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='cards_active',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='cpu_secondary',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='devices',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='devices_cpes',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='mac_secondary',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='name',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='ram_secondary',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='temperature_secondary',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='time_uptime',
        ),
        migrations.RemoveField(
            model_name='mikrotik',
            name='watts',
        ),
    ]
================================================

File: 0003_auto_20190709_0208.py
================================================
# Generated by Django 2.1.3 on 2019-07-09 02:08
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utp', '0002_auto_20190705_1740'),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalMikrotikConnection',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('connections', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mikrotik', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Mikrotik')),
            ],
            options={
                'verbose_name': 'historical mikrotik connection',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='MikrotikConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('connections', models.PositiveSmallIntegerField(default=0)),
                ('mikrotik', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='utp.Mikrotik')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.RemoveField(
            model_name='historicalmodeldevice',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='modeldevice',
            name='brand',
        ),
    ]
================================================

File: 0004_auto_20190710_1511.py
================================================
# Generated by Django 2.1.3 on 2019-07-10 15:11
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0003_auto_20190709_0208'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='firmware',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='firmware',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
================================================

File: 0005_auto_20190710_1602.py
================================================
# Generated by Django 2.1.3 on 2019-07-10 16:02
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0004_auto_20190710_1511'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='cpu',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='ram',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='temperature',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='time_uptime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='watts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='cpu',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='ram',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='temperature',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='time_uptime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='watts',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
================================================

File: 0006_auto_20190716_0725.py
================================================
# Generated by Django 2.1.3 on 2019-07-16 07:25
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0005_auto_20190710_1602'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='architecture',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='serial',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='historicalmodeldevice',
            name='brand',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='architecture',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='serial',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='modeldevice',
            name='brand',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
================================================

File: 0007_auto_20190716_0811.py
================================================
# Generated by Django 2.1.3 on 2019-07-16 08:11
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utp', '0006_auto_20190716_0725'),
    ]
    operations = [
        migrations.CreateModel(
            name='CpeUtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=80, null=True)),
                ('serial', models.CharField(db_index=True, max_length=30)),
                ('description', models.TextField()),
                ('service_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('mac', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, protocol='IPv4')),
                ('firmware', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utp.ModelDevice')),
                ('nodo_utp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.Mikrotik')),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalCpeUtp',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('alias', models.CharField(blank=True, db_index=True, max_length=80, null=True)),
                ('serial', models.CharField(db_index=True, max_length=30)),
                ('description', models.TextField()),
                ('service_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('mac', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, db_index=True, null=True, protocol='IPv4')),
                ('firmware', models.CharField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.ModelDevice')),
                ('nodo_utp', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Mikrotik')),
            ],
            options={
                'verbose_name': 'historical cpe utp',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='cpeutp',
            unique_together={('alias', 'serial', 'nodo_utp'), ('serial', 'nodo_utp')},
        ),
    ]
================================================

File: 0008_auto_20190716_1549.py
================================================
# Generated by Django 2.1.3 on 2019-07-16 15:49
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0007_auto_20190716_0811'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='mac_wan',
            field=models.CharField(blank=True, db_index=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='mac_wan',
            field=models.CharField(blank=True, db_index=True, max_length=17, null=True),
        ),
    ]
================================================

File: 0009_auto_20190717_0805.py
================================================
# Generated by Django 2.1.3 on 2019-07-17 08:05
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0008_auto_20190716_1549'),
    ]
    operations = [
        migrations.RenameField(
            model_name='historicalmikrotik',
            old_name='mac_wan',
            new_name='mac_eth1',
        ),
        migrations.RenameField(
            model_name='mikrotik',
            old_name='mac_wan',
            new_name='mac_eth1',
        ),
    ]
================================================

File: 0010_auto_20190723_1457.py
================================================
# Generated by Django 2.1.3 on 2019-07-23 14:57
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utp', '0009_auto_20190717_0805'),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalOperator',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical operator',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPlan',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('id_plan', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('aggregation_rate', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)])),
                ('matrix_plan', models.PositiveSmallIntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProfileUTP',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical profile utp',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTypePLAN',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical type plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('id_plan', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('aggregation_rate', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)])),
                ('matrix_plan', models.PositiveSmallIntegerField()),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.Operator')),
            ],
            options={
                'ordering': ['-matrix_plan'],
            },
        ),
        migrations.CreateModel(
            name='ProfileUTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TypePLAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='profile_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.ProfileUTP'),
        ),
        migrations.AddField(
            model_name='plan',
            name='type_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.TypePLAN'),
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='operator',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Operator'),
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='profile_name',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.ProfileUTP'),
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='type_plan',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.TypePLAN'),
        ),
    ]
================================================

File: 0011_auto_20190725_1039.py
================================================
# Generated by Django 2.1.3 on 2019-07-25 10:39
import django.core.validators
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0010_auto_20190723_1457'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='historicalplan',
            name='id_plan',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='id_plan',
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='historicalplan',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='limitation_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='provisioning_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='plan',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='plan',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='profileutp',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AddField(
            model_name='profileutp',
            name='limitation_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profileutp',
            name='provisioning_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profileutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4096)]),
        ),
        migrations.AlterUniqueTogether(
            name='cpeutp',
            unique_together={('alias', 'nodo_utp')},
        ),
    ]
================================================

File: 0012_auto_20190725_2152.py
================================================
# Generated by Django 2.1.3 on 2019-07-25 21:52
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0011_auto_20190725_1039'),
    ]
    operations = [
        migrations.AddField(
            model_name='cpeutp',
            name='active_mac',
            field=models.CharField(blank=True, db_index=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='historicalcpeutp',
            name='active_mac',
            field=models.CharField(blank=True, db_index=True, max_length=17, null=True),
        ),
    ]
================================================

File: 0013_auto_20190725_2347.py
================================================
# Generated by Django 2.1.3 on 2019-07-25 23:47
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0012_auto_20190725_2152'),
    ]
    operations = [
        migrations.AddField(
            model_name='cpeutp',
            name='active_ip',
            field=models.GenericIPAddressField(blank=True, db_index=True, null=True, protocol='IPv4'),
        ),
        migrations.AddField(
            model_name='historicalcpeutp',
            name='active_ip',
            field=models.GenericIPAddressField(blank=True, db_index=True, null=True, protocol='IPv4'),
        ),
    ]
================================================

File: 0014_auto_20190726_0856.py
================================================
# Generated by Django 2.1.3 on 2019-07-26 08:56
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0013_auto_20190725_2347'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='historicalplan',
            name='download_speed',
        ),
        migrations.RemoveField(
            model_name='historicalplan',
            name='upload_speed',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='download_speed',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='upload_speed',
        ),
    ]
================================================

File: 0015_auto_20190731_2002.py
================================================
# Generated by Django 2.1.3 on 2019-07-31 20:02
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utp', '0014_auto_20190726_0856'),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalRadius',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('alias', models.CharField(db_index=True, max_length=80)),
                ('ip', models.CharField(db_index=True, max_length=15)),
                ('mac_eth1', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('time_uptime', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.ModelDevice')),
            ],
            options={
                'verbose_name': 'historical radius',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRadiusConnection',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('connections', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical radius connection',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Radius',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('alias', models.CharField(db_index=True, max_length=80)),
                ('ip', models.CharField(db_index=True, max_length=15)),
                ('mac_eth1', models.CharField(blank=True, db_index=True, max_length=17, null=True)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('uptime', models.DateTimeField(blank=True, null=True)),
                ('time_uptime', models.DateTimeField(blank=True, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.ModelDevice')),
            ],
            options={
                'ordering': ['alias'],
            },
        ),
        migrations.CreateModel(
            name='RadiusConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('connections', models.PositiveSmallIntegerField(default=0)),
                ('radius', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='utp.Radius')),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.AlterField(
            model_name='cpeutp',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='historicalcpeutp',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='historicalradiusconnection',
            name='radius',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Radius'),
        ),
        migrations.AlterUniqueTogether(
            name='radius',
            unique_together={('alias', 'ip')},
        ),
    ]
================================================

File: 0016_auto_20190803_1042.py
================================================
# Generated by Django 2.1.3 on 2019-08-03 10:42
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0015_auto_20190731_2002'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicaltypeplan',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='typeplan',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
================================================

File: 0017_auto_20190805_2210.py
================================================
# Generated by Django 2.1.3 on 2019-08-05 22:10
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0016_auto_20190803_1042'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='storage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='storage',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
================================================

File: 0018_auto_20190806_0001.py
================================================
# Generated by Django 2.1.3 on 2019-08-06 00:01
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0017_auto_20190805_2210'),
    ]
    operations = [
        migrations.RenameField(
            model_name='historicalmikrotik',
            old_name='watts',
            new_name='voltage',
        ),
        migrations.RenameField(
            model_name='mikrotik',
            old_name='watts',
            new_name='voltage',
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='comment',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='power_consumption',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalmikrotik',
            name='temperature_cpu',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='comment',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='power_consumption',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='temperature_cpu',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
================================================

File: 0019_auto_20190806_2124.py
================================================
# Generated by Django 2.1.3 on 2019-08-06 21:24
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0018_auto_20190806_0001'),
    ]
    operations = [
        migrations.RenameField(
            model_name='historicalmikrotik',
            old_name='cpeutp_total',
            new_name='cpeutps',
        ),
        migrations.RenameField(
            model_name='mikrotik',
            old_name='cpeutp_total',
            new_name='cpeutps',
        ),
    ]
================================================

File: 0020_auto_20190807_0051.py
================================================
# Generated by Django 2.1.3 on 2019-08-07 00:51
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0019_auto_20190806_2124'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicalmikrotik',
            name='comment',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mikrotik',
            name='comment',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
================================================

File: 0021_auto_20190809_0024.py
================================================
# Generated by Django 2.1.3 on 2019-08-09 00:24
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0020_auto_20190807_0051'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalprofileutp',
            name='radius',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Radius'),
        ),
        migrations.AddField(
            model_name='profileutp',
            name='radius',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utp.Radius'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='limitation_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='limitation_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
================================================

File: 0022_auto_20190809_0726.py
================================================
# Generated by Django 2.1.3 on 2019-08-09 07:26
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utp', '0021_auto_20190809_0024'),
    ]
    operations = [
        migrations.CreateModel(
            name='HistoricalSystemProfile',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('limitation_name', models.CharField(max_length=50)),
                ('download_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('upload_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('provisioning_available', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical system profile',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SystemProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status_field', models.BooleanField(default=True)),
                ('id_data', models.UUIDField(blank=True, db_index=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('limitation_name', models.CharField(max_length=50)),
                ('download_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('upload_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('provisioning_available', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='historicalprofileutp',
            name='system_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.SystemProfile'),
        ),
        migrations.AddField(
            model_name='profileutp',
            name='system_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utp.SystemProfile'),
        ),
    ]
================================================

File: 0023_auto_20190809_1137.py
================================================
# Generated by Django 2.1.3 on 2019-08-09 11:37
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0022_auto_20190809_0726'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
================================================

File: 0024_auto_20190809_1147.py
================================================
# Generated by Django 2.1.3 on 2019-08-09 11:47
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0023_auto_20190809_1137'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicalprofileutp',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='profileutp',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
================================================

File: 0025_auto_20190812_2314.py
================================================
# Generated by Django 2.1.3 on 2019-08-12 23:14
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0024_auto_20190809_1147'),
    ]
    operations = [
        migrations.AddField(
            model_name='historicalmikrotik',
            name='radius',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.Radius'),
        ),
        migrations.AddField(
            model_name='mikrotik',
            name='radius',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utp.Radius'),
        ),
    ]
================================================

File: 0026_auto_20190815_1239.py
================================================
# Generated by Django 2.1.3 on 2019-08-15 12:39
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0025_auto_20190812_2314'),
    ]
    operations = [
        migrations.AddField(
            model_name='cpeutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='cpeutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='historicalcpeutp',
            name='download_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='historicalcpeutp',
            name='upload_speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='mikrotik',
            name='radius',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utp.Radius'),
        ),
    ]
================================================

File: 0027_auto_20190815_1313.py
================================================
# Generated by Django 2.1.3 on 2019-08-15 13:13
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0026_auto_20190815_1239'),
    ]
    operations = [
        migrations.AddField(
            model_name='cpeutp',
            name='service_number_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicalcpeutp',
            name='service_number_verified',
            field=models.BooleanField(default=False),
        ),
    ]
================================================

File: 0028_auto_20190821_1554.py
================================================
# Generated by Django 2.1.3 on 2019-08-21 15:54
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0027_auto_20190815_1313'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicalplan',
            name='profile_name',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utp.SystemProfile'),
        ),
        migrations.AlterField(
            model_name='historicalsystemprofile',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='plan',
            name='profile_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utp.SystemProfile'),
        ),
        migrations.AlterField(
            model_name='systemprofile',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
================================================

File: 0029_auto_20190821_1957.py
================================================
# Generated by Django 2.1.3 on 2019-08-21 19:57
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0028_auto_20190821_1554'),
    ]
    operations = [
        migrations.AlterField(
            model_name='profileutp',
            name='system_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utp.SystemProfile'),
        ),
    ]
================================================

File: 0030_auto_20190822_0708.py
================================================
# Generated by Django 2.1.3 on 2019-08-22 07:08
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0029_auto_20190821_1957'),
    ]
    operations = [
        migrations.AlterField(
            model_name='historicalsystemprofile',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='systemprofile',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
================================================

File: 0031_auto_20190829_1050.py
================================================
# Generated by Django 2.1.3 on 2019-08-29 10:50
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        ('utp', '0030_auto_20190822_0708'),
    ]
    operations = [
        migrations.AlterField(
            model_name='mikrotik',
            name='radius',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utp.Radius'),
        ),
    ]
================================================

File: mikrotik.py
================================================
#!/usr/bin/python3
#import os
import sys
from os.path import join
try:
    import posix
except Exception as e:
    pass
import time
import logging
import binascii
import socket
import select
import hashlib
from datetime import datetime
from django.conf import settings
#from dynamic_preferences.registries import global_preferences_registry
#global_preferences = global_preferences_registry.manager()
def get_logger(name, is_in_cron=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG) # WARNING ERROR
    # now = "{0.year}-{0.month}-{0.day}-{0.hour}".format(datetime.now()) 
    # if is_in_cron:
    #     ruta = join(settings.BASE_DIR_LOG,'mik_%s_cron.log' % now)
    # else:
    #     ruta = join(settings.BASE_DIR_LOG,'mik_%s_web.log' % now)
    ruta = join(settings.BASE_DIR_LOG,'mik_web.log')
    file_log = open(str(ruta), "a+")
    format_log = "%(levelname)-.3s %(asctime)s.%(msecs)03d %(name)s %(message)s"
    #os.chmod(ruta, 777)
    handler1 = logging.StreamHandler(file_log)
    handler1.setFormatter(logging.Formatter(format_log, "%Y%m%d-%H:%M:%S"))
    logger.addHandler(handler1)
    return logger
logger = get_logger('Mikrotik', False)
class ApiRos:
    "Routeros api"
    def __init__(self, sk):
        self.sk = sk
        self.currenttag = 0
    def login(self, username, pwd):
        md = hashlib.md5()
        md.update(b'\x00')
        md.update(pwd.encode('UTF-8'))
        respuesta = self.talk(["/login", "=name=" + username,
                   "=password=" + pwd])
        if respuesta[0][1]!={}:
            for repl, attrs in self.talk(["/login"]):
                chal = binascii.unhexlify((attrs['=ret']).encode('UTF-8'))
            md = hashlib.md5()
            md.update(b'\x00')
            md.update(pwd.encode('UTF-8'))
            md.update(chal)
            return self.talk(["/login", "=name=" + username,
                   "=response=00" + binascii.hexlify(md.digest()).decode('UTF-8')])
        return []
    def talk(self, words):
        if self.writeSentence(words) == 0: return
        r = []
        while 1:
            i = self.readSentence();
            if len(i) == 0: continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if (j == -1):
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j+1:]
            r.append((reply, attrs))
            if reply == '!done': return r
    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret
    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '':
                return r
            r.append(w)
    def writeWord(self, w):
        logger.info("Execute:%s"%w)
        #print(("<<< " + w))
        self.writeLen(len(w))
        self.writeStr(w)
    def readWord(self):
        ret = self.readStr(self.readLen())
        logger.info("Received:%s"%ret)
        #print((">>> " + ret))
        return ret
    def writeLen(self, l):
        if l < 0x80:
            self.writeStr(chr(l))
        elif l < 0x4000:
            l |= 0x8000
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        else:
            self.writeStr(chr(0xF0))
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
    def readLen(self):
        c = ord(self.readStr(1))
        if (c & 0x80) == 0x00:
            pass
        elif (c & 0xC0) == 0x80:
            c &= ~0xC0
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xE0) == 0xC0:
            c &= ~0xE0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xF0) == 0xE0:
            c &= ~0xF0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xF8) == 0xF0:    
            c = ord(self.readStr(1))     
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        return c                    
    def writeStr(self, str):        
        n = 0;                      
        while n < len(str):         
            r = self.sk.send(bytes(str[n:], 'UTF-8'))
            if r == 0:
                logger.error("RuntimeErr: Connection closed by remote end")
                raise RuntimeError("connection closed by remote end")
            n += r                  
    def readStr(self, length):      
        ret = ''
        while len(ret) < length:
            s = self.sk.recv(length - len(ret))
            if s == '': 
                logger.error("RuntimeErr: Connection closed by remote end")
                raise RuntimeError("connection closed by remote end")
            ret += s.decode('UTF-8', 'replace')
        return ret
def drop_client(contract):
    if not contract.node:
        logger.error("Tried to DROP contract #%s without a node", contract.number)
        return
    mikrotik_ip = contract.node.mikrotik_ip
    user = contract.node.mikrotik_username
    password = contract.node.mikrotik_password
    primary = contract.primary_equipment
    slug = contract.slug
    if primary:
        s = None
        for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                 s = socket.socket(af, socktype, proto)
                 s.settimeout(1)
            except socket.error as msg:
                s = None
                continue
            try:
                s.connect(sa)
            except socket.error as msg:
                s.close()
                s = None
                continue
            break
        if s is None:
            # print('could not open socket')
            logger.error("Can't open socket to Node %s to DROP contract #%s (Mikrotik: %s)", contract.node.code, contract.number, mikrotik_ip)
            return
            # sys.exit(1) # WTH
        apiros = ApiRos(s)
        apiros.login(user, password)
        apiros.talk(["/ip/firewall/address-list/add",
                     "=list=CORTES CLIENTES",
                     "=address={}".format(primary.ip),
                     "=comment=servicio #{}".format(slug)])
        logger.info("DROPPED %s on Node %s for contract #%s", primary.ip, contract.node.code, contract.number)
    else:
        logger.error("Tried to DROP contract #%s without a primary")
def activate_client(contract):
    if not contract.node:
        logger.error("Tried to ACTIVATE contract #%s without a node", contract.number)
        return
    mikrotik_ip = contract.node.mikrotik_ip
    user = contract.node.mikrotik_username
    password = contract.node.mikrotik_password
    primary = contract.primary_equipment
    if primary:
        s = None
        for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                 s = socket.socket(af, socktype, proto)
                 s.settimeout(1)
            except socket.error as msg:
                s = None
                continue
            try:
                s.connect(sa)
            except socket.error as msg:
                s.close()
                s = None
                continue
            break
        if s is None:
            # print('could not open socket')
            logger.error("Can't open socket to Node %s to ACTIVATE contract #%s (Mikrotik: %s)", contract.node.code, contract.number, mikrotik_ip)
            return
            # sys.exit(1) # why this was here, I can't comprehend
        apiros = ApiRos(s)
        apiros.login(user, password)
        response = apiros.talk(["/ip/firewall/address-list/print",
                                "?list=CORTES CLIENTES",
                                "?address={}".format(primary.ip),
                                "=.proplist=.id"])
        for reply, data in response:
            if reply == '!re':
                try:
                    client_id = data['=.id']
                    apiros.talk(["/ip/firewall/address-list/remove", "=.id={}".format(client_id)])
                    logger.info("ACTIVATED %s on Node %s for contract #%s", primary.ip, contract.node.code, contract.number)
                except KeyError:
                    pass
    else:
        logger.error("Tried to ACTIVATE contract #%s without a primary", contract.number)
def get_client_status(mikrotik_ip, user, password, client_ip):
    return False
    s = None
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
             s.settimeout(1)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    apiros = ApiRos(s)
    apiros.login(user, password)
    response = apiros.talk(["/ip/firewall/address-list/print",
                            "?list=CORTES CLIENTES",
                            ])
    is_there = False
    for reply, data in response:
        if reply == '!re':
            try:
                if client_ip == data['=address']:
                    is_there = True
            except KeyError:
                pass
    return is_there
def get_dropped(mikrotik_ip, user, password):
    s = None
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    s.settimeout(1)
    apiros = ApiRos(s)
    apiros.login(user, password)
    response = apiros.talk(["/ip/firewall/address-list/print",
                            "?list=CORTES CLIENTES",
                            ])
    raw_results = []
    for reply, data in response:
        if reply == '!re':
            try:
                raw_results.append(data['=comment'])
            except KeyError:
                pass
    results = []
    for item in raw_results:
        try:
            contract_number = item.split('#')[1].split(' ')[0]
            results.append(int(contract_number))
        except:
            pass
    return results
def obtain_first_numbers(string):
    arr = ""
    for i in range(len(string)):
        try:
            new = int(string[i])
            arr = arr + string[i]
        except:
            break
    if arr == "":
        return None
    else:
        return int(arr)
def get_mikrotik_info(mikrotik_ip, user, password):
    #sys.argv[1]
    s = None
    #print ('list_interfaces')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('get_mikrotik_info Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    results = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("get_mikrotik_info Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        response = apiros.talk(["/system/routerboard/print",
                                #"=.proplist=routerboard,model",
        #response = apiros.talk(["/system/identity/export",
        #                        "=file=temp.txt"
                                ])
        #print(response)
        #response = apiros.talk(["/file/print",
                                #"=from=temp.rsc",
        #                        "=detail"
                                #"=.proplist=contents,.id",
        #                        ])
        #print(response)
        #response = apiros.talk(["/file/remove"])
        #print(response)
        uptime = apiros.talk(["/system/resource/print",
                             #"=.proplist=uptime",
                             ])
        #print(uptime)
        name = apiros.talk(["/system/identity/print",
                            #"=.proplist=name",
                            ])
        health = apiros.talk(["/system/health/print"])       
        #print(health)
        for reply, data in response:
            if reply == '!re':
                try:
                    #firmwarestr = data['=firmware-type']+" v"+data['=current-firmware']
                    results.append(dict(routerboard=data['=routerboard'],
                                        serial=data['=serial-number'],
                                        #firmware=firmwarestr),
                                        ))
                    logger.info("get_mikrotik_info: Append serial and routerboard")
                except KeyError:
                    logger.error("get_mikrotik_info KeyErr: Could not append serial and routerboard")
                    print("pass in response")
        if results == []:
            results = [{}]
        index = 0
        for reply, data in uptime:
            if reply == '!re':
                try:
                    firmwarestr = "RouterOS v"+data['=version']
                    ram = (float(data['=total-memory']) - float(data['=free-memory'])) / float(data['=total-memory'])
                    ram = round(ram*100,1)
                    hdd = (float(data['=total-hdd-space']) - float(data['=free-hdd-space'])) / float(data['=total-hdd-space'])
                    hdd = round(hdd*100,1)
                    results[index]['uptime'] = data['=uptime']
                    results[index]['brand'] = data['=platform']
                    results[index]['model'] = data['=board-name']
                    results[index]['architecture'] = data['=architecture-name']
                    results[index]['cpu'] = int(data['=cpu-load'])
                    results[index]['ram'] = ram
                    results[index]['hdd'] = hdd
                    results[index]['firmware'] = firmwarestr
                    logger.info("get_mikrotik_info: Append health info")
                except:
                    logger.info("get_mikrotik_info Err: Could not append health info")
                    print("pass in uptime")
        if results == []:
            results = [{}]
        index = 0
        for reply, data in name:
            if reply == '!re':
                try:
                    results[index]['description'] = data['=name']
                    logger.info("get_mikrotik_info: Append description")
                except:
                    logger.error("get_mikrotik_info Err: Could not append description")
                    print("pass")
        if results == []:
            results = [{}]
        index = 0
        for reply, data in health:
            if reply == '!re':
                try:
                    if '=power-consumption' in data.keys():
                        results[index]['power_consumption'] = data['=power-consumption']
                    else:
                        results[index]['power_consumption'] = ""
                    if '=cpu-temperature' in data.keys():
                        results[index]['temperature_cpu'] = data['=cpu-temperature']
                    else:
                        results[index]['temperature_cpu'] = ""
                    if '=temperature' in data.keys():
                        results[index]['temperature'] = data['=temperature']
                    else:
                        results[index]['temperature'] = ""
                    if '=voltage' in data.keys():
                        results[index]['voltage'] = data['=voltage']
                    else:
                        results[index]['voltage'] = ""
                    logger.info("get_mikrotik_info: Append power_consumption,cpu-temp, temperature, voltage")
                except:
                    logger.error("get_mikrotik_info Err: Could not append power_consumption,cpu-temp, temperature, or voltage")
                    print("pass")
        if results == []:
            results = [{}]
        index = 0
        leases = apiros.talk(["/ip/dhcp-server/lease/print"])       
        neighbors = apiros.talk(["/ip/neighbor/print"])
        resultsleases=[]
        for reply, data in leases:
            if reply == '!re':
                try:
                    if data["=status"] == "waiting":
                        statusbool = False
                    else:
                        statusbool = True
                    if '=active-mac-address' in data.keys():
                        active_mac = data["=active-mac-address"]
                    else:
                        active_mac = ""
                    if '=active-address' in data.keys():
                        active_address = data["=active-address"]
                    else:
                        active_address = ""
                    var = obtain_first_numbers(data['=host-name'])
                    resultsleases.append(dict(description=data['=host-name'],
                                        active_mac=active_mac,
                                        mac=data['=mac-address'],
                                        status=statusbool,
                                        active_ip=active_address,
                                        ip=data['=address'],
                                        service_number=var
                                        ))
                    logger.info("get_mikrotik_info: Append lease, hostname: "+data['=host-name'])
                except KeyError:
                    logger.error("get_mikrotik_info KeyErr: Could not append lease with data="+str(data))
                    print("pass in leases")
        if results == []:
            results = [{}]
        index = 0
        for reply, data in neighbors:
            if reply == '!re':
                try:
                    ip = data['=address']
                    found = False
                    for i in range(len(resultsleases)):
                        if resultsleases[i]['ip'] == ip:
                            index = i
                            found = True
                            break
                    if found:
                        resultsleases[index]['brand'] = data['=platform']
                        resultsleases[index]['firmware'] = data['=version']
                        if '=board' in data.keys():
                            resultsleases[index]['model'] = data['=board']
                        else:
                            resultsleases[index]['model'] = ''
                        if '=uptime' in data.keys():
                            resultsleases[index]['uptime'] = data['=uptime']
                        else:
                            resultsleases[index]['uptime'] = None
                        logger.info("get_mikrotik_info: Append additional info to lease with ip="+ip)
                    else:
                        logger.info("get_mikrotik_info: Could not find additional info for lease with ip="+ip)
                except:
                    logger.error("get_mikrotik_info Err: Could not append additional info to lease with data="+str(data))
                    print("pass in neighbors")
        speeds = apiros.talk(["/queue/simple/print"])
        if results == []:
            results = [{}]
        index = 0
        for reply, data in speeds:
            if reply == '!re':
                try:
                    ip = data['=target']
                    found = False
                    for i in range(len(resultsleases)):
                        if resultsleases[i]['ip'] == ip:
                            index = i
                            found = True
                            break
                    if found:
                        temp = data['=limit-at'].split("/")
                        us = temp[0]
                        ds = temp[1]
                        resultsleases[index]['download_speed'] = ds
                        resultsleases[index]['upload_speed'] = us
                        logger.info("get_mikrotik_info: Append download/upload speeds to lease with ip="+ip)
                    else:
                        logger.info("get_mikrotik_info: Could not find download/upload speeds for lease with ip="+ip)
                except:
                    logger.error("get_mikrotik_info Err: Could not append download/upload speeds to lease with data="+str(data))
                    print("pass in neighbors")
        results[0]['leases'] = resultsleases
    except:
        logger.error("get_mikrotik_info UnhandledErr: Unhandled exception happened")
        pass
    if len(results) == 0:
        return {}
    else:
        #print(results[0])
        return results[0]
def get_mikrotik_leases(mikrotik_ip, user, password):
    #sys.argv[1]
    s = None
    #print ('list_interfaces')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('get_mikrotik_leases Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    resultsleases = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("get_mikrotik_leases Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        leases = apiros.talk(["/ip/dhcp-server/lease/print"])       
        neighbors = apiros.talk(["/ip/neighbor/print"])
        resultsleases=[]
        for reply, data in leases:
            if reply == '!re':
                try:
                    if data["=status"] == "waiting":
                        statusbool = False
                    else:
                        statusbool = True
                    if '=active-mac-address' in data.keys():
                        active_mac = data["=active-mac-address"]
                    else:
                        active_mac = ""
                    if '=active-address' in data.keys():
                        active_address = data["=active-address"]
                    else:
                        active_address = ""
                    var = obtain_first_numbers(data['=host-name'])
                    resultsleases.append(dict(description=data['=host-name'],
                                        active_mac=active_mac,
                                        mac=data['=mac-address'],
                                        status=statusbool,
                                        active_ip=active_address,
                                        ip=data['=address'],
                                        service_number=var
                                        ))
                    logger.info("get_mikrotik_leases: Append lease, hostname: "+data['=host-name'])
                except KeyError:
                    logger.error("get_mikrotik_leases KeyErr: Could not append lease with data="+str(data))
                    print("pass in leases")
        index = 0
        for reply, data in neighbors:
            if reply == '!re':
                try:
                    ip = data['=address']
                    found = False
                    for i in range(len(resultsleases)):
                        if resultsleases[i]['ip'] == ip:
                            index = i
                            found = True
                            break
                    if found:
                        resultsleases[index]['brand'] = data['=platform']
                        resultsleases[index]['firmware'] = data['=version']
                        if '=board' in data.keys():
                            resultsleases[index]['model'] = data['=board']
                        else:
                            resultsleases[index]['model'] = ''
                        if '=uptime' in data.keys():
                            resultsleases[index]['uptime'] = data['=uptime']
                        else:
                            resultsleases[index]['uptime'] = None
                        logger.info("get_mikrotik_leases: Append lease, ip: "+ip)
                except:
                    logger.error("get_mikrotik_leases Err: Could not append lease additional info with data="+str(data))
                    print("pass in neighbors")
        speeds = apiros.talk(["/queue/simple/print"])
        index = 0
        for reply, data in speeds:
            if reply == '!re':
                try:
                    ip = data['=target']
                    found = False
                    for i in range(len(resultsleases)):
                        if resultsleases[i]['ip'] == ip:
                            index = i
                            found = True
                            break
                    if found:
                        temp = data['=limit-at'].split("/")
                        us = round(int(temp[0])/1000000,0)
                        ds = round(int(temp[1])/1000000,0)
                        resultsleases[index]['download_speed'] = ds
                        resultsleases[index]['upload_speed'] = us
                        logger.info("get_mikrotik_info: Append download/upload speeds to lease with ip="+ip)
                    else:
                        logger.info("get_mikrotik_info: Could not find download/upload speeds for lease with ip="+ip)
                except:
                    logger.error("get_mikrotik_info Err: Could not append download/upload speeds to lease with data="+str(data))
                    print("pass in neighbors")
    except:
        logger.error("get_mikrotik_leases UnhandledErr: Unhandled exception happened")
        pass
    return resultsleases
def get_radius_profile(mikrotik_ip, user, password):
    #sys.argv[1]
    s = None
    #print ('list_interfaces')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('get_radius_profile Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    results = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("get_radius_profile Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        response = apiros.talk(["/tool/user-manager/profile/profile-limitation/print",
                                #"=.proplist=routerboard,model",
                                ])
        limitations = apiros.talk(["/tool/user-manager/profile/limitation/print"
                                ])
        for reply, data in response:
            if reply == '!re':
                try:
                    results.append(dict(name=data['=profile'],
                                        limitation_name=data['=limitation']
                                        ))
                    logger.info("get_radius_profile: Append profile link with data="+str(data))
                except KeyError:
                    logger.error("get_radius_profile KeyErr: Could not ppend profile link with data="+str(data))
                    print("pass in response")
        if results!=[]:
            for reply, data in limitations:
                if reply == '!re':
                    try:
                        limitation = data['=name']
                        found = False
                        for i in range(len(results)):
                            speed = results[i]
                            if speed['limitation_name'] == limitation:
                                found = True
                                index = i
                                break
                        if found:
                            results[index]['upload_speed'] = data['=rate-limit-rx']
                            results[index]['download_speed'] = data['=rate-limit-tx']
                            logger.info("get_radius_profile: Append profile speeds with data="+str(data))
                    except KeyError:
                        logger.info("get_radius_profile: Could not append profile speeds with data="+str(data))
                        print("pass in response")
    except:
        logger.error("get_mikrotik_leases UnhandledErr: Unhandled exception happened")
        pass
    print(results)
    if len(results) == 0:
        return []
    else:
        #print(results[0])
        return results
def create_radius_profile(mikrotik_ip, user, password,data):
    #sys.argv[1]
    s = None
    #print ('list_interfaces')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except socket.error as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('create_radius_profile Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    results = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("create_radius_profile Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        profile = data['profile']
        limitation = data['limitation']
        download_speed = data['download_speed']
        upload_speed = data['upload_speed']
        search_profile = apiros.talk(["/tool/user-manager/profile/print",
                                    ])
        found_profile = False
        for reply,data in search_profile:
            if reply=='!re':
                if data['=name'] == profile:
                    found_profile = True
                    logger.info("create_radius_profile: Found profile with given data")
        if not found_profile:
            logger.info("create_radius_profile: Could not find profile with given data, creating one")
            logger.info("create_radius_profile: Creating profile with name="+profile)
            create_profile = apiros.talk(["/tool/user-manager/profile/add",
                                    "=name="+profile,
                                    "=owner=admin",
                                    "=starts-at=now",
                                    ])
            for reply,data in create_profile:
                if reply=='!trap':
                    msg = data['=message']
                    logger.error("create_radius_profile Err: Creating profile resulted in !trap from device. Msg:"+msg)
                    return msg
            logger.info("create_radius_profile: Profile created, name="+profile)
        search_limitation = apiros.talk(["/tool/user-manager/profile/limitation/add",])
        found_limitation = False
        for reply,data in search_limitation:
            if reply=='!re':
                if data['=name'] == limitation:
                    found_limitation = True
                    logger.info("create_radius_profile: Found limitation with given data: name="+limitation)
        if not found_limitation:
            logger.info("create_radius_profile: Could not find limitation with given data, creating one")
            data = {
                "name" : limitation,
                "download_speed" : str(download_speed)+"M",
                "upload_speed" : str(upload_speed)+"M",
            }
            logger.info("create_radius_profile: Creating limitation with data="+str(data))
            create_limitation = apiros.talk(["/tool/user-manager/profile/limitation/add",
                                    "=name="+limitation,
                                    "=owner=admin",
                                    "=rate-limit-rx="+str(download_speed)+"M",
                                    "=rate-limit-tx="+str(upload_speed)+"M",
                                    ])
            for reply,data in create_limitation:
                if reply=='!trap':
                    msg = data['=message']
                    logger.error("create_radius_profile Err: Creating limitation resulted in !trap from device. Msg:"+msg)
                    return msg
            logger.info("create_radius_profile: Limitation created, data="+str(data))
        logger.info("create_radius_profile: Creating profile/limitation link with profile="+profile+" limitation="+limitation)
        link = apiros.talk(["/tool/user-manager/profile/profile-limitation/add",
                                "=profile="+profile,
                                "=limitation="+limitation,
                                ])
        for reply,data in link:
            if reply=='!trap':
                msg = data['=message']
                logger.error("create_radius_profile Err: Creating profile/limitation link resulted in !trap from device. Msg:"+msg)
                return msg
        logger.info("create_radius_profile: Created profile/limitation link with profile="+profile+" limitation="+limitation)
    except:
        logger.error("create_radius_profile UnhandledErr: Unhandled exception happened")
        return ""
    print("success")
    results.append({})
    return results[0]
def delete_radius_profile_witheverything(mikrotik_ip, user, password,data):
    #sys.argv[1]
    s = None
    #print ('delete_interface')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('delete_radius_profile_witheverything Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    results = []
    try:
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("delete_radius_profile_witheverything Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        profile = data['profile']
        limitation = data['limitation']
        # Get and delete link
        logger.info("delete_radius_profile_witheverything: Getting profile/limitation link number where profile="+profile+" limitation="+limitation)
        search_link = apiros.talk(["/tool/user-manager/profile/profile-limitation/print",
                                ])
        index = 0
        linkid = None
        for reply,data in search_link:
            if reply=='!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Looking up profile/limitation link number resulted in !trap from device. Msg:"+msg)
                return msg
            if reply=='!re':
                if data['=profile'] == profile and data['=limitation']==limitation:
                    linkid = index
                    logger.info("delete_radius_profile_witheverything: Got profile/limitation link number="+str(linkid))
                    break
            index += 1
        if linkid == None:
            logger.error("delete_radius_profile_witheverything Err: Could not find profile/limitation link where profile="+profile+" limitation="+limitation)
            return "No se encontró profile-limitation link en el RADIUS. Por favor actualice la lista de profile"
        logger.info("delete_radius_profile_witheverything: Deleting profile/limitation link where number="+str(linkid))
        delete_link = apiros.talk(["/tool/user-manager/profile/profile-limitation/remove",
                                    "=numbers="+str(linkid)
                                ])
        keepgoing = False
        for reply,data in delete_link:
            if reply == '!done':
                keepgoing = True
                logger.info("delete_radius_profile_witheverything: Deleted profile/limitation link where number="+str(linkid))
            if reply == '!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Deleting profile/limitation link where number="+str(linkid)+" resulted in !trap from device. Msg:"+msg)    
        if not keepgoing:
            logger.error("delete_radius_profile_witheverything Err: Could not delete profile/limitation link where number="+str(linkid))
            return "Ocurrió un error inesperado, no se pudo eliminar el profile/limitation link" 
        # Get and delete profile
        logger.info("delete_radius_profile_witheverything: Getting profile number where name="+profile)
        search_profile = apiros.talk(["/tool/user-manager/profile/print",
                                ])
        index = 0
        profileid = None
        for reply,data in search_profile:
            if reply=='!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Looking up profile number resulted in !trap from device. Msg:"+msg)
                return msg
            if reply=='!re':
                if data['=name'] == profile:
                    profileid = index
                    logger.info("delete_radius_profile_witheverything: Got profile number="+str(profileid))
                    break
            index += 1
        if profileid == None:
            logger.error("delete_radius_profile_witheverything Err: Could not find profile where name="+profile)
            return "No se encontró el profile en el RADIUS. Por favor actualice la lista de profile"
        logger.info("delete_radius_profile_witheverything: Deleting profile where number="+str(profileid))
        delete_profile = apiros.talk(["/tool/user-manager/profile/remove",
                                    "=numbers="+str(profileid)
                                ])
        keepgoingProfile = False
        for reply,data in delete_profile:
            if reply == '!done':
                keepgoingProfile = True
                logger.info("delete_radius_profile_witheverything: Deleted profile where number="+str(profileid))
            if reply == '!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Deleting profile where number="+str(profileid)+" resulted in !trap from device. Msg:"+msg)    
        if not keepgoingProfile:
            logger.error("delete_radius_profile_witheverything Err: Could not delete profile where number="+str(profileid))
            return "Ocurrió un error inesperado. Se eliminó el profile/limitation link pero no se pudo eliminar el profile ni la limitation en el dispositivo" 
        # Get and delete limitation
        logger.info("delete_radius_profile_witheverything: Getting limitation number where name="+limitation)
        search_limitation = apiros.talk(["/tool/user-manager/profile/limitation/print",
                                ])
        index = 0
        limitationid = None
        for reply,data in search_limitation:
            if reply=='!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Looking up limitation number resulted in !trap from device. Msg:"+msg)
                return msg
            if reply=='!re':
                if data['=name'] == limitation:
                    limitationid = index
                    logger.info("delete_radius_profile_witheverything: Got limitation number="+str(limitationid))
                    break
            index += 1
        if limitationid == None:
            logger.error("delete_radius_profile_witheverything Err: Could not find limitation where name="+limitation)
            return "No se encontró el profile en el RADIUS. Por favor actualice la lista de profile"
        logger.info("delete_radius_profile_witheverything: Deleting limitation where number="+str(limitationid))
        delete_limitation = apiros.talk(["/tool/user-manager/profile/limitation/remove",
                                    "=numbers="+str(limitationid)
                                ])
        keepgoingLimitation = False
        for reply,data in delete_limitation:
            if reply == '!done':
                keepgoingLimitation = True
                logger.info("delete_radius_profile_witheverything: Deleted limitation where number="+str(limitationid))
            if reply == '!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_witheverything Err: Deleting limitation where number="+str(limitationid)+" resulted in !trap from device. Msg:"+msg)    
        if not keepgoingLimitation:
            logger.error("delete_radius_profile_witheverything Err: Could not delete limitation where number="+str(limitationid))
            return "Ocurrió un error inesperado. Se ha eliminado el profile/limitation link, más no se pudo eliminar la limitation en el dispositivo" 
    except:
        logger.error("delete_radius_profile_witheverything UnhandledErr: Unhandled exception happened")
        return ""
    print("success")
    results.append({})
    return results[0]
def delete_radius_profile_onlylink(mikrotik_ip, user, password,data):
    #sys.argv[1]
    s = None
    #print ('delete_interface')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        logger.error('delete_radius_profile_onlylink Err: Could not open socket for connection')
        return 'No se pudo abrir el socket para realizar la conección'
    results = []
    try:
        s.settimeout(1)
        apiros = ApiRos(s)
        resp_login = apiros.login(user, password)
        for reply,data in resp_login:
            if reply == '!trap':
                logger.error("delete_radius_profile_onlylink Err: Credentials given are not valid. Login unsucessful")
                return "Las credenciales dadas no son válidas"
        profile = data['profile']
        limitation = data['limitation']
        # Get and delete link
        logger.info("delete_radius_profile_onlylink: Getting profile/limitation link number where profile="+profile+" limitation="+limitation)
        search_link = apiros.talk(["/tool/user-manager/profile/profile-limitation/print",
                                ])
        index = 0
        linkid = None
        for reply,data in search_link:
            if reply=='!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_onlylink Err: Looking up profile/limitation link number resulted in !trap from device. Msg:"+msg)
                return msg
            if reply=='!re':
                if data['=profile'] == profile and data['=limitation']==limitation:
                    linkid = index
                    logger.info("delete_radius_profile_onlylink: Got profile/limitation link number="+str(linkid))
                    break
            index += 1
        if linkid == None:
            logger.error("delete_radius_profile_onlylink Err: Could not find profile/limitation link where profile="+profile+" limitation="+limitation)
            return "No se encontró profile-limitation link en el RADIUS. Por favor actualice la lista de profile"
        logger.info("delete_radius_profile_onlylink: Deleting profile/limitation link where number="+str(linkid))
        delete_link = apiros.talk(["/tool/user-manager/profile/profile-limitation/remove",
                                    "=numbers="+str(linkid)
                                ])
        keepgoing = False
        for reply,data in delete_link:
            if reply == '!done':
                keepgoing = True
                logger.info("delete_radius_profile_onlylink: Deleted profile/limitation link where number="+str(linkid))
            if reply == '!trap':
                msg = data['=message']
                logger.error("delete_radius_profile_onlylink Err: Deleting profile/limitation link where number="+str(linkid)+" resulted in !trap from device. Msg:"+msg)    
        if not keepgoing:
            logger.error("delete_radius_profile_onlylink Err: Could not delete profile/limitation link where number="+str(linkid))
            return "Ocurrió un error inesperado, no se pudo eliminar el profile/limitation link" 
    except:
        logger.error("delete_radius_profile_onlylink UnhandledErr: Unhandled exception happened")
        print("Something failed in creating a profile in the device")
        return ""
    print("success")
    results.append({})
    return results[0]
def convert_uptime(uptime_str):
    date,time = uptime_str.split(" ")
    month,day,year = date.split("/")
    if "apr" in month:
        month = "04"
    return year+"-"+month+"-"+day+" "+time
def list_interfaces(mikrotik_ip, user, password):
    #sys.argv[1]
    s = None
    #print ('list_interfaces')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    results = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        apiros.login(user, password)
        response = apiros.talk(["/interface/print",
                                "=.proplist=.id,name,type,mac-address,last-link-up-time,status",])
        for reply, data in response:
            if reply == '!re':
                try:
                    newuptime = convert_uptime(data['=last-link-up-time'])
                    results.append(dict(name=data['=name'],
                                        mac=data['=mac-address'],
                                        type=data['=type'],
                                        uptime=newuptime,
                                        id=data['=.id'],
                                        status=True))
                except KeyError:
                    newuptime = None
                    results.append(dict(name=data['=name'],
                                        mac=data['=mac-address'],
                                        type=data['=type'],
                                        uptime=newuptime,
                                        id=data['=.id'],
                                        status=False))
        #print (results)
    except:
        print("Connection timed out")
    return results
def create_interface(mikrotik_ip, user, password,data):
    #sys.argv[1]
    s = None
    #print ('create_interface')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    results = []
    #print ('time')
    s.settimeout(1)
    apiros = ApiRos(s)
    apiros.login(user, password)
    id_given = data['id']
    alias = data['alias']
    #ip = data['ip']
    #model = data['model']
    description = data['description']
    #cpeutp_total = data['cpeutp_total']
    #cpeutp_active = data['cpeutp_active']
    #uptime = data['uptime']
    response = apiros.talk(["/interface/vlan/add",
                            "=vlan-id="+str(id_given),
                            "=name="+alias,
                            "=interface=ether1",
                            "=comment="+description,
                            ])
    return response
def delete_interface(mikrotik_ip, user, password,data):
    #sys.argv[1]
    s = None
    #print ('delete_interface')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    response = []
    try:
        #print ('time')
        s.settimeout(1)
        apiros = ApiRos(s)
        apiros.login(user, password)
        alias = "\""+data['alias']+"\""
        reply, _ = apiros.talk(["/interface/vlan/print",
                                "=from="+alias,
                                "=.proplist=.id",
                                ])
        id_given = reply[1]['=.id']
        response = apiros.talk(["/interface/vlan/remove",
                            "=.id="+id_given,
                            ])
    except:
        pass
    return response
def update_interface(mikrotik_ip, user, password,data,newdata):
    #sys.argv[1]
    s = None
    print ('update_interface')
    for res in socket.getaddrinfo(mikrotik_ip, "8728", socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
             s = socket.socket(af, socktype, proto)
        except (socket.error, msg):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error, msg):
            s.close()
            s = None
            continue
        break
    if s is None:
        # print('could not open socket')
        sys.exit(1)
    results = []
    #print ('time')
    s.settimeout(1)
    apiros = ApiRos(s)
    apiros.login(user, password)
    alias = "\""+data['alias']+"\""
    reply, _ = apiros.talk(["/interface/vlan/print",
                            "=from="+alias,
                            "=.proplist=.id",
                            ])
    id_given = reply[1]['=.id']
    list_command = ["/interface/vlan/set",
                    "=.id="+id_given,
                    ]
    if newdata['alias']:
        alias = newdata['alias']
        list_command.append("=name="+alias)
    if newdata['id']:
        vlan_id = newdata['id']
        list_command.append("=vlan-id="+str(vlan_id))
    if newdata['description']:
        description = newdata['description']
        list_command.append("=comment="+description)
    response = apiros.talk(list_command)
    return response
================================================

File: models.py
================================================
import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.utils import timezone
from common.utils import timedelta_format
from common.models import BaseModel
class Device(BaseModel):
    uuid = models.UUIDField(db_index=True,
                            default=uuid.uuid4,
                            editable=settings.DEBUG)
    class Meta:
        abstract = True
class ModelDevice(BaseModel):
    model = models.CharField(max_length=80)
    brand = models.CharField(max_length=80, null=True, blank=True)
    def __str__(self):
        return self.model
    class Meta:
        ordering = ['-id']
class Radius(Device):
    alias = models.CharField(max_length=80, db_index=True)
    ip = models.CharField(max_length=15, db_index=True)
    mac_eth1 = models.CharField(max_length=17, db_index=True, null=True, blank=True)
    status = models.BooleanField(default=False)
    model = models.ForeignKey(ModelDevice,
                              on_delete=models.CASCADE)
    description = models.TextField()
    uptime = models.DateTimeField(null=True, blank=True)
    time_uptime = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        if self.ip:
            return f"{self.alias} {self.ip}"
        return self.alias
    def get_uptime(self):
        return self.uptime
    def set_status_offline(self):
        self.status = False
        self.save()
    def set_status_online(self):
        self.status = True
        self.save()
    @property
    def get_uptime_delta(self):
        try:
            if self.status:
                u = timezone.now() - self.uptime
                return timedelta_format(u)
            return None
        except Exception as e:
            print (e)
            return None
    def save(self, *args, **kwargs):
        super(Radius, self).save(*args, **kwargs)
    class Meta:
        ordering = ["alias"]
        unique_together = ("alias", "ip")
class RadiusConnection(BaseModel):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=30)
    radius = models.ForeignKey(Radius, blank=True, on_delete=models.CASCADE)
    connections = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.radius.alias
    def release_connection(self):
        if self.connections > 0:
            self.connections -= 1
            self.save()
    def connection_usage(self):
        self.connections += 1
        self.save()
    def get_ip(self):
        return self.radius.ip
    class Meta:
        ordering = ["username"]
class Mikrotik(Device):
    name = models.CharField(max_length=80,blank=True)
    alias = models.CharField(max_length=80, db_index=True)
    ip = models.CharField(max_length=15, db_index=True)
    mac_eth1 = models.CharField(max_length=17, db_index=True, null=True, blank=True)
    status = models.BooleanField(default=False)
    model = models.ForeignKey(ModelDevice,
                              on_delete=models.CASCADE)
    architecture = models.CharField(max_length=80,blank=True)
    description = models.TextField()
    firmware = models.CharField(max_length=100, null=True, blank=True)
    serial = models.CharField(max_length=80,blank=True)
    cpeutps = models.PositiveSmallIntegerField(default=0)
    cpeutp_active = models.PositiveSmallIntegerField(default=0)
    ram = models.CharField(max_length=10, null=True, blank=True)
    cpu = models.CharField(max_length=10, null=True, blank=True)
    storage = models.CharField(max_length=10, null=True, blank=True)
    temperature_cpu = models.CharField(max_length=10, null=True, blank=True)
    temperature = models.CharField(max_length=10, null=True, blank=True)
    voltage = models.PositiveSmallIntegerField(default=0)
    power_consumption = models.PositiveSmallIntegerField(default=0)
    uptime = models.DateTimeField(null=True, blank=True)
    time_uptime = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(max_length=300,null=True)
    radius = models.ForeignKey(Radius, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        if self.ip:
            return f"{self.alias} {self.ip}"
        return self.alias
    def get_uptime(self):
        return self.uptime
    def set_status_offline(self):
        self.status = False
        self.save()
    def set_status_online(self):
        self.status = True
        self.save()
    @property
    def get_uptime_delta(self):
        try:
            if self.status:
                u = timezone.now() - self.uptime
                return timedelta_format(u)
            return None
        except Exception as e:
            print (e)
            return None
    @property
    def get_uptime_date(self):
        return self.uptime.strftime('Desde %d/%m/%Y a las %H:%M')
    @property
    def get_radius_alias(self):
        if self.radius:
            return self.radius.alias
        else:
            return None
    def save(self, *args, **kwargs):
        super(Mikrotik, self).save(*args, **kwargs)
    class Meta:
        ordering = ["alias"]
        unique_together = ("alias", "ip")
class MikrotikConnection(BaseModel):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=30)
    mikrotik = models.ForeignKey(Mikrotik, blank=True, on_delete=models.CASCADE)
    connections = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.mikrotik.alias
    def release_connection(self):
        if self.connections > 0:
            self.connections -= 1
            self.save()
    def connection_usage(self):
        self.connections += 1
        self.save()
    def get_ip(self):
        return self.mikrotik.ip
    class Meta:
        ordering = ["username"]
class CpeUtp(Device):
    alias = models.CharField(max_length=80, db_index=True, null=True, blank=True)
    serial = models.CharField(max_length=30, db_index=True)
    nodo_utp = models.ForeignKey(Mikrotik, on_delete=models.CASCADE)
    description = models.TextField()
    model = models.ForeignKey(ModelDevice, null=True, blank=True,
                              on_delete=models.CASCADE)
    service_number = models.PositiveSmallIntegerField(null=True, blank=True)
    service_number_verified = models.BooleanField(default=False)
    # Quitada la posibilidad de que status sea NULL en este campo para evitar error en el serializer
    status = models.BooleanField(default=False, blank=True)
    uptime = models.DateTimeField(null=True, blank=True)
    mac = models.CharField(max_length=17, db_index=True, null=True, blank=True)
    active_mac = models.CharField(max_length=17, db_index=True, null=True, blank=True)
    ip = models.GenericIPAddressField(protocol="IPv4", db_index=True, null=True, blank=True)
    active_ip = models.GenericIPAddressField(protocol="IPv4", db_index=True, null=True, blank=True)
    firmware = models.CharField(max_length=100, null=True, blank=True)
    download_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)
    upload_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)    
    def delete_this(self):
        self.delete()
    def __str__(self):
        if self.alias:
            return self.alias
        return self.serial
    def set_status_offline(self):
        self.status = False
        self.save()
    @property
    def get_uptime_delta(self):
        try:
            if self.status:
                u = timezone.now() - self.uptime
                return timedelta_format(u)
            return None
        except Exception as e:
            print (e)
            return None
    @property
    def get_uptime_date(self):
        return self.uptime.strftime('Desde %d/%m/%Y a las %H:%M')
    def get_mac(self):
        return self.mac
    class Meta:
        ordering = ["serial"]
        unique_together = (("alias", "nodo_utp"),)
class Operator(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-name"]
class SystemProfile(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    limitation_name = models.CharField(max_length=50)
    download_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)
    upload_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)    
    provisioning_available = models.BooleanField(default=False)
    description = models.TextField(blank=True,default="")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-name"]
class ProfileUTP(BaseModel):
    name = models.CharField(max_length=50)
    limitation_name = models.CharField(max_length=50)
    download_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)
    upload_speed = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=True, blank=True)    
    provisioning_available = models.BooleanField(default=False)
    description = models.TextField(blank=True,default="")
    radius = models.ForeignKey(Radius, on_delete=models.CASCADE)
    system_profile = models.ForeignKey(SystemProfile, on_delete = models.SET_NULL,
                                     null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-name"]
class TypePLAN(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-name"]
class Plan(BaseModel):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type_plan = models.ForeignKey(TypePLAN, on_delete=models.CASCADE)
    aggregation_rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(4096)], null=True, blank=True)   
    profile_name = models.ForeignKey(SystemProfile, on_delete=models.CASCADE)
    matrix_plan = models.PositiveSmallIntegerField()                                       
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    class Meta:
        ordering = ["-matrix_plan"]
================================================

File: __init__.py
================================================
#from decimal import Decimal
from dynamic_preferences.types import BooleanPreference, StringPreference,\
    DecimalPreference, IntegerPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
#from dynamic_preferences.users.registries import user_preferences_registry
# we create some section objects to link related preferences together
general = Section('general')
@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = 'title'
    default = 'Mikrotik'
    required = False
# @global_preferences_registry.register
# class URLFeedback(StringPreference):
#     name = 'url_slack_feedback'
#     default = "https://hooks.slack.com/services/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"
#     required = False
================================================

File: serializers.py
================================================
import uuid
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.core.management import call_command
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework.utils import model_meta
from common.serializers import QueryFieldsMixin
from .models import Mikrotik, ModelDevice, MikrotikConnection,CpeUtp, Operator, ProfileUTP, TypePLAN, \
                    Plan, Radius, RadiusConnection, SystemProfile
from utp.mikrotik import get_mikrotik_info,get_mikrotik_leases,create_radius_profile,get_radius_profile
from dashboard.utils import LOG
from dashboard.models import TaskModel    
__all__ = ['MikrotikSerializer', 'ModelDeviceSerializer','CPEUTPSerializer',
            'OperatorSerializer','ProfileUTPSerializer','TypePLANSerializer',
            'PlanSerializer','RadiusSerializer','ProvisioningSerializer']
_l = LOG()
class ModelDeviceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ModelDevice
        fields = ('id', 'model','brand')
class ListNodeField(serializers.Field):
    def to_internal_value(self, obj):
        if isinstance(obj, list):
            return obj[0]
        else:
            msg = self.error_messages['invalid']
            raise ValidationError(msg)
class RadiusSerializer(QueryFieldsMixin, HyperlinkedModelSerializer):
    model = ModelDeviceSerializer(read_only=True)
    user = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = self.context['request'].user
        username = validated_data.pop('user')
        password = validated_data.pop('password')
        ip = validated_data.get('ip')
        id_data = uuid.uuid4()
        try:
            info = get_mikrotik_info(ip,username,password)
            if (not isinstance(info,dict)) or info=={}:
                if info == {}:
                    msg = 'Falló la conexión vía API. Por favor revise que el username soporte API, \
                            y que el IP Services permita la conexión desde las IP 190.113.247.215 y 190.113.247.219.'
                else:
                    msg = info
                raise Exception('{}'.format(msg))
            model_name = info['model']
            try:
                model = ModelDevice.objects.get(model=model_name)
            except ModelDevice.DoesNotExist:
                model = ModelDevice.objects.create(model=model_name,id_data=id_data,brand=info['brand'])
                _l.MODEL.ADD(by_representation=user, id_value=model.id,
                description=f'Modelo creado por crear RADIUS', entity_representation=repr(model))
            except Exception as e:
                print ("Error getmodel serializer RADIUS")
                print (e)
                raise serializers.ValidationError({
                  "error" : "No se puede obtener el modelo del dispositivo",
                  "detail" : str(e)
                })                      
            validated_data['model'] = model
            # If week
            if "w" in info['uptime']:
                weeks,rest = info['uptime'].split('w')
                weeks=int(weeks)
            else:
                weeks=0
                rest = info['uptime']
            # If day
            if "d" in rest:
                days,rest = rest.split('d')
                days=int(days)
            else:
                days=0
            # If hour
            if "h" in rest:
                hours,rest = rest.split('h')
                hours=int(hours)
            else:
                hours=0
            # If minute
            if "m" in rest:
                minutes,rest = rest.split('m')
                minutes=int(minutes)
            else:
                minutes=0
            # If seconds
            if "s" in rest:
                secs,rest = rest.split('s')
                secs=int(secs)
            else:
                secs=0
            # Get uptime with retrieved values
            value_uptime = timezone.now() - timedelta(weeks=weeks, days=days, hours=hours,
                                                       minutes=minutes, seconds=secs)
            obj = Radius.objects.create(**validated_data)
            print("here")
            obj.status = True  
            obj.uptime = value_uptime
            obj.time_uptime = timezone.now()
            obj.ip = ip
            obj.description = info['description']
            obj.name = ""
            obj.save()
            _l.RADIUS.ADD(by_representation=user, id_value=obj.uuid,
                description=f'Nuevo RADIUS', entity_representation=repr(obj))
            RadiusConnection.objects.create(radius=obj,
                                         username=username,
                                         password=password,
                                         id_data=id_data)
            """ task """             
            TaskModel.objects.create(
              id_obj = obj.id,
              model_obj = 'radius',
              uuid = obj.uuid,
              name = 'task_new_radius',
              id_data = id_data
            )
            return obj
        except Exception as e:
            _l.RADIUS.ADD(by_representation=user, id_value=ip, id_field='ip',
            description=f'fallo crear: {e}')
            raise serializers.ValidationError({
              "error" : f'fallo crear: {e}',
              "detail" : str(e)
            })
    class Meta:
        model = Radius
        fields = ('ip','alias','model', 'description','uptime','id',
                  'user', 'password','uuid','status','mac_eth1',
                  'get_uptime_delta')
class MikrotikSerializer(QueryFieldsMixin, HyperlinkedModelSerializer):
    model = ModelDeviceSerializer(read_only=True)
    radius = serializers.ModelField(model_field=Radius()._meta.get_field('id'))
    user = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    def get_task_in_progress(self, obj):
        pass
    def validate(self, attrs):
        if self.context['view'].action == 'partial_update' or\
          self.context['view'].action == 'update':
          return super().validate(attrs)
        import ipaddress
        try:
            ipaddress.ip_address(attrs['ip'])
        except ValueError as e:
            _err = {'error':'La ip es invalida'}
            raise serializers.ValidationError(_err)
        return super().validate(attrs)
    def create(self, validated_data):
        user = self.context['request'].user
        username = validated_data.pop('user')
        password = validated_data.pop('password')
        ip = validated_data.get('ip')
        id_data = uuid.uuid4()
        radiusid = validated_data.pop('radius')
        try:
            try:
                radius = Radius.objects.get(id=radiusid)
            except:
                radius = ""
            print(radius)
            info = get_mikrotik_info(ip,username,password)
            if (not isinstance(info,dict)) or info=={}:
                if info == {}:
                    msg = 'Falló la conexión vía API. Por favor revise que el username soporte API, \
                            y que el IP Services permita la conexión desde las IP 190.113.247.215 y 190.113.247.219.'
                else:
                    msg = info
                raise Exception('{}'.format(msg))
            model_name = info['model']
            try:
                model = ModelDevice.objects.get(model=model_name)
            except ModelDevice.DoesNotExist:
                model = ModelDevice.objects.create(model=model_name,id_data=id_data,brand=info['brand'])
                _l.MODEL.ADD(by_representation=user, id_value=model.id,
                description=f'Modelo creado por crear Mikrotik', entity_representation=repr(model))
            except Exception as e:
                print ("Error getmodel serializer Mikrotik")
                print (e)
                raise serializers.ValidationError({
                  "error" : "No se puede obtener el modelo del dispositivo",
                  "detail" : str(e)
                })                      
            validated_data['model'] = model
            # If week
            if "w" in info['uptime']:
                weeks,rest = info['uptime'].split('w')
                weeks=int(weeks)
            else:
                weeks=0
                rest = info['uptime']
            # If day
            if "d" in rest:
                days,rest = rest.split('d')
                days=int(days)
            else:
                days=0
            # If hour
            if "h" in rest:
                hours,rest = rest.split('h')
                hours=int(hours)
            else:
                hours=0
            # If minute
            if "m" in rest:
                minutes,rest = rest.split('m')
                minutes=int(minutes)
            else:
                minutes=0
            # If seconds
            if "s" in rest:
                secs,rest = rest.split('s')
                secs=int(secs)
            else:
                secs=0
            # Get uptime with retrieved values
            value_uptime = timezone.now() - timedelta(weeks=weeks, days=days, hours=hours,
                                                       minutes=minutes, seconds=secs)
            obj = Mikrotik.objects.create(**validated_data)
            if radius != "":
                obj.radius = radius
            obj.status = True
            obj.firmware = info['firmware']            
            obj.uptime = value_uptime
            obj.time_uptime = timezone.now()
            obj.id_data = id_data
            obj.ip = ip
            obj.description = info['description']
            obj.name = ""
            obj.architecture = info['architecture']
            obj.serial = info['serial']
            obj.cpu = str(info['cpu'])
            obj.ram = str(info['ram'])
            obj.storage = str(info['hdd'])
            if info['temperature']!='':
                obj.temperature = info['temperature']
            if info['voltage']!='':
                obj.voltage = round(float(info['voltage']),0)
            if info['temperature_cpu']!='':
                obj.temperature_cpu = info['temperature_cpu']
            if info['power_consumption']!='':
                obj.power_consumption = round(float(info['power_consumption']),0)
            obj.save()
            _l.MIKROTIK.ADD(by_representation=user, id_value=obj.uuid,
                description=f'Nuevo Mikrotik', entity_representation=repr(obj))
            MikrotikConnection.objects.create(mikrotik=obj,
                                         username=username,
                                         password=password,
                                         id_data=id_data)
            """ task """             
            TaskModel.objects.create(
              id_obj = obj.id,
              model_obj = 'mikrotik',
              uuid = obj.uuid,
              name = 'task_new_mikrotik',
              id_data = id_data
            )
            if 'leases' in info.keys():
                listleases = info['leases']
                for i in listleases:
                    try:
                        print(i)
                        model_name = i['model']
                        try:
                            model = ModelDevice.objects.get(model=model_name)
                        except ModelDevice.DoesNotExist:
                            model = ModelDevice.objects.create(model=model_name,id_data=id_data,brand=i['brand'])
                            _l.MODEL.ADD(by_representation=user, id_value=model.id,
                            description=f'Modelo creado por crear una CPE al crear un Mikrotikik',
                            entity_representation=repr(model))
                        cpe = CpeUtp.objects.create(status=i['status'],
                                                    description=i['description'],
                                                    mac=i['mac'],
                                                    active_mac=i['active_mac'],
                                                    nodo_utp=obj,
                                                    model=model,
                                                    ip=i['ip'],
                                                    active_ip=i['active_ip'],
                                                    firmware=i['firmware'],
                                                    alias=i['description']
                                                    )
                        if i['uptime'] != None:
                            # If week
                            if "w" in i['uptime']:
                                weeks,rest = i['uptime'].split('w')
                                weeks=int(weeks)
                            else:
                                weeks=0
                                rest = i['uptime']
                            # If day
                            if "d" in rest:
                                days,rest = rest.split('d')
                                days=int(days)
                            else:
                                days=0
                            # If hour
                            if "h" in rest:
                                hours,rest = rest.split('h')
                                hours=int(hours)
                            else:
                                hours=0
                            # If minute
                            if "m" in rest:
                                minutes,rest = rest.split('m')
                                minutes=int(minutes)
                            else:
                                minutes=0
                            # If seconds
                            if "s" in rest:
                                secs,rest = rest.split('s')
                                secs=int(secs)
                            else:
                                secs=0
                            # Get uptime with retrieved values
                            value_uptime = timezone.now() - timedelta(weeks=weeks, days=days, hours=hours,
                                                                       minutes=minutes, seconds=secs)
                            print(value_uptime)
                            cpe.uptime = value_uptime
                            cpe.save()
                        print(1)
                    except:
                        cpe = CpeUtp.objects.create(status=i['status'],
                                                    description=i['description'],
                                                    mac=i['mac'],
                                                    active_mac=i['active_mac'],
                                                    nodo_utp=obj,
                                                    ip=i['ip'],
                                                    active_ip=i['active_ip'],
                                                    alias=i['description']
                                                    )
                        print(2)
                    cpe.service_number=i['service_number']
                    if 'download_speed' in i.keys():
                        cpe.download_speed=i['download_speed']
                    if 'upload_speed' in i.keys():
                        cpe.upload_speed=i['upload_speed']
                    cpe.save()
                    _l.CPEUTP.ADD(by_representation=user, id_value=cpe.id,
                        description=f'CPE creado al crear Mikrotik', entity_representation=repr(cpe))
                    obj.cpeutps = obj.cpeutps + 1
                    if cpe.status == True:
                        obj.cpeutp_active = obj.cpeutp_active + 1
                obj.save()
            return obj
        except Exception as e:
            _l.MIKROTIK.ADD(by_representation=user, id_value=ip, id_field='ip',
            description=f'fallo crear: {e}')
            raise serializers.ValidationError({
              "error" : f'fallo crear: {e}',
              "detail" : str(e)
            })
    class Meta:
        model = Mikrotik
        fields = ('ip','alias','model', 'description', 'cpeutps','cpeutp_active','uptime','id',
                  'user', 'password','uuid','name','status','firmware','architecture',
                  'cpu','ram','serial','mac_eth1','storage','get_uptime_delta','get_uptime_date',
                  'temperature','temperature_cpu','voltage','power_consumption','comment',
                  'radius','get_radius_alias'
                  )
class CPEUTPSerializer(QueryFieldsMixin, HyperlinkedModelSerializer):
    nodo_utp = serializers.CharField(read_only=True, source='nodo_utp.alias')
    model = ModelDeviceSerializer()
    # Comentada la siguiente línea por error "NoneType has no attribute 'model'"
    #model = serializers.CharField(source='model.model')
    class Meta:
        model = CpeUtp
        fields = ('serial','model','description','service_number',
                  'nodo_utp','uuid','alias','status','uptime','mac','ip',
                  'firmware','nodo_utp','active_mac','active_ip',
                  'get_uptime_delta','get_uptime_date')
def extract_elem_from_list(givenlist,index):
    """
    Extracts an element from a list given its index in said list.
    This method is used in main_updatecpeutp.
    """
    if index == 0:
        return givenlist[1:]
    elif index==len(givenlist)-1:
        return givenlist[:len(givenlist)-1]
    else:
        return givenlist[:index]+givenlist[index+1:]
def update_cpeutp(cpeutp,i,obj,user):
    """
    This method supports the main for updating cpe.
    Simply grabs a dict and updates de writable fields of a CpeUtp instance.
    """
    boolean = True
    if i['service_number']!=cpeutp.service_number:
        boolean = False
        cpeutp.service_number=i['service_number']
    if i['status']!=cpeutp.status:
        boolean = False
        cpeutp.status=i['status']
        if cpeutp.status == True:
            obj.cpeutp_active += 1
            obj.save()
            _l.MIKROTIK.ADD(by_representation=user, id_value=obj.id,
                description=f'Cambiado status de un CPE al actualizar lista CPEUTP del nodo',
                entity_representation=repr(obj))
        else:
            if obj.cpeutp_active != 0:
                obj.cpeutp_active -= 1
                obj.save()
                _l.MIKROTIK.ADD(by_representation=user, id_value=obj.id,
                    description=f'Cambiado status de un CPE al actualizar lista CPEUTP del nodo',
                    entity_representation=repr(obj))
    if i['description']!=cpeutp.description:
        boolean = False
        cpeutp.description=i['description']
    if i['mac']!=cpeutp.mac:
        boolean = False
        cpeutp.mac=i['mac']
    if i['active_mac']!=cpeutp.active_mac:
        boolean = False
        cpeutp.active_mac=i['active_mac']
    if "model" in i.keys():
        boolean = False
        model_name=i['model']
        try:
            model = ModelDevice.objects.get(model=model_name)
        except ModelDevice.DoesNotExist:
            model = ModelDevice.objects.create(model=model_name,id_data=obj.uuid,brand=i['brand'])
            _l.MODEL.ADD(by_representation=user, id_value=model.id,
            description=f'Modelo creado por crear una CPE al actualizar la lista CPEUTP de un Mikrotikik',
            entity_representation=repr(model))
        if cpeutp.model!=model:
            boolean=False
            cpeutp.model=model
    else:
        if cpeutp.model:
            boolean = False
            cpeutp.model=None
    if i['ip']!=cpeutp.ip:
        boolean = False
        cpeutp.ip=i['ip']
    if i['active_ip']!=cpeutp.active_ip:
        boolean = False
        cpeutp.active_ip=i['active_ip']
    if "firmware" in i.keys() and i['firmware']!=cpeutp.firmware:
        boolean = False
        cpeutp.firmware=i['firmware']
    if "uptime" in i.keys() and i['uptime'] != None:
        # If week
        if "w" in i['uptime']:
            weeks,rest = i['uptime'].split('w')
            weeks=int(weeks)
        else:
            weeks=0
            rest = i['uptime']
        # If day
        if "d" in rest:
            days,rest = rest.split('d')
            days=int(days)
        else:
            days=0
        # If hour
        if "h" in rest:
            hours,rest = rest.split('h')
            hours=int(hours)
        else:
            hours=0
        # If minute
        if "m" in rest:
            minutes,rest = rest.split('m')
            minutes=int(minutes)
        else:
            minutes=0
        # If seconds
        if "s" in rest:
            secs,rest = rest.split('s')
            secs=int(secs)
        else:
            secs=0
        # Get uptime with retrieved values
        value_uptime = timezone.now() - timedelta(weeks=weeks, days=days, hours=hours,
                                                   minutes=minutes, seconds=secs)
        if value_uptime!=cpeutp.uptime:
            boolean = False
            cpeutp.uptime = value_uptime
    if 'download_speed' in i.keys():
        cpeutp.download_speed=i['download_speed']
        boolean=False
    if 'upload_speed' in i.keys():
        cpeutp.upload_speed=i['upload_speed']
        boolean=False
    if not boolean:
        cpeutp.save()
        _l.CPEUTP.ADD(by_representation=user, id_value=cpeutp.id,
                        description=f'CPE actualizado al actualizar lista CPEUTP de Mikrotik', entity_representation=repr(cpeutp))
def main_updatecpeutp(utp_uuid):
    """
    This is a method used in order to update the cpelist of a
    given utp node
    """
    # Get utp node
    elem = Mikrotik.objects.get(uuid=utp_uuid)
    # Get connections details for this device
    connection_data = MikrotikConnection.objects.get(mikrotik=elem)
    user = connection_data.username
    _l.MIKROTIK.ADD(by_representation=user, id_value=elem.uuid,
                description=f'Petición para actualizar lista CPEUTP de Mikrotik', entity_representation=repr(elem))
    obj = elem
    try:
        # Get device leases
        leases = get_mikrotik_leases(elem.ip,user,connection_data.password)
        if isinstance(leases,str):
            raise Exception("Error: "+leases)
        # Get cpes currently associated to utp node
        saved_cpeutp = list(CpeUtp.objects.filter(nodo_utp=elem))
        # Compare the two lists
        temp = []
        while len(leases)!=0 and len(saved_cpeutp)!=0:
            current = leases.pop()
            temp.append(current)
            print("This is current element from leases")
            print(current)
            for i in range(len(saved_cpeutp)):
                if current['ip'] == saved_cpeutp[i].ip and current['mac'] == saved_cpeutp[i].mac:
                    print("found match in saved cpeutp,updating")
                    update_cpeutp(saved_cpeutp[i],current,elem,user)
                    saved_cpeutp = extract_elem_from_list(saved_cpeutp,i)
                    print("This is the new list")
                    print(saved_cpeutp)
                    temp.pop()
                    break
        if len(leases)==0:
            leases = temp
        print(leases)
        if len(leases)!= 0 and len(saved_cpeutp)==0: # There is at least one cpe that needs to be added
            print("Need to add new cpe(s) to list")
            for i in leases:
                try:
                    print(i)
                    model_name = i['model']
                    try:
                        model = ModelDevice.objects.get(model=model_name)
                    except ModelDevice.DoesNotExist:
                        model = ModelDevice.objects.create(model=model_name,id_data=obj.uuid,brand=i['brand'])
                        _l.MODEL.ADD(by_representation=user, id_value=model.id,
                        description=f'Modelo creado por crear una CPE al actualizar la lista CPEUTP de un Mikrotikik',
                        entity_representation=repr(model))
                    cpe = CpeUtp.objects.create(status=i['status'],
                                                description=i['description'],
                                                mac=i['mac'],
                                                active_mac=i['active_mac'],
                                                nodo_utp=obj,
                                                model=model,
                                                ip=i['ip'],
                                                active_ip=i['active_ip'],
                                                firmware=i['firmware'],
                                                alias=i['description']
                                                )
                    if i['uptime'] != None:
                        # If week
                        if "w" in i['uptime']:
                            weeks,rest = i['uptime'].split('w')
                            weeks=int(weeks)
                        else:
                            weeks=0
                            rest = i['uptime']
                        # If day
                        if "d" in rest:
                            days,rest = rest.split('d')
                            days=int(days)
                        else:
                            days=0
                        # If hour
                        if "h" in rest:
                            hours,rest = rest.split('h')
                            hours=int(hours)
                        else:
                            hours=0
                        # If minute
                        if "m" in rest:
                            minutes,rest = rest.split('m')
                            minutes=int(minutes)
                        else:
                            minutes=0
                        # If seconds
                        if "s" in rest:
                            secs,rest = rest.split('s')
                            secs=int(secs)
                        else:
                            secs=0
                        # Get uptime with retrieved values
                        value_uptime = timezone.now() - timedelta(weeks=weeks, days=days, hours=hours,
                                                                   minutes=minutes, seconds=secs)
                        print(value_uptime)
                        cpe.uptime = value_uptime
                        cpe.save()
                    print(1)
                except:
                    cpe = CpeUtp.objects.create(status=i['status'],
                                                description=i['description'],
                                                mac=i['mac'],
                                                active_mac=i['active_mac'],
                                                nodo_utp=obj,
                                                ip=i['ip'],
                                                active_ip=i['active_ip'],
                                                alias=i['description']
                                                )
                    print(2)
                cpe.service_number=i['service_number']
                if 'download_speed' in i.keys():
                    cpe.download_speed=i['download_speed']
                if 'upload_speed' in i.keys():
                    cpe.upload_speed=i['upload_speed']
                cpe.save()
                print(cpe)
                _l.CPEUTP.ADD(by_representation=user, id_value=cpe.id,
                    description=f'CPE creado al actualizar lista CPEUTPE de un Mikrotik', entity_representation=repr(cpe))
                obj.cpeutps+=1
                if cpe.status == True:
                    obj.cpeutp_active+=1
                obj.save()
        elif len(leases)== 0 and len(saved_cpeutp)!=0: # There is a cpe that needs to be deleted
            print("We need to delete cpeutp(s)")
            for i in saved_cpeutp:
                print("Deleting this element")
                print(i)
                print(i.ip)
                i.delete()
                _l.CPEUTP.ADD(by_representation=user, id_value=i.id,
                        description=f'CPE borrado al actualizar lista CPEUTP de Mikrotik', 
                        entity_representation=repr(i))
                if i.status==True and obj.cpeutp_active != 0:
                    obj.cpeutp_active = obj.cpeutp_active - 1
                if obj.cpeutps != 0:
                    obj.cpeutps = obj.cpeutps - 1
                obj.save()
                _l.MIKROTIK.ADD(by_representation=user, id_value=obj.id,
                    description=f'Eliminado CPE al actualizar lista CPEUTP del nodo',
                    entity_representation=repr(obj))
        else: # All other have already been updated, do nothing
            print("All have been updated")
            pass
        _l.MIKROTIK.ADD(by_representation=user, id_value=elem.uuid,
                description=f'Actualizada lista CPEUTP de Mikrotik', entity_representation=repr(elem))
    except Exception as e:
        _l.MIKROTIK.ADD(by_representation=user, id_value=utp_uuid, id_field='uuid',
        description=f'fallo actualizar lista cpeutp: {e}')
        raise serializers.ValidationError({
          "error" : f'fallo actualizar lista cpeutp: {e}',
          "detail" : str(e)
        })
class OperatorSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id', 'name', 'code')
class ProfileUTPSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        profile_name = validated_data.pop('name')
        limitation_name = validated_data.pop('limitation_name')
        download_speed = validated_data.pop('download_speed')
        upload_speed = validated_data.pop('upload_speed')
        radius = validated_data.pop('radius')
        try:
            radius_conn = RadiusConnection.objects.get(radius__id=radius.id)
            data = {
                    "profile" : profile_name,
                    "limitation" : limitation_name,
                    "download_speed" : download_speed,
                    "upload_speed" : upload_speed
            }
            info = create_radius_profile(radius_conn.radius.ip,radius_conn.username,
                                            radius_conn.password,data)
            if not isinstance(info,dict):
                msg = 'Falló la conexión vía API. Por favor revise que el username soporte API, \
                        y que el IP Services permita la conexión desde las IP 190.113.247.215 y \
                        190.113.247.219.'
                if info!="":
                    msg=msg+"\n"+info
                raise Exception('{}'.format(msg))
            obj = ProfileUTP.objects.create(name=profile_name,limitation_name=limitation_name,
                                            download_speed=download_speed,upload_speed=upload_speed,
                                            radius=radius)
            obj.save()
            _l.PROFILEUTP.ADD(by_representation=user, id_value=obj.id,
                description=f'Nuevo Profile', entity_representation=repr(obj))
            return obj
        except Exception as e:
            _l.PROFILEUTP.ADD(by_representation=user, id_value=radius, id_field='id',
            description=f'fallo crear profile: {e}')
            raise serializers.ValidationError({
              "error" : f'fallo crear profile: {e}',
              "detail" : str(e)
            })
    class Meta:
        model = ProfileUTP
        fields = ('id', 'name','download_speed','upload_speed','provisioning_available',
                    'limitation_name','description','radius','system_profile')
class SystemProfileSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SystemProfile
        fields = ('id', 'name','download_speed','upload_speed','provisioning_available',
                    'limitation_name','description')
def update_profileutp(profile,i):
    """
    This method supports the main for updating cpe.
    Simply grabs a dict and updates de writable fields of a ProfileUTP instance.
    """
    boolean = True
    if i['name']!=profile.name:
        boolean = False
        profile.name=i['name']
    if i['limitation_name']!=profile.limitation_name:
        boolean = False
        profile.limitation_name=i['limitation_name']
    if "download_speed" in i.keys() and round(int(i['download_speed'])/1000000,0)!=profile.download_speed:
        boolean = False
        profile.download_speed=round(int(i['download_speed'])/1000000,0)
    if "upload_speed" in i.keys() and round(int(i['upload_speed'])/1000000,0)!=profile.upload_speed:
        boolean = False
        profile.upload_speed=round(int(i['upload_speed'])/1000000,0)
    if not boolean:
        profile.save()
        _l.PROFILEUTP.ADD(by_representation=user, id_value=profile.id,
                description=f'Actualizado profile al actualizar lista Profile de RADIUS',
                entity_representation=repr(profile))
def main_updateprofileutp(id_given):
    """
    This is a method used in order to update the profile list of a
    given RADIUS with the information in the device
    """
    # Get RADIUS
    elem = Radius.objects.get(uuid=id_given)
    # Get connections details for this device
    connection_data = RadiusConnection.objects.get(radius=elem)
    user = connection_data.username
    _l.RADIUS.ADD(by_representation=user, id_value=elem.id,
                description=f'Petición para actualizar lista Profile de RADIUS',
                entity_representation=repr(elem))
    try:
        # Get device profiles
        profiles = get_radius_profile(elem.ip,connection_data.username,connection_data.password)
        if not isinstance(profiles,list):
            raise Exception("Error: "+profiles)
        # Get cpes currently associated to utp node
        saved_profile = list(ProfileUTP.objects.filter(radius=elem))
        # Compare the two lists
        temp = []
        while len(profiles)!=0 and len(saved_profile)!=0:
            current = profiles.pop()
            temp.append(current)
            print("This is current element from profile list in device")
            print(current)
            for i in range(len(saved_profile)):
                if (current['name'] == saved_profile[i].name and 
                    current['limitation_name']==saved_profile[i].limitation_name):
                    print("found match in saved profile,updating")
                    update_profileutp(saved_profile[i],current)
                    saved_profile = extract_elem_from_list(saved_profile,i)
                    print("This is the new list")
                    print(saved_profile)
                    temp.pop()
                    break
        if len(profiles)==0:
            profiles = temp
        print(profiles)
        if len(profiles)!= 0 and len(saved_profile)==0: # There is at least one that needs to be added
            print("Need to add new profile(s) to list")
            radius = elem
            for i in profiles:
                print(i)
                try:       
                    if "download_speed" in i.keys():
                        ds=round(int(i['download_speed'])/1000000,0)
                    else:
                        ds=None
                    if "upload_speed" in i.keys():
                        up=round(int(i['upload_speed'])/1000000,0)
                    else:
                        up=None
                    obj = ProfileUTP.objects.create(name=i['name'],
                                                    limitation_name=i['limitation_name'],
                                                    download_speed=ds,
                                                    upload_speed=up,
                                                    radius=radius)
                    obj.save()
                    _l.PROFILEUTP.ADD(by_representation=user, id_value=obj.id,
                        description=f'Nuevo Profile', entity_representation=repr(obj))
                except Exception as e:
                    _l.PROFILEUTP.ADD(by_representation=user, id_value=id_given, id_field='uuid',
                    description=f'fallo crear profile: {e}')
                    raise serializers.ValidationError({
                      "error" : f'fallo crear profile: {e}',
                      "detail" : str(e)
                    })
        elif len(profiles)== 0 and len(saved_profile)!=0: # There is a cpe that needs to be deleted
            print("We need to delete profile(s)")
            for i in saved_profile:
                print("Deleting this element")
                print(i)
                print(i.name)
                i.delete()
                _l.PROFILEUTP.ADD(by_representation=user, id_value=i.id,
                description=f'Borrado profile al actualizar lista Profile de RADIUS',
                entity_representation=repr(i))
        else: # All other have already been updated, do nothing
            print("All have been updated")
            pass
        _l.RADIUS.ADD(by_representation=user, id_value=elem.uuid,
            description=f'Actualizada lista Profile de RADIUS', entity_representation=repr(elem))
    except Exception as e:
        _l.RADIUS.ADD(by_representation=user, id_value=id_given, id_field='uuid',
        description=f'fallo actualizar lista profile: {e}')
        raise serializers.ValidationError({
          "error" : f'fallo actualizar lista profile: {e}',
          "detail" : str(e)
        })
class TypePLANSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = TypePLAN
        fields = ('id', 'name',)
class PlanSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id','operator','name','type_plan',
                  'aggregation_rate','profile_name','matrix_plan')   
class ProvisioningSerializer(QueryFieldsMixin, serializers.Serializer):
    mik = serializers.CharField()
    def create(self, validated_data):
        return validated_data
================================================

File: tests.py
================================================
from django.test import TestCase
# Create your tests here.
================================================

File: urls.py
================================================
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'utp', UTPViewSet, 'utp_api')
router.register(r'cpeutp', CpeUtpViewSet, 'cpeutp_api')
router.register(r'operator', OperatorViewSet, 'operator_api')
router.register(r'profileutp', ProfileViewSet, 'profile_utp_api')
router.register(r'system_profileutp', SystemProfileViewSet, 'system_profile_utp_api')
router.register(r'type_plan', TypePLANViewSet, 'type_plan_api')
router.register(r'plan', PlanViewSet, 'plan_api')
router.register(r'radius', RadiusViewSet, 'radiusutp_api')
================================================

File: views.py
================================================
#from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from dynamic_preferences.registries import global_preferences_registry
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.renderers import JSONRenderer
from .serializers import MikrotikSerializer, CPEUTPSerializer, \
                            OperatorSerializer, ProfileUTPSerializer, \
                            TypePLANSerializer, PlanSerializer, RadiusSerializer, \
                            main_updatecpeutp, main_updateprofileutp, \
                            SystemProfileSerializer
from .models import Mikrotik, MikrotikConnection,ModelDevice, CpeUtp, Operator, \
                    TypePLAN, Plan, ProfileUTP, Radius, RadiusConnection, SystemProfile
from .mikrotik import get_mikrotik_leases, delete_radius_profile_witheverything, \
                      delete_radius_profile_onlylink
from dashboard.utils import LOG
__all__ = ['UTPViewSet','CpeUtpViewSet','OperatorViewSet','ProfileViewSet',
            'TypePLANViewSet','PlanViewSet','RadiusViewSet','updateCpeUtp',
            'updateProfile','SystemProfileViewSet']
global_preferences = global_preferences_registry.manager()
_l = LOG()
class UTPViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Mikrotik
    retrieve:
        End point for Mikrotik
    update:
        End point for Mikrotik
    delete:
        End point for Mikrotik
    """
    queryset = Mikrotik.objects.all()
    serializer_class = MikrotikSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
    def get_queryset(self):
        for_alias = self.request.GET.get('alias', None)
        if for_alias:
            return Mikrotik.objects.filter(alias__icontains=for_alias)
        return Mikrotik.objects.filter()
class CpeUtpViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for CPEUTP
    retrieve:
        End point for CPEUTP
    update:
        End point for CPEUTP
    delete:
        End point for CPEUTP
    """
    queryset = CpeUtp.objects.all()
    serializer_class = CPEUTPSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
@csrf_exempt
def updateCpeUtp(request,version):
    if request.method=="POST" or request.method=="GET":
        url = request.get_full_path()
        utp_uuid = url.split("/").pop()
        try:
            main_updatecpeutp(utp_uuid)
            response = Response(
            {"detail": "ok"},
            content_type="application/json",
            status=status.HTTP_200_OK,
            )            
        except Exception as e:
            response = Response({**e.detail},
            content_type="application/json",
            status=status.HTTP_400_BAD_REQUEST,
            )  
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
@csrf_exempt
def updateProfile(request,version):
    if request.method=="POST" or request.method=="GET":
        url = request.get_full_path()
        radiusid = url.split("/").pop()
        main_updateprofileutp(radiusid)
        response = Response(
            {"detail": "ok"},
            content_type="application/json",
            status=status.HTTP_200_OK,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
    else:
        response = Response(
            {"detail": "ok"},
            content_type="application/json",
            status=status.HTTP_200_OK,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
class OperatorViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Operator
    retrieve:
        End point for Operator
    update: 
        End point for Operator
    delete:
        End point for Operator
    """
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
class SystemProfileViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Profile
    retrieve:
        End point for Profile
    update:
        End point for Profile
    delete:
        End point for Profile
    """
    queryset = SystemProfile.objects.all()
    serializer_class = SystemProfileSerializer 
class ProfileViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Profile
    retrieve:
        End point for Profile
    update:
        End point for Profile
    delete:
        End point for Profile
    """
    queryset = ProfileUTP.objects.all()
    serializer_class = ProfileUTPSerializer  
    def destroy(self, request, *args, **kwargs):
        url = request.path.split("/")
        id_given = url.pop()
        deleteall = False
        if id_given=="":
            id_given = url.pop()
        if "?all" in id_given:
            deleteall = True
            id_given = int(url.pop())
        else:
            id_given = int(id_given)
        elem = ProfileUTP.objects.get(id=id_given)
        radius = Radius.objects.get(id=elem.radius.id)
        connection_data = RadiusConnection.objects.get(radius=radius)
        user = connection_data.username
        _l.PROFILEUTP.ADD(by_representation=user, id_value=elem.id,
                description=f'Petición para borrar profile', entity_representation=repr(elem))
        data = {
            "profile" : elem.name,
            "limitation" : elem.limitation_name
        }
        try:
            if deleteall:
                _l.RADIUS.ADD(by_representation=user, id_value=radius.uuid,
                    description=f'Petición para borrar profile link de RADIUS incluyendo profile y limitation',
                    entity_representation=repr(radius))
                try:
                    result = delete_radius_profile_witheverything(radius.ip,user,connection_data.password,data)
                    if result != {}:
                        raise Exception("Error: "+str(result))
                except Exception as e:
                    _l.PROFILEUTP.ADD(by_representation=user, id_value=radius, id_field='id',
                    description=f'fallo borrar profile: {e}')
                    raise serializers.ValidationError({
                      "error" : f'fallo borrar profile: {e}',
                      "detail" : str(e)
                    })
            else:
                _l.RADIUS.ADD(by_representation=user, id_value=radius.uuid,
                    description=f'Petición para borrar profile link de RADIUS sin borrar profile y limitation',
                    entity_representation=repr(radius))
                try:
                    result = delete_radius_profile_onlylink(radius.ip,user,connection_data.password,data)
                    if result != {}:
                        raise Exception("Error: "+str(result))
                except Exception as e:
                    _l.PROFILEUTP.ADD(by_representation=user, id_value=radius, id_field='id',
                    description=f'fallo borrar profile: {e}')
                    raise serializers.ValidationError({
                      "error" : f'fallo borrar profile: {e}',
                      "detail" : str(e)
                    })
            return super(ProfileViewSet, self).destroy(request, *args, **kwargs) 
        except Exception as e:
            _l.PROFILEUTP.ADD(by_representation=user, id_value=radius, id_field='id',
                description=f'fallo borrar profile: {e}')
            raise serializers.ValidationError({
              "error" : f'fallo borrar profile: {e}',
              "detail" : str(e)
            })
class TypePLANViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for TypePLAN
    retrieve:
        End point for TypePLAN
    update:
        End point for TypePLAN
    delete:
        End point for TypePLAN
    """ 
    queryset = TypePLAN.objects.all()
    serializer_class = TypePLANSerializer   
class PlanViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Plan
    retrieve:
        End point for Plan
    update:
        End point for Plan
    delete:
        End point for Plan
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
class RadiusViewSet(viewsets.ModelViewSet):
    """
    create:
        End point for Radius
    retrieve:
        End point for Radius
    update:
        End point for Radius
    delete:
        End point for Radius
    """
    queryset = Radius.objects.all()
    serializer_class = RadiusSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
    def get_queryset(self):
        for_alias = self.request.GET.get('alias', None)
        if for_alias:
            return Radius.objects.filter(alias__icontains=for_alias)
        return Radius.objects.filter()