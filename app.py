from logging import warning
import streamlit as st
import datetime
import psycopg2
import pandas as pd
from psycopg2.extensions import AsIs
from psycopg2 import sql
from random import randrange
from datetime import date


def simple_queries(username, pw):
    con = psycopg2.connect(
        host='localhost',
        database='moviebooking',
        user=username,
        password=pw
    )
    cur = con.cursor()
    queries = {
        'user details given user email_id',
        'list of shows with the given language',
        'Update Food price',
        'Given show name return whether it has subtitles or not',
        'Count of gender of the customer',
        'All movies of given genre and language',
        'Order food by price',
        'Decrease bill with bill id 1131 by 10%'
    }
    option = st.selectbox("Choose query", options=queries)
    if(option == 'user details given user email_id'):
        inp = st.text_input('Enter email')
        submit = st.button("Submit")
        if submit and inp != "":
            try:
                cur.execute(
                    "select username,first_name,middle_name,last_name,email_id,phone_no,dob,gender from customer where email_id='"+inp+"';")
                df = pd.DataFrame(cur.fetchall())
                df.columns = ['Username', 'Firstname', 'middlename',
                              'lastname', 'mail', 'Phone', 'dob', 'Gender']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")
    elif (option == 'list of shows with the given language'):
        inp = st.text_input('Enter Language')
        submit = st.button("Submit")
        if submit and inp != "":
            try:
                cur.execute(
                    "select * from custo_view_show where language='"+inp+"';")
                df = pd.DataFrame(cur.fetchall())
                df.columns = ['Language', 'genre',
                              'subtitles', 'Show name', 'timing', 'Date']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")
    elif (option == 'Update Food price'):
        inp1 = st.text_input('Enter Food')
        inp2 = st.text_input('Enter New price')
        submit = st.button("Submit")
        if submit and inp1 != "" and inp2 != "":
            try:
                cur.execute("update Food set food_price="+inp2 +
                            " where food_name='"+inp1+"'; select food_name,food_price from Food;")
                df = pd.DataFrame(cur.fetchall())
                df.columns = ['Food name', 'Prices']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")
    elif (option == 'Given show name return whether it has subtitles or not'):
        inp = st.text_input('Enter Show name')
        submit = st.button("Submit")
        if submit and inp != "":
            try:
                cur.execute(
                    "select subtitles from show where show_name='"+inp+"';")
                df = pd.DataFrame(cur.fetchall())
                df.columns = ['Subtitle']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")
    elif (option == 'Count of gender of the customer'):
        cur.execute("select gender,count(*) from customer group by gender;")
        df = pd.DataFrame(cur.fetchall())
        df.columns = ['Gender', 'Count']
        st.table(df)
    elif (option == 'All movies of given genre and language'):
        inp1 = st.text_input('Language')
        inp2 = st.text_input('Genre')
        submit = st.button("Submit")
        if submit and inp1 != "" and inp2 != "":
            try:
                cur.execute("select language,genre,subtitles,show_name,timing,date from show where language='" +
                            inp1+"' and genre='"+inp2+"';")
                df = pd.DataFrame(cur.fetchall())
                df.columns = ['language', 'genre',
                              'subtitle', 'Show name', 'Timing', 'Date']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")
    elif(option == 'Order food by price'):
        sort = st.radio("Sort", ["High to Low", "Low to High"])
        if sort == "High to Low":
            cur.execute("select * from food order by food_price desc;")
            df = pd.DataFrame(cur.fetchall())
            st.table(df)
        elif sort == "Low to High":
            cur.execute("select * from food order by food_price;")
            df = pd.DataFrame(cur.fetchall())
            st.table(df)
    elif(option == 'Decrease bill with bill id 1131 by 10%'):
        inp1 = st.text_input('Enter Bill ID')
        inp2 = st.text_input('Enter Discount %')
        submit = st.button("Submit")
        if submit and inp1 != "" and inp2 != "":
            try:
                disc = 1-int(inp2)/100
                disc = str(disc)
                print(disc)
                cur.execute(
                    "update bill set charges=("+disc+")*charges where bill_id='"+inp1+"'; select * from bill;")
                print(
                    "update bill set charges=("+disc+")*charges where bill_id='"+inp1+"'; select * from bill;")
                con.commit()
                df = pd.DataFrame(cur.fetchall())
                # df.columns = ['language', 'genre',
                #               'subtitle', 'Show name', 'Timing', 'Date']
                st.table(df)
            except psycopg2.errors.InFailedSqlTransaction as e:
                st.warning(e)
            except psycopg2.OperationalError as e:
                st.warning(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                st.warning(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")


def complex_queries(username, pw):
    con = psycopg2.connect(
        host='localhost',
        database='moviebooking',
        user=username,
        password=pw
    )
    cur = con.cursor()
    queries = {'List of theatres playing the shows',
               'Select list of customers booked given booking date: 2021-11-09',
               'bill id with max charges',
               'Which theatre had the least vacancy for Eternals',
               'Most expensive food',
               'List of all the customers watching a certain show currently in the DB'}
    option = st.selectbox("Choose query", options=queries)
    # cur.execute(queries[option])

    if(option == 'List of theatres playing the shows'):
        cur.execute(
            "select theatre_name,show_name from plays,theatre,show where theatre.theatre_id=plays.theatre_id and show.show_id=plays.show_id;")
        col = ['Theatre', 'Movie']
    elif(option == 'Select list of customers booked given booking date: 2021-11-09'):
        cur.execute(
            "select first_name from customer where customer_id in (select customer_id from bought_by where booking_date ='2021-11-09');")
        col = ['Customer']
    elif(option == 'bill id with max charges'):
        cur.execute(
            "select bill_id from bill where charges=(select max(charges) from bill);")
        col = ['Bill_ID']
    elif(option == 'Which theatre had the least vacancy for Eternals'):
        cur.execute("select theatre_name from theatre where theatre_id=(select theatre_id from screens where vacant_seats=(select min(vacant_seats) from screens where show='Eternals'));")
        col = ['Theatre']
    elif(option == 'Most expensive food'):
        cur.execute(
            "select food_name from food where food_price=(select max(food_price) from food);")
        col = ['Food Name']
    elif(option == 'List of all the customers watching a certain show currently in the DB'):
        cur.execute("select first_name, genre, show_name from bought_by,customer,show where bought_by.customer_id=customer.customer_id and show.show_id=bought_by.show_id;")
        col = ['Customer', 'Genre', 'Movie']
    df = pd.DataFrame(cur.fetchall())
    df.columns = col
    st.table(df)
    cur.close()
    con.close()


def login(username, pw):
    try:
        if(username != "" and pw != ""):
            con = psycopg2.connect(
                host='localhost',
                database='moviebooking',
                user=username,
                password=pw
            )
            ROLE = username
            st.sidebar.info('\tlogged in as ' + ROLE)
            con.close()
            return True
    except psycopg2.OperationalError as e:
        st.sidebar.warning('\tnot logged in')
        st.error(e)
        return False


def remove(username, pw):
    if(username != "" and pw != ""):
        con = psycopg2.connect(
            host='localhost',
            database='moviebooking',
            user=username,
            password=pw
        )
        if username != "postgres" and username != "restaurant_manager" and username != "ticket_seller" and username != "owner1":
            st.warning(
                "This user does not have access to this section of the page")
        else:
            cur = con.cursor()
            options = st.selectbox("Choose what to remove from", [
                                   "Remove food", "Remove show", "Delete from plays", "Remove screen", "Remove bought ticket"])
            try:
                if options == "Remove food":
                    with st.form(key='removefood', clear_on_submit=False):
                        cur.execute("select food_name from food;")
                        df = cur.fetchall()
                        df = pd.DataFrame(df)
                        df.columns = ["food_name"]
                        food_name = st.selectbox(
                            "Select food name", options=tuple(df["food_name"]))
                        remfood = st.form_submit_button('Remove food')
                        if remfood:
                            if food_name != "":
                                cur.execute(
                                    "delete from Food where food_name='"+food_name+"';")
                                con.commit()
                                st.info("Succesfully deleted"+food_name+"")
                elif options == "Remove show":
                    with st.form(key='removeshow', clear_on_submit=False):
                        show_name = st.text_input("Enter show name")
                        remshow = st.form_submit_button('Remove Show')
                        if remshow:
                            cur.execute("select show_name from show;")
                            df = cur.fetchall()
                            df = pd.DataFrame(df)

                            if show_name != "":
                                if show_name in tuple(df[0]):
                                    cur.execute(
                                        "Delete from show where show_name='"+show_name+"';")
                                    con.commit()
                                    st.info("Succesfully deleted "+show_name)
                                else:
                                    st.warning(
                                        ""+show_name+" does not exist :(")
                                    st.write("Try Entering from one of these")
                                    st.table(df[0])
                elif options == "Delete from plays":
                    with st.form(key='removeplays', clear_on_submit=False):
                        theatre_name = st.text_input("Enter theatre name")
                        show_name = st.text_input("Enter show name")
                        remplay = st.form_submit_button('Remove from Plays')
                        if remplay:
                            cur.execute("select show_name from plays;")
                            df1 = cur.fetchall()
                            df1 = pd.DataFrame(df1)
                            cur.execute("select theatre_name from plays")
                            df2 = cur.fetchall()
                            df2 = pd.DataFrame(df2)
                            if show_name != "" and theatre_name != "":
                                if show_name in tuple(df1[0]) and theatre_name in tuple(df2[0]):
                                    cur.execute(
                                        "Delete from plays where show_name='"+show_name+"' and theatre_name='"+theatre_name+"';")
                                    con.commit()
                                    st.info("Succesfully deleted " +
                                            show_name+" in "+theatre_name)
                                else:
                                    st.warning("Invalid entry")
                elif options == "Remove screen":
                    with st.form(key='removescreen', clear_on_submit=False):
                        screen_id = st.text_input("Enter screen ID")
                        remscreen = st.form_submit_button('Remove Screen')
                        if remscreen:
                            if screen_id != "":
                                cur.execute("select screen_id from screen;")
                                df = cur.fetchall()
                                df = pd.DataFrame(df)
                                if screen_id in tuple(df[0]):
                                    cur.execute(
                                        "Delete from screen where screen_id='"+screen_id+"';")
                                    con.commit()
                                    st.info("Succesfully deleted "+screen_id)
                                else:
                                    st.warning(
                                        ""+screen_id+" does not exist :(")
                elif options == "Remove bought ticket":
                    with st.form(key='removeticket', clear_on_submit=False):
                        show_id = st.text_input("Entet show ID")
                        customer_id = st.text_input("Enter customer ID")
                        remticket = st.form_submit_button('Remove Ticket')
                        if remticket:
                            if show_id != "" and customer_id != "":
                                cur.execute(
                                    "select customer_id,show_id from bought_by where customer_id='"+customer_id+"' and show_id='"+show_id+"';")
                                df = cur.fetchall()
                                df = pd.DataFrame(df)

                                if customer_id in tuple(df[0]) and show_id in tuple(df[1]):
                                    cur.execute(
                                        "Delete from from bought_by where customer_id='"+customer_id+"' and show_id='"+show_id+"';")
                                    con.commit()
                                    st.info("Succesfully deleted")
                                else:
                                    st.warning(
                                        ""+customer_id+" or "+show_id+" does not exist :(")

            except psycopg2.errors.InFailedSqlTransaction as e:
                print(e)
            except psycopg2.OperationalError as e:
                print(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                print(e)
            finally:
                if con:
                    cur.close()
                    con.close()
                    print("PostgreSQL connection is closed")


def read(username, pw):
    if(username != "" and pw != ""):
        con = psycopg2.connect(
            host='localhost',
            database='moviebooking',
            user=username,
            password=pw
        )
        cur = con.cursor()
        cur.execute(
            "select table_name from information_schema.tables where table_schema = 'public';")
        df = cur.fetchall()
        df = pd.DataFrame(df)
        df.columns = ["tables"]
        option = st.selectbox("Choose table", options=tuple(df["tables"]))
        cur.execute("select * from "+option+"")
        cur.execute(
            "select column_name from information_schema.columns where table_schema = 'public' and table_name='"+option+"'")
        col = [row[0] for row in cur]
        cur.execute("Select * from "+option)
        df = pd.DataFrame(cur.fetchall())
        df.columns = col
        st.table(df)
        cur.close()
        con.close()


def createuser(username, password, first_name, middle_name, last_name, email_id, phone_no, dob, gender):
    if(first_name != "" and password != ""):
        try:
            con = psycopg2.connect(
                host='localhost',
                database='moviebooking',
                user='postgres',
                password=''  # password here
            )
            print(str(password), str(first_name), str(middle_name),
                  str(last_name), str(email_id), str(phone_no), str(dob), str(gender))
            cur = con.cursor()
            cur.execute("select customer_id from customer")
            cust_id = cur.fetchall()
            exist = 1
            while exist:
                customer_id = randrange(1000)
                if customer_id not in cust_id:
                    exist = 0
            customer_id = str(customer_id)
            print(customer_id)
            postgres_insert_query = """ INSERT INTO customer (customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (customer_id, username, password, first_name, middle_name,
                                last_name, email_id, phone_no, dob, gender)

            cur.execute(postgres_insert_query, record_to_insert)
            cur.execute("create user  %s with password %s",
                        (AsIs(username), password,))
            count = cur.rowcount
            print(count)
            granting_access = """grant select,update on custo_update to %s; 
            grant select on custo_view_theatre to %s; 
            grant select on custo_view_show to %s; 
            grant select on custo_view_food to %s; 
            grant select on custo_view_screen to %s; 
            grant select, update on custo_view_ord to %s;"""
            to_customer = (AsIs(username), AsIs(username), AsIs(
                username), AsIs(username), AsIs(username), AsIs(username))
            cur.execute(granting_access, to_customer)
            con.commit()
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record", error)
            st.warning(error)
        finally:
            if con:
                cur.close()
                con.close()
                print("PostgreSQL connection is closed")


title = st.container()
title.title('Book your favorite movies!!')

rad = st.sidebar.radio("Navigation", ["Home", "Signup"])
if rad == "Home":
    st.title('Home Page')
    with st.sidebar.form(key='loginform', clear_on_submit=True):
        st.sidebar.header('Already have an Account?')
        option = st.sidebar.text_input('Username')
        passw = st.sidebar.text_input(
            'password', placeholder="Enter password", type='password')
        st.sidebar.button('sign in', key='login')

    ref = st.container()
    login(option, passw)
    page = st.sidebar.selectbox('Choose page', options=(
        'read', 'delete', 'simple queries', 'complex queries'))
    with ref:
        if passw == '' or option == '':
            st.warning('please enter password and username')
        else:
            try:
                if page == 'read':
                    st.header('Select')
                    read(option, passw)
                elif page == 'delete':
                    st.header('Yeet stuff here')
                    remove(option, passw)
                elif page == 'simple queries':
                    st.header('Simple queries')
                    simple_queries(option, passw)
                elif page == 'complex queries':
                    st.header('Complex queries')
                    complex_queries(option, passw)
            except psycopg2.errors.InFailedSqlTransaction as e:
                print(e)
            except psycopg2.OperationalError as e:
                print(e)
            except psycopg2.errors.InsufficientPrivilege as e:
                print(e)

elif rad == "Signup":
    st.title('Sign Up')
    with st.form(key='Submitform', clear_on_submit=False):
        username = st.text_input('User Name')
        first_name = st.text_input('First Name')
        middle_name = st.text_input('Middle Name')
        last_name = st.text_input('Last Name')
        email_id = st.text_input('Email')
        password = st.text_input('Password', type='password')
        phone_no = st.text_input('Phone number', max_chars=10)
        dob = st.date_input('DOB')
        gender = st.radio('Gender', ["Male", "Female", "Non-Binary"])
        submitted = st.form_submit_button('Sign Up')

    dob = datetime.datetime.strptime(str(dob), '%Y-%m-%d').strftime('%d-%m-%Y')
    if gender == "Male":
        gender = "M"
    elif gender == "Female":
        gender = "F"
    elif gender == "Non-Binary":
        gender = "NB"

    createuser(str(username), str(password), str(first_name), str(middle_name),
               str(last_name), str(email_id), str(phone_no), str(dob), str(gender))
