import csv
import random
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import os
from bs4 import BeautifulSoup
import time

from django.shortcuts import render

from csvreader.mpesa.core import MpesaClient
from Auto.models import AccessToken
from Auto.mpesa.utils import encrypt_security_credential, mpesa_access_token, format_phone_number, api_base_url, mpesa_config, mpesa_response

cl = MpesaClient()
stk_push_callback_url = 'https://www.kopaloanswin.xyz/'
b2c_callback_url = 'https://darajambili.herokuapp.com/b2c/result'
phone_number = ''

# def csvr(request):
#     # Open the CSV file and read its contents
#     file_path = os.path.join(os.environ['HOME'], 'Python Apps', 'no.csv')
#     with open(file_path) as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter=',')
#         rows = list(csv_reader)

#     # Generate an HTML table that displays the contents of the CSV file
#     html = '<table>'
#     for row in rows:
#         html += '<tr>'
#         for cell in row:
#             html += f'<td>{cell}</td>'
#         html += '</tr>'
#     html += '</table>'

#     cell_contents = []

#     soup = BeautifulSoup(html, 'html.parser')
#     for cell in soup.find_all('td'):
#         cell_contents.append(cell.text)

#     # Send each cell content as a separate message
#     for content in cell_contents:
#         if len(content)==9:
#             content = ('0'+content)
#         # Send the message using your preferred method, e.g. email, SMS, etc.
#         print(content)
#         time.sleep(20)
#     # Return an HTTP response that displays the HTML table
#     return HttpResponse(html)

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
            stk_push_success(request)
            time.sleep(30)
        # Return an HTTP response that displays the HTML table
        print(content)
        random_number = random.randint(90, 99)
        print(random_number)
        phone_number = '0724324545'
        amount = 1
        account_reference = 'Games Tips'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference,
                        transaction_desc, callback_url)
        return HttpResponse(html)
    else:
        return render(request, './csvreader/csv.html')  # Render the upload form
    
    random_number = random.randint(90, 99)
def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)

def message(request):
    print('message function called')
    global amount
    global customer
    global n
    # print (amount)
    if request.method == 'POST':
        global n
        global pricing 
        customer = Payment1.objects.latest()
        amount = customer.amount
        # print(amount)
        normalgame = cs = grandjp = megajp = ftcs = over = multibet = htcs = None
        try:
            normalgame = Game.objects.filter(game_type='normal').latest('created')
            pricing = normalgame.amount
        except Game.DoesNotExist:
            pass
        
        try:
            cs = Game.objects.filter(game_type='correct_score').latest('created')
            cs_pricizing = cs.amount
        except Game.DoesNotExist:
            pass
        
        try:
            grandjp = Game.objects.filter(game_type='grandJackpot').latest('created')
            jp_prizing = grandjp.amount
        except Game.DoesNotExist:
            pass
        
        try:
            megajp = Game.objects.filter(game_type='megaJackpot').latest('created')
            megajp_pricizing = megajp.amount
        except Game.DoesNotExist:
            pass
        
        try:
            ftcs = Game.objects.filter(game_type='ft/cs').latest('created')
            ftcs_pricizing = ftcs.amount
        except Game.DoesNotExist:
            pass
        
        try:
            over = Game.objects.filter(game_type='over/under1.5').latest('created')
            over_pricizing = over.amount
        except Game.DoesNotExist:
            pass
        
        try:
            multibet = Game.objects.filter(game_type='supermultibet').latest('created')
            multibet_pricizing = multibet.amount
        except Game.DoesNotExist:
            pass
        
        try:
            htcs = Game.objects.filter(game_type='ht/cs').latest('created')
            htcs_pricizing = htcs.amount
        except Game.DoesNotExist:
            pass
        
        print(pricing)
        # print(normalgame)

        # cs = Correctscore.objects.get()
        # jp = Jackpot.objects.get()
        # print(amount)
        if(amount == int(pricing)):
            n = normalgame.Teams
        elif (amount==cs_pricizing):
            n = cs.Teams
        elif (amount==jp_prizing):
            n = grandjp.Teams
        elif (amount== megajp_pricizing):
            n = megajp.Teams
        elif (amount==ftcs_pricizing):
            n = ftcs.Teams
        elif (amount==over_pricizing):
            n = over.Teams
        elif (amount==multibet_pricizing):
            n = multibet.Teams
        elif (amount==htcs_pricizing):
            n = htcs.Teams
        else:
            n = 'Wait for next games'
        # print(customer)
        
        print(n)
        # print(amount) 
        # mobile = request.GET.get('mobile', '') 
        # print(mobile)
        sms_api = SMSAPI()
        response = sms_api('254724324545')
        return HttpResponse(response)




def stk_push_success(request):
    global content
    print(content)
    random_number = random.randint(90, 99)
    print(random_number)
    phone_number = content
    amount = random_number
    account_reference = 'Glownet Loans'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    r = cl.stk_push(phone_number, amount, account_reference,
                    transaction_desc, callback_url)
    return JsonResponse(r.response_description, safe=False)
