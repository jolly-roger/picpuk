CREATE OR REPLACE FUNCTION getresources(outeruserid varchar(128))
 RETURNS setof resource
AS $BODY$
BEGIN
    return query select r.*
        from resource as r
        inner join user_resource as ur
            on r.id_resource = ur.resource_id
        where ur.user_id = (select * from getuserid(outeruserid)) and r.is_removed = false;
END;
$BODY$
  LANGUAGE plpgsql;