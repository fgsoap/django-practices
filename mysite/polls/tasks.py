from huey import crontab
from huey.contrib import djhuey as huey


@huey.periodic_task(crontab(hour='*/2'))
def clear_expired_sessions():
    from django.core.management import call_command
    return call_command('clearsessions')
