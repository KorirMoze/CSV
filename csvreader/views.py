import csv
from django.http import HttpResponse
import os
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

    # Return an HTTP response that displays the HTML table
    return HttpResponse(rows)
