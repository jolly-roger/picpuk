CREATE OR REPLACE FUNCTION addresource(resourcealias varchar(256), resourcedomain varchar(256),
    outeruserid varchar(128))
 RETURNS bigint
AS $BODY$
declare
    new_resource_id bigint;
    local_user_id bigint;
    local_priority integer;
BEGIN
    insert into resource ("alias", "domain") values (resourcealias, resourcedomain) returning id_resource
        into new_resource_id;
    insert into user_resource values (new_resource_id, (select * from getuserid(outeruserid)));
    
    return new_resource_id;
END;
$BODY$
  LANGUAGE plpgsql;