drop database moviebooking;
create database moviebooking;

\c moviebooking

CREATE TABLE theatre(
    theatre_id int not null,
    theatre_name varchar(50),
    city varchar(30),
    state varchar(30),
    primary key(theatre_id)
    );

CREATE TABLE show(   
    show_id	int not null ,
    language varchar(20),
    genre varchar(20),
    subtitles varchar(20),
    show_name varchar(30),
    timing time,
    date date,
    primary key(show_id) 
    );

CREATE TABLE customer(	
    customer_id int not null,
    username varchar(20),
    password varchar(20),
    first_name varchar(20),
    middle_name varchar(20),
    last_name varchar(20),
    email_id varchar(30),
    phone_no char(10),
    dob date,
    gender varchar(2),
    primary key(customer_id)
    );

CREATE TABLE food_cart(	 
    order_id int not null,  
    orders varchar(200), 
    theatre_id int,
    primary key(order_id),
    foreign key(theatre_id) references theatre(theatre_id) ON DELETE CASCADE
    );

CREATE TABLE bill(
    bill_id  int not null, 
    charges int, 
    order_id int,
    primary key(bill_id),
    foreign key(order_id) references food_cart(order_id) ON DELETE CASCADE
    );

CREATE TABLE Food(	
    food_id int not null , 
    food_name varchar(30), 
    food_price int ,  
    food_type varchar(30),
    order_id int ,
    bill_id int,
    primary key(food_id),
    foreign key(order_id) references food_cart(order_id) ON DELETE CASCADE,
    foreign key(bill_id) references bill(bill_id) ON DELETE CASCADE
    );

CREATE TABLE plays(	
   theatre_id int not null,
   show_id int not null,
   primary key(theatre_id,show_id),
   foreign key(theatre_id) references theatre(theatre_id) ON DELETE CASCADE,
   foreign key(show_id) references show(show_id) ON DELETE CASCADE
   );

CREATE TABLE screens(
    screen_id int not null, 
    vacant_seats int, 
    show varchar(100), 
    time time,
    date date, 
    screen_no int , 
    cost int ,
    theatre_id int,
    show_id int,
    primary key(screen_id) ,
    foreign key(theatre_id) references theatre(theatre_id) ON DELETE CASCADE,
    foreign key(show_id) references show(show_id) ON DELETE CASCADE
    );

CREATE TABLE ticket(
    ticket_id int not null,
    seat_no int,
    show_date date,
    theatre_id int,
    show_id int,
    customer_id int,
    screen_id int,
    primary key(ticket_id),
    foreign key(theatre_id) references theatre(theatre_id) ON DELETE CASCADE,
    foreign key(show_id) references show(show_id) ON DELETE CASCADE,
    foreign key(customer_id) references customer(customer_id)ON DELETE CASCADE,
    foreign key(screen_id) references screens(screen_id) ON DELETE CASCADE
	);  

CREATE TABLE bought_by(	
    customer_id int not null,
    show_id int,
    booking_date date,
    primary key(customer_id),
    foreign key(customer_id) references customer(customer_id) ON DELETE CASCADE,
    foreign key(show_id) references show(show_id) ON DELETE CASCADE
    );