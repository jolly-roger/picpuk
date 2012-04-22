create sequence id_resource_seq minvalue 0 start 0;


create table resource (
	id_resource bigint primary key not null default nextval('id_resource_seq'),	
	"alias" varchar(256) not null,
    "domain" varchar(256) not null,
    is_verified boolean not null default false
);


create table user_resource (
    resource_id bigint not null,
    user_id bigint not null,
    constraint fk_user_resource_resource foreign key (resource_id)
        references resource (id_resource),
    constraint fk_user_resource_user foreign key (user_id)
        references "user" (id_user)
);