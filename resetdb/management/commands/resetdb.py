
from optparse import make_option
from django.core.management import call_command
from django.conf import settings
from django.core.management.commands.syncdb import Command as Syncdb
from django.db import connections

class Command(Syncdb):
    option_list = Syncdb.option_list + (make_option('-r', '--reset',
            action='store_true',
            dest='reset',
            default=False,
            help='Delete all tables before syncdb'),
            
            make_option( '--nosouth',
            action='store_false',
            dest='use_south',
            default=True,
            help='When using south, do not migrate after syndb'))

    def handle(self, *args, **options):
        
        
        if options.get('reset') is True:
            
            if settings.DEBUG is False and options.get('interactive') is True:
                response_valid = False
                while (not response_valid):
                    try:
                        response = raw_input("WARNING ! DEBUG = False, are you sure you want to drop all tables ? (y/n)")
                    except KeyboardInterrupt:
                        print 
                        print 
                        return
                    if response in ['y', 'n']:
                        response_valid = True
                        
                if response == 'n': 
                    print "abort"
                    return
                    
            connection = connections[options.get('database')]
            cursor = connection.cursor()
            
            cursor.execute('SET foreign_key_checks = 0')
            cursor.execute('show tables')
            
            for r in cursor.fetchall():
                print  "Dropping table %s" % r[0]
                cursor.execute('DROP TABLE ' + r[0])
                
            cursor.execute('SET foreign_key_checks = 0')
            
        super(Command, self).handle(*args, **options)
        
        if 'south' in settings.INSTALLED_APPS and options.get('use_south') is True:
            call_command('migrate')
        