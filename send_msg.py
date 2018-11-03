import csv
import urllib.request
import re

my_file=open("message.txt","r")
msg=my_file.read()
my_file.close()

message=str(msg)

def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    >>> print slugify("[Some] _ Article's Title--")
    some-articles-title
    """

    # # "[Some] _ Article's Title--"
    # # "[some] _ article's title--"
    # s = s.lower()

    # "[some] _ article's_title--"
    # "[some]___article's_title__"
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')

    # "[some]___article's_title__"
    # "some___articles_title__"
    # s = re.sub('\W', '', s)

    # "some___articles_title__"
    # "some   articles title  "
    s = s.replace('_', ' ')

    # "some   articles title  "
    # "some articles title "
    s = re.sub('\s+', ' ', s)

    # "some articles title "
    # "some articles title"
    s = s.strip()

    # "some articles title"
    # "some-articles-title"
    s = s.replace(' ', '%20')

    return s

with open('name_contact.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are',", ".join(row))
            line_count += 1
        name=row['name']
        contact=row["contact"]
        prifix = row["prefix"]
        message_1 =prifix+' '+name+','+message
        msg=slugify(message_1)
        url_1='''http://103.16.101.52:8080/bulksms/bulksms?username=ssd-akshya&password=balram&type=0&dlr=1&destination=%2B'''
        url_2='''&source=FOLKPL&message='''
        url_link=url_1+ str(contact) + url_2 + msg

        urllib.request.urlopen(url_link)

        print(url_link)
        print('\n***message sent to',row["name"],'with prifix',row["prefix"],'message:-',message,'|contact no-',row["contact"])
        line_count += 1
    print('Processed {} lines.'.format(line_count))