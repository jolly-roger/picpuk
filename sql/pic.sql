create sequence id_pic_seq minvalue 0 start 0;


create table pic (
	id_pic bigint primary key not null default nextval('id_pic_seq'),	
	user_id bigint
);

create index "pic_user_id_idx" on pic (user_id);