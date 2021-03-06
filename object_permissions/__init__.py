from django.db.models.signals import post_syncdb
from django.contrib.auth.models import  Permission
from django.contrib.auth.management import create_permissions

def create_all_permissions(**kwargs):
    create_permissions(**kwargs)
    for p in Permission.objects.filter(codename__startswith='change_'):
        res= Permission.objects.get_or_create(
            content_type=p.content_type,
            codename=p.codename.replace('change_','changeall_',1),
            name=p.name.replace('change','change ALL',1),
        )

post_syncdb.connect(create_all_permissions,weak=False)
