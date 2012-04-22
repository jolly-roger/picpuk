--create database queuetodo encoding 'utf-8' template template0;

create sequence id_todo_seq minvalue 0 start 0;


create table todo (
	id_todo integer primary key not null default nextval('id_todo_seq'),	
	name varchar(256)
);

