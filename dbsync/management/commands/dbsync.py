
from optparse import make_option
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connections, DEFAULT_DB_ALIAS

DEFAULT_DB_ALIAS

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-d', '--droptables',
            action='store_true',
            dest='droptables',
            default=False,
            help='Delete all tables before syncdb'),
                                             
        make_option('--noinput', action='store_false', dest='interactive', default=True,
            help='Tells Django to NOT prompt the user for input of any kind.'),
                                             
        make_option('--database', action='store', dest='database',
            default=DEFAULT_DB_ALIAS, help='Nominates a database to synchronize. '
                'Defaults to the "default" database.'),
                                             
        )
        
    help = "Allow to drop all tables before invoke django syncdb"

    def handle(self, *args, **options):
        
        if options.get('droptables') is True:
            
            connection = connections[options.get('database')]
            
            cursor = connection.cursor()
            
            cursor.execute('SET foreign_key_checks = 0')
            cursor.execute('show tables')
            
            for r in cursor.fetchall():
                print  "Dropping table %s" % r[0]
                cursor.execute('DROP TABLE ' + r[0])
                
            cursor.execute('SET foreign_key_checks = 0')
            
        call_command('syncdb', **options)