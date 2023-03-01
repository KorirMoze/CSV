import csv
from django.http import HttpResponse, HttpResponseRedirect
import os
from bs4 import BeautifulSoup
import time

from django.shortcuts import render

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
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # Do something with the CSV file
        return HttpResponseRedirect('/success/')  # Redirect to a success page
    else:
        return render(request, 'upload_csv.html')  # Render the upload form
