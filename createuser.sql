--Uncomment the following if the file is run from the second time onwards to avoid errors because of dependencies

revoke select on custo_view_theatre from customer;
revoke select,update on custo_update from customer;
revoke select on custo_view_theatre from customer;
revoke select on custo_view_show from customer;
revoke select on custo_view_food from customer;
revoke select on custo_view_screen from customer;
revoke select, update on custo_view_ord from customer;
revoke select, update on bill,food_cart from restaurant_manager;
revoke select, update,delete,truncate on food from restaurant_manager;
revoke select on resto_view_custo from restaurant_manager;
revoke select on resto_view_ord from restaurant_manager;
revoke select on theatre,ticket,bought_by,plays,screens,show from ticket_seller;
revoke select, update, delete on customer_id_update from ticket_seller;
revoke ALL on database moviebooking from owner1;

--Actual code starts here 
DROP USER IF EXISTS customer;
create user customer with password 'customer';

DROP USER IF EXISTS sethu21;
create user sethu21 with password 'Sethupathy';

DROP USER IF EXISTS Shanegg;
create user Shanegg with password 'Shane';

DROP USER IF EXISTS shettyRocks;
create user shettyRocks with password 'Shilpitha';

DROP USER IF EXISTS ram22;
create user ram22 with password 'Ram';

DROP USER IF EXISTS rahul101;
create user rahul101 with password 'Rahul';

Drop view if exists custo_update;
create view custo_update as select first_name,middle_name,last_name,email_id,phone_no,dob,gender from customer;
Drop view if exists custo_view_theatre;
create view custo_view_theatre as select theatre_name,city,state from theatre;
Drop view if exists custo_view_show;
create view custo_view_show as select language,genre,subtitles,show_name,timing,date from show;
Drop view if exists custo_view_food;
create view custo_view_food as select food_name,food_price,food_type from food;
Drop view if exists custo_view_screen;
create view custo_view_screen as select vacant_seats,show,time,date,screen_no,cost from screens;
Drop view if exists custo_view_ord;
create view custo_view_ord as select orders from food_cart;

grant select,update on custo_update to customer;
grant select on custo_view_theatre to customer;
grant select on custo_view_show to customer;
grant select on custo_view_food to customer;
grant select on custo_view_screen to customer;
grant select, update on custo_view_ord to customer;

grant select,update on custo_update to sethu21;
grant select on custo_view_theatre to sethu21;
grant select on custo_view_show to sethu21;
grant select on custo_view_food to sethu21;
grant select on custo_view_screen to sethu21;
grant select, update on custo_view_ord to sethu21;

grant select,update on custo_update to Shanegg;
grant select on custo_view_theatre to Shanegg;
grant select on custo_view_show to Shanegg;
grant select on custo_view_food to Shanegg;
grant select on custo_view_screen to Shanegg;
grant select, update on custo_view_ord to Shanegg;

grant select,update on custo_update to rahul101;
grant select on custo_view_theatre to rahul101;
grant select on custo_view_show to rahul101;
grant select on custo_view_food to rahul101;
grant select on custo_view_screen to rahul101;
grant select, update on custo_view_ord to rahul101;

grant select,update on custo_update to ram22;
grant select on custo_view_theatre to ram22;
grant select on custo_view_show to ram22;
grant select on custo_view_food to ram22;
grant select on custo_view_screen to ram22;
grant select, update on custo_view_ord to ram22;

grant select,update on custo_update to shettyRocks;
grant select on custo_view_theatre to shettyRocks;
grant select on custo_view_show to shettyRocks;
grant select on custo_view_food to shettyRocks;
grant select on custo_view_screen to shettyRocks;
grant select, update on custo_view_ord to shettyRocks;

DROP USER IF EXISTS restaurant_manager;
create user restaurant_manager with password 'restaurant_manager';

Drop view if exists resto_view_custo;
create view resto_view_custo as select customer_id from customer;
Drop view if exists resto_view_ord;
create view resto_view_ord as select order_id,orders,theatre_id from food_cart;

grant select, update on bill,food_cart to restaurant_manager;
grant select, update,delete,truncate on food to restaurant_manager;
grant select on resto_view_custo to restaurant_manager;
grant select on resto_view_ord to restaurant_manager;

DROP USER IF EXISTS ticket_seller;
create user ticket_seller with password 'ticket_seller';

Drop view if exists customer_id_update;
create view customer_id_update as select customer_id from customer;

grant select on theatre,ticket,bought_by,plays,screens,show to ticket_seller;
grant select, update, delete on customer_id_update to ticket_seller;

DROP USER IF EXISTS owner1;
create user owner1 with password 'owner1';

grant ALL on database moviebooking to owner1;