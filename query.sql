--SIMPLE
--Find user details given user email_id
select * from customer 
where email_id='sethupathyrv@gmail.com';

-- Find the list of shows with english subtitles
select show_name from show
where subtitles='yes';


--Update Masala dosa price to 100
update Food
set food_price=100
where food_name='Masala Dosa';
select * from Food;

--Given show name return whether it has subtitles or not
select subtitles from show
where show_name='Sardar Udham';

--Count of gender of the customer
select gender,count(*) from customer group by gender;


-- Find all english movies with Action thriller genre
select * from show
where language='English' and genre='Action Thriller';

--Display food price from minimum to maximum
select * from food order by food_price;

-- Decrease bill with bill id 1131 by 10%
update bill
set charges=(0.9)*charges
where bill_id=1131;
select * from bill; 

--COMPLEX QUERY
--List of theatres playing the shows
select theatre_name,show_name from plays,theatre,show
where theatre.theatre_id=plays.theatre_id and show.show_id=plays.show_id;

--Select list of customers booked given booking date
select first_name from customer
where customer_id in (select customer_id from bought_by
where booking_date ='2021-11-09');

--Display bill id with max charges
select bill_id from bill 
where charges=(select max(charges) from bill);

--Which theatre had the least vacancy for Eternals
select theatre_name from theatre 
where theatre_id=(select theatre_id from screens
where vacant_seats=(select min(vacant_seats) from screens
where show='Eternals'));

--Most expensive food
select food_name from food
where food_price=(select max(food_price) from food);

-- Find the list of all the customers watching a certain show currently in the DB
select first_name, genre, show_name from bought_by,customer,show
where bought_by.customer_id=customer.customer_id and show.show_id=bought_by.show_id;






