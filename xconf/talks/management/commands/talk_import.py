from optparse import make_option
import csv
import sys
import chardet
import codecs

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from mezzanine.blog.models import BlogPost


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("-f", "--filename",
                action="store", type="string", dest="filename"),
        )

    def __csvfile(self, datafile):
        """ Detect file encoding and open appropriately """
        filehandle = open(datafile)
        diagnose = chardet.detect(filehandle.read())
        charset = diagnose['encoding']
        try:
            csvfile = codecs.open(datafile, 'r', charset)
        except IOError:
            self.error('Could not open specified csv file, %s, or it does not exist' % datafile, 0)
        else:
            return list(self.charset_csv_reader(csv_data=csvfile, 
                                                charset=charset))

    def charset_csv_reader(self, csv_data, 
                           dialect=csv.excel, charset='utf-8', **kwargs):
        csv_reader = csv.reader(self.charset_encoder(csv_data, charset), 
                                dialect=dialect, **kwargs)
        csv_reader.next()
        for row in csv_reader:
            yield [unicode(cell, charset) for cell in row]

    def charset_encoder(self, csv_data, charset='utf-8'):
        for line in csv_data:
            yield line.encode(charset)

    def handle(self, *args, **options):
        csvfilename = options['filename']
        csvfile = self.__csvfile(csvfilename)

        for row in csvfile:
            email = row[1]
            username = email.split('@')[0]
            try:
                u = User.objects.get(username=username)
            except User.DoesNotExist:
                u = User(email=email, username=username)
                u.save()

            try:
                talk = BlogPost.objects.filter(title__exact=row[2], user_id=u.id)[0]
                talk.content = row[3]
                talk.speakers = row[4]
                talk.office = row[5]
                talk.save()
            except:
                talk = BlogPost(title=row[2], content=row[3], user_id=u.id, speakers=row[4], office=row[5])
                talk.save()
                talk.categories.add(int(row[7]))
