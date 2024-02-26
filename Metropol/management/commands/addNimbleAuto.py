# myapp/management/commands/mycommand.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from Metropol.views import getPendingCRB,addNimbleAuto,generateReportAuto

class Command(BaseCommand):
    help = 'My custom management command'

    def handle(self, *args, **options):
        addNimbleAuto()
        #generateReportAuto('CM950901008P7F')
        print(getPendingCRB())
