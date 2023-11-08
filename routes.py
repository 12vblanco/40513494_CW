import sqlite3
from flask import session, render_template, redirect, url_for, flash
from app import app
from datetime import date
from form import BookingForm, AdminLogin
from flask import Flask, flash, redirect, url_for
from urllib import request

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    # check the current day to avoid booking past days https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
    # set to isoformat() https://docs.python.org/3/library/datetime.html
    current_date = date.today().isoformat()
    
    # check if it's a POST and its valid https://flask-wtf.readthedocs.io/en/0.15.x/quickstart/
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        booking_date = form.booking_date.data
        time = form.time.data
        table_num = form.table_num.data
        
        con = sqlite3.connect('bookings.db')
        cur = con.cursor()
        
        # This will check if the table is free at that time and date
        cur.execute("SELECT * FROM bookings WHERE booking_date=? AND time=? AND table_num=?", (booking_date, time, table_num))
        existing_booking = cur.fetchone()
        
        if existing_booking:
            # message when the table is not available
            # including variables from the DB as in https://stackoverflow.com/questions/71153840/how-to-flash-message-with-variables-in-flask
            flash('Table {} is taken at {} - {}!'.format(table_num, time, booking_date), 'danger')
        else:
            # Save the booking if it's free
            cur.execute("INSERT INTO bookings (name, email, booking_date, time, table_num) VALUES (?, ?, ?, ?, ?)",
                  (name, email, booking_date, time, table_num))
            con.commit()
            # While looking for a fix to multiple messages showing I came across with this post about seasons https://stackoverflow.com/questions/46270091/displaying-multiple-flash-messages-with-flask
            session['table_booked'] = True
            flash('Table {} booked {} - {}!'.format(table_num, time, booking_date), 'success') 
            # and the message can appear only during the session avoiding the overlapping with success flash messages from admin
            session.pop('table_booked', None)

        con.close()
        return redirect(url_for('index'))   
        
    return render_template('index.html', form=form, current_date=current_date)

# the routes for the navigation to map and contact
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/menu', methods=['GET'])
def menu():
    return render_template('menu.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # then the same procedure to validate the admin login form
    form2 = AdminLogin()
    if form2.validate_on_submit():
        user = form2.user.data
        password = form2.password.data
        # if valid connect
        con = sqlite3.connect('bookings.db')
        cur = con.cursor()
        # then check user and password
        cur.execute("SELECT * FROM admin WHERE user=? AND password=?", (user, password))
        admin = cur.fetchone()
        
        if admin:
            # if the login is correct get bookings from the Db 
            cur.execute("SELECT * FROM bookings")
            bookings = cur.fetchall()
            con.close()
            # and pass them to delete.html
            return render_template('delete.html', bookings=bookings)
        else: 
            # if the login is not successful show a message with the user name entered
            flash('Introduce the right credentials {}'.format(user), 'danger')
        con.close()
    return render_template('admin.html', form2=form2)

# to delete the entries I adapted the code in https://stackoverflow.com/questions/25925024/how-to-delete-items-from-database-using-a-flask-framework
@app.route('/delete/<int:booking_id>', methods=['POST'])
def delete(booking_id):    
        con = sqlite3.connect('bookings.db')
        cur = con.cursor()
        # delete the booking with the right id
        cur.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
        con.commit()
        # success message
        flash('Booking deleted!', 'success')
        # check if there are bookings and if not redirect to home
        cur.execute("SELECT * FROM bookings")
        bookings = cur.fetchall()
        if not bookings:
            con.close()
            return redirect(url_for('index'))            
        con.close()
        # Stay if there are bookings
        return render_template('delete.html', bookings=bookings)
