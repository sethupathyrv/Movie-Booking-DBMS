\c moviebooking

INSERT into theatre(theatre_id,theatre_name,city,state) values('6789','pvr','bangalore','karnataka');
INSERT into theatre(theatre_id,theatre_name,city,state) values('6780','inox','bangalore','karnataka');
INSERT into theatre(theatre_id,theatre_name,city,state) values('6781','navrang theatre','bangalore','karnataka');
INSERT into theatre(theatre_id,theatre_name,city,state) values('6782','pvr','bangalore','karnataka');
INSERT into theatre(theatre_id,theatre_name,city,state) values('6783','imax','bangalore','karnataka');

INSERT into show(show_id,language,genre,subtitles,show_name,timing,date) values('2345','English','Scifi','yes','Eternals','12:00:00','2021-11-08');
INSERT into show(show_id,language,genre,subtitles,show_name,timing,date) values('3345','Tamil','Legal Drama','yes','Jai Bhim','23:00:00','2021-11-09');
INSERT into show(show_id,language,genre,subtitles,show_name,timing,date) values('4345','Hindi','Biographical','no','Sardar Udham','09:30:00','2021-11-10');
INSERT into show(show_id,language,genre,subtitles,show_name,timing,date) values('5345','English','Action Thriller','yes','Wrath Of Man','08:45:00','2021-11-11');
INSERT into show(show_id,language,genre,subtitles,show_name,timing,date) values('6345','Hindi','Action Thriller','yes','Sherni','13:30:00','2021-11-12');

INSERT into customer(customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) values('1111','Shanegg','Shane','Shane','Hansel','Mendon','shanemendon@gmail.com','8971750423','02-05-2001','M');
INSERT into customer(customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) values('1112','rahul101','Rahul','Rahul','Srinivas','Manjunath','rsrimanj@gmail.com','7536490234','03-08-1997','M');
INSERT into customer(customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) values('1113','ram22','Ram','Ram','Govind','Preetham','rgopreeth@gmail.com','8753490234','09-02-2000','M');
INSERT into customer(customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) values('1114','shettyRocks','Shilpitha','Shilpitha','R','Shetty','shilpithshetty@gmail.com','8150889998','12-04-2001','F');
INSERT into customer(customer_id,username,password,first_name,middle_name,last_name,email_id,phone_no,dob,gender) values('1115','sethu21','Sethupathy','Sethupathy','R','Venkataraman','sethupathyrv@gmail.com','9113855415','01-01-2001','M');

INSERT into food_cart(order_id,orders,theatre_id) values('1121','Masala Dosa','6789');
INSERT into food_cart(order_id,orders,theatre_id) values('1122','Roti Curry','6780');
INSERT into food_cart(order_id,orders,theatre_id) values('1123','Pasta','6781');
INSERT into food_cart(order_id,orders,theatre_id) values('1124','Nachos','6782');
INSERT into food_cart(order_id,orders,theatre_id) values('1125','Popcorn','6783');

INSERT into bill(bill_id,charges,order_id) values('1131','200','1121'); 
INSERT into bill(bill_id,charges,order_id) values('1132','100','1122');
INSERT into bill(bill_id,charges,order_id) values('1133','300','1123');
INSERT into bill(bill_id,charges,order_id) values('1134','250','1124');
INSERT into bill(bill_id,charges,order_id) values('1135','150','1125');

INSERT into Food(food_id,food_name,food_price,food_type,order_id,bill_id) values('1141','Masala Dosa','50','Indian Breakfast','1121','1131');
INSERT into Food(food_id,food_name,food_price,food_type,order_id,bill_id) values('1142','Roti Curry','100','Indian Lunch','1122','1132');
INSERT into Food(food_id,food_name,food_price,food_type,order_id,bill_id) values('1143','Pasta','100','Italian Lunch','1123','1133');
INSERT into Food(food_id,food_name,food_price,food_type,order_id,bill_id) values('1144','Nachos','50','Snack','1124','1134');
INSERT into Food(food_id,food_name,food_price,food_type,order_id,bill_id) values('1145','Popcorn','50','Snack','1125','1135');

INSERT into plays(theatre_id,show_id) values('6789','2345');
INSERT into plays(theatre_id,show_id) values('6780','3345');
INSERT into plays(theatre_id,show_id) values('6781','4345');
INSERT into plays(theatre_id,show_id) values('6782','5345');
INSERT into plays(theatre_id,show_id) values('6783','6345');

INSERT into screens(screen_id,vacant_seats,show,time,date,screen_no,cost,theatre_id,show_id) values('1152','30','Jai Bhim','23:00:00','2021-11-09','2','400','6780','3345');
INSERT into screens(screen_id,vacant_seats,show,time,date,screen_no,cost,theatre_id,show_id) values('1154','32','Wrath Of Man','08:45:00','2021-11-11','3','350','6782','5345');
INSERT into screens(screen_id,vacant_seats,show,time,date,screen_no,cost,theatre_id,show_id) values('1151','40','Eternals','12:00:00','2021-11-08','1','500','6789','2345');
INSERT into screens(screen_id,vacant_seats,show,time,date,screen_no,cost,theatre_id,show_id) values('1153','25','Eternals','09:30:00','2021-11-10','1','450','6781','2345');
INSERT into screens(screen_id,vacant_seats,show,time,date,screen_no,cost,theatre_id,show_id) values('1155','49','Eternals','13:30:00','2021-11-12','2','300','6783','2345');

INSERT into ticket(ticket_id,seat_no,show_date,theatre_id,show_id,customer_id,screen_id) values('1161','11','2021-11-08','6789','2345','1111','1151');  
INSERT into ticket(ticket_id,seat_no,show_date,theatre_id,show_id,customer_id,screen_id) values('1162','12','2021-11-09','6780','3345','1112','1152');  
INSERT into ticket(ticket_id,seat_no,show_date,theatre_id,show_id,customer_id,screen_id) values('1163','21','2021-11-10','6781','4345','1113','1153');  
INSERT into ticket(ticket_id,seat_no,show_date,theatre_id,show_id,customer_id,screen_id) values('1164','22','2021-11-11','6782','5345','1114','1154');  
INSERT into ticket(ticket_id,seat_no,show_date,theatre_id,show_id,customer_id,screen_id) values('1165','42','2021-11-12','6783','6345','1115','1155');  

INSERT into bought_by(customer_id,show_id,booking_date) values('1111','2345','2021-11-07');
INSERT into bought_by(customer_id,show_id,booking_date) values('1112','3345','2021-11-08');
INSERT into bought_by(customer_id,show_id,booking_date) values('1113','4345','2021-11-09');
INSERT into bought_by(customer_id,show_id,booking_date) values('1114','5345','2021-11-10');
INSERT into bought_by(customer_id,show_id,booking_date) values('1115','6345','2021-11-09');


