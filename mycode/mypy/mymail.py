from smtplib import SMTP
import datetime

debuglevel = 0

sendmessage(to_addr = "jlmarks@jlmarks.org", subj="from LivingRoomMachine", message_text = " "):
    smtp = SMTP()
    smtp.set_debuglevel(debuglevel)
    smtp.connect('smtpout.secureserver.net', 3535)
    smtp.login('jeremiah@jlmarks.org', 'B0ttles0fb33r!')

    from_addr = "JL Marks <jeremiah@jlmarks.org>"



    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

    smtp.sendmail(from_addr, to_addr, msg)
    smtp.quit()
