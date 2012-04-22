create sequence id_user_seq minvalue 0 start 0;


create table "user" (
	id_user bigint primary key not null default nextval('id_user_seq'),	
	facebook_user_id bigint
);

create index "user_facebook_user_id_idx" on "user" (facebook_user_id);