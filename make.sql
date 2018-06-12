use main;

create table sample_user(
id int auto_increment primary key,
email varchar(100),
password varchar(100),
regist_date datetime default now(),
modify_date datetime default null
);
