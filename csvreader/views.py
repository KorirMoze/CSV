import csv
import random
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
from bs4 import BeautifulSoup
import time

from django.shortcuts import render

from csvreader.mpesa.core import MpesaClient


cl = MpesaClient()
stk_push_callback_url = 'https://www.kopaloanswin.xyz/'
b2c_callback_url = 'https://darajambili.herokuapp.com/b2c/result'
phone_number = ''

def csvr(request):
    # Open the CSV file and read its contents
    file_path = os.path.join(os.environ['HOME'], 'Python Apps', 'no.csv')
    with open(file_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        rows = list(csv_reader)

    # Generate an HTML table that displays the contents of the CSV file
    html = '<table>'
    for row in rows:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>'
    html += '</table>'

    cell_contents = []

    soup = BeautifulSoup(html, 'html.parser')
    for cell in soup.find_all('td'):
        cell_contents.append(cell.text)

    # Send each cell content as a separate message
    for content in cell_contents:
        if len(content)==9:
            content = ('0'+content)
        # Send the message using your preferred method, e.g. email, SMS, etc.
        print(content)
        time.sleep(20)
    # Return an HTTP response that displays the HTML table
    return HttpResponse(html)

def upload_csv(request):
    global content
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # Do something with the CSV file
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        rows = list(reader)
        html = '<table>'
        for row in rows:
            html += '<tr>'
            for cell in row:
                html += f'<td>{cell}</td>'
            html += '</tr>'
        html += '</table>'

        cell_contents = []

        soup = BeautifulSoup(html, 'html.parser')
        for cell in soup.find_all('td'):
            cell_contents.append(cell.text)

        # Send each cell content as a separate message
        for content in cell_contents:
            if len(content)==9:
                content = ('0'+content)
            # Send the message using your preferred method, e.g. email, SMS, etc.
            # print(content)
            # stk_push_success(request)
            # time.sleep(30)
        # Return an HTTP response that displays the HTML table
        print(content)
        # random_number = random.randint(90, 99)
        # print(random_number)
        # phone_number = '0724324545'
        # amount = 1
        # account_reference = 'Games Tips'
        # transaction_desc = 'STK Push Description'
        # callback_url = stk_push_callback_url
        # r = cl.stk_push(phone_number, amount, account_reference,
        #                 transaction_desc, callback_url)
        return HttpResponse(html)
    else:
        return render(request, './csvreader/csv.html')  # Render the upload form
    
    random_number = random.randint(90, 99)
def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)
        
def stk_push_success(request):
    global content
    print(content)
    random_number = random.randint(90, 99)
    print(random_number)
    phone_number = '0724324545'
    amount = random_number
    account_reference = 'Glownet Loans'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference,
                    transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)
