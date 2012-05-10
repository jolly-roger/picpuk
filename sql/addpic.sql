CREATE OR REPLACE FUNCTION addpic(outeruserid varchar(128))
 RETURNS boolean
AS $BODY$
declare
    local_id_pic numeric;
BEGIN
    insert into pic (user_id) values ((select * from getuserid(outeruserid))) returning id_pic into local_id_pic;

    return local_id_pic;
END;
$BODY$
  LANGUAGE plpgsql;