import smtplib # Import smtplib for the actual sending function
from email.MIMEMultipart import MIMEMultipart # Import the email modules we'll need
from email.MIMEText import MIMEText
import csv #For dealing with the CSV files and data
import multiprocessing  # the module we will be using for multiprocessing



def send_mail(info):
    msg = MIMEMultipart() # Create message container - the correct MIME type is multipart/alternative
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = info[1]
    msg.attach(MIMEText(info[2], 'plain')) # Attach parts into message container
    text = msg.as_string()
    server.sendmail(fromaddr, info[0], text)

if __name__ == "__main__":  # Allows for the safe importing of the main module
    filename = "fcku.csv" 
    print("There are %d CPUs on this machine" % multiprocessing.cpu_count())
    number_processes = 2
    pool = multiprocessing.Pool(number_processes)
    info = []
    with open(filename, 'rb') as csvfile: #opening file in binary mode
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                info.append(row)
    fromaddr = "YOUR ADDRESS"
    server = smtplib.SMTP('smtp.gmail.com', 587)  #sending the message with SMTP
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD")
    
    results = pool.map_async(send_mail, info)
    pool.close()
    pool.join()