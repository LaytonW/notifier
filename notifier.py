url = {'BA(ArchStud)' : 'http://www.exam.hku.hk/timetable/BA-ARCHSTUD.htm',
       'BA(Conservation)' : 'http://www.exam.hku.hk/timetable/BA-CONSERVATION.htm',
       'BA(LS)' : 'http://www.exam.hku.hk/timetable/BA-LS.htm',
       'BA(UrbanStud)' : 'http://www.exam.hku.hk/timetable/BA-URBANSTUD.htm',
       'Bsc(Surv)' : 'http://www.exam.hku.hk/timetable/BSC-SURV.htm',
       'BHousMan' : 'http://www.exam.hku.hk/timetable/BHOUSMAN.htm',
       'BBA' : 'http://www.exam.hku.hk/timetable/BBA.htm',
       'BBA(Acc&Fin)' : 'http://www.exam.hku.hk/timetable/BBA-ACCFIN.htm',
       'BBA(IBGM)' : 'http://www.exam.hku.hk/timetable/BBA-IBGM.htm',
       'BBA(IS)' : 'http://www.exam.hku.hk/timetable/BBA-IS.htm',
       'BBA(Law)' : 'http://www.exam.hku.hk/timetable/BBA-LAW.htm',
       'BBA(LAW)&LLB' : 'http://www.exam.hku.hk/timetable/BBA-LAWLLB.htm',
       'BBA(UrbanStud)' : 'http://www.exam.hku.hk/timetable/BA-URBANSTUD.htm',
       'BEcon' : 'http://www.exam.hku.hk/timetable/BECON.htm',
       'BEcon&Fin' : 'http://www.exam.hku.hk/timetable/BECON-FIN.htm',
       'BSc(QFin)' : 'http://www.exam.hku.hk/timetable/BSC-QFIN.htm',
       'BA&BEd(LangEd-Chin)' : 'http://www.exam.hku.hk/timetable/BABED-LANGED-CHIN.htm',
       'BA&BEd(LangEd-Eng)' : 'http://www.exam.hku.hk/timetable/BABED-LANGED-ENG.htm',
       'BEd' : 'http://www.exam.hku.hk/timetable/BED.htm',
       'BEd&Bsc' : 'http://www.exam.hku.hk/timetable/BEDBSC.htm',
       'BEd&BSocSc' : 'http://www.exam.hku.hk/timetable/BEDBSS.htm',
       'BEd(LangEd-Chin)' : 'http://www.exam.hku.hk/timetable/BED-LANGED.htm',
       'BEd(LangEd-Eng)' : 'http://www.exam.hku.hk/timetable/BED-LANGED-ENG.htm',
       'BSc(Exercise&Health)' : 'http://www.exam.hku.hk/timetable/BSC-EXERCISEHEALTH.htm',
       'BSc(IM)' : 'http://www.exam.hku.hk/timetable/BSC-IM.htm',
       'BSc(Sp&HearSc)' : 'http://www.exam.hku.hk/timetable/BSC-SPHEARSC.htm',
       'BSocSc(Govt&Laws)&LLB' : 'http://www.exam.hku.hk/timetable/BSOCSC-GOVTLAWSLLB.htm',
       'LLB' : 'http://www.exam.hku.hk/timetable/LLB.htm',
       'BSc' : 'http://www.exam.hku.hk/timetable/BSC.htm',
       'BSc(ActuarSc)' : 'http://www.exam.hku.hk/timetable/BSC-ACTUARSC.htm',
       'BA(Literary Studies)' : 'http://www.exam.hku.hk/timetable/BA-LITERARYSTUDIES.htm',
       'BA' : 'http://www.exam.hku.hk/timetable/BA.htm',
       'BA&LLB' : 'http://www.exam.hku.hk/timetable/BALLB.htm',
       'BDS' : 'http://www.exam.hku.hk/timetable/BDS.htm',
       'BEng' : 'http://www.exam.hku.hk/timetable/BENG.htm',
       'BBiomedSc' : 'http://www.exam.hku.hk/timetable/BBIOMEDSC.htm',
       'BChinMed' : 'http://www.exam.hku.hk/timetable/BCHINMED.htm',
       'BNurs' : 'http://www.exam.hku.hk/timetable/BSC-NURS.htm',
       'BPharm' : 'http://www.exam.hku.hk/timetable/BPHARM.htm',
       'MBBS' : 'http://www.exam.hku.hk/timetable/MBBS.htm',
       'BJ' : 'http://www.exam.hku.hk/timetable/BJ.htm',
       'BSW' : 'http://www.exam.hku.hk/timetable/BSW.htm',
       'BSocSc' : 'http://www.exam.hku.hk/timetable/BSOCSC.htm',
       'BSocSc(Govt&Laws)' : 'http://www.exam.hku.hk/timetable/BSOC-GL.htm',
       'Bachelor of Criminal Justice Examination' : 'http://www.exam.hku.hk/timetable/BCJ.htm',
       }

table = {}
updateTime = {}
subscribers = {}

def updateTimetable(url):
    from lxml.html import parse
    from lxml import etree
    content = parse(url)
    etree.strip_tags(content, 'font', 'b')
    rows = content.xpath('body/table')[1].findall('tr')
    data = list()
    for row in rows:
        data.append([c.text for c in row.getchildren()])
    timetable = {}
    for entry in data[1:]:
        code = entry[3].strip()
        name = entry[4].strip()
        date = entry[0].strip()
        time = entry[1].strip()
        venu = entry[5].strip()
        if code not in timetable:
            timetable[code] = list()
        timetable[code].append((code, name, date, time, venu))
    return timetable

def search(curr, code):
    if code not in table[curr]:
        return None
    return table[curr][code]

def sortKey(t):
    code, name, date, time, venu = t
    date = date.split(' ')[1]
    time = time.split('-')[0].strip()
    t = time.split(' ')[0]
    if time[-2:] == 'pm':
        t = str(int(t.split(':')[0]) + 12) + ':' + t.split(':')[1]
    if len(t.split(':')[0]) == 1:
        t = '0' + t.split(':')[0] + ':' + t.split(':')[1]
    return int(date), t

def query(curr, l):
    msg = "<table><tr><td><u>Date</u></td><td width=10></td><td><u>Time</u></td><td width=10></td><td width=70><u>Course Code</u></td><td width=10></td><td><u>Description</u></td><td width=10></td><td><u>Venue</u></td></tr>"
    found = list()
    nfound = list()
    for q in l:
        r = search(curr, q)
        if r == None:
            nfound.append(q)
        else:
            for p in r:
                found.append(p)
    found = sorted(found, key=sortKey)
    for e in found:
        code, name, date, time, venu = e
        msg += '<tr><td valign=top width=48>{}</td><td width=10></td><td valign=top width=170>{}</td><td width=10></td><td valign=top width=50>{}</td><td width=10></td><td valign=top width=210>{}</td><td width=10></td><td valign=top>{}</td></tr>'.format(date, time, code, name, venu)
    msg += '</table>'
    if len(nfound) != 0:
        msg += '<br><br>'
    for e in nfound:
        msg += 'No record of exam for {}.<br>'.format(e)
    return msg

def subscribe(c, n, a, q):
    if c not in subscribers:
        subscribers[c] = list()
    subscribers[c].append((n, a, q))

def forward(curr, t):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    if curr not in subscribers:
        return
    l = subscribers[curr]
    for s in l:
        name, addr, cour = s
        print "Forwarding to ", name, " with addr ", addr
        msg = MIMEMultipart('alternative')
        msg['Subject'] = '(noreply) Updated Exam Timetable'
        msg['From'] = 'noreply@wangzixu.me'
        msg['To'] = addr
        text = '<html><body>Dear {},<br><br>Your subscribed exam timetable has been updated.<br><br>{}<br><br>Note that this is NOT the official personal exam timetable. Thank you for your support!</body></html>'.format(name, query(curr, cour))
        msg.attach(MIMEText(text, 'html'))
        server = smtplib.SMTP('mail.wangzixu.me:26')
        server.ehlo()
        server.starttls()
        server.login('noreply@wangzixu.me', '!Q@W#E$R')
        server.sendmail('noreply@wangzixu.me', [addr], msg.as_string())
        server.quit()

def checkSubscribe():
    pass

import urllib2 as ul
import time
import thread
from datetime import datetime

subscribe('BEng', 'Wang Zixu', 'wangzixu.china@gmail.com', ['COMP2123', 'COMP2121', 'COMP2396', 'ELEC2346', 'ELEC3241'])
#subscribe('BEcon&Fin', 'Wang Jing', 'wj929570566@gmail.com', ['COMP2121', 'ECON2220', 'FINA2322', 'FINA2320', 'MATH2101', 'ECON2280'])
#subscribe('BEng', 'Ji Zhuoran', 'jizr@hku.hk', ['COMP2123', 'COMP2121', 'COMP3317', 'ELEC4543', 'MATH2101', 'COMP3278'])

while True:
    for curr in url:
        if curr not in updateTime:
            updateTime[curr] = None
        lastUpdate = updateTime[curr]
        lastModify = datetime.fromtimestamp(time.mktime(ul.urlopen(url[curr]).info().getdate('last-modified')))
        if lastUpdate == None:
            print "Initialize table for ", curr
            updateTime[curr] = lastModify
            table[curr] = updateTimetable(url[curr])
            forward(curr, lastModify)
        elif int((lastModify - lastUpdate).days) > 90:
            print "Update table for ", curr
            updateTime[curr] = lastModify
            table[curr] = updateTimetable(url[curr])
            forward(curr, lastModify)
    time.sleep(10)
