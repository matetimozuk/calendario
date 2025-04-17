from flask import Flask, render_template, request, url_for
import calendar
from datetime import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES')
    except locale.Error:
        pass 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    year = datetime.now().year
    month = datetime.now().month
    calendar_html = ""

    if request.method == "POST":
        year = int(request.form.get("year", year))
        month = int(request.form.get("month", month))
    
    calendar.setfirstweekday(calendar.MONDAY)  
    calendar_html = calendar.HTMLCalendar().formatmonth(year, month)

    return render_template("calendar.html", calendar=calendar_html, year=year, month=month)

if __name__ == "__main__":
    app.run(debug=True)


