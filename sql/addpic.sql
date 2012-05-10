CREATE OR REPLACE FUNCTION addpic(userid numeric)
 RETURNS boolean
AS $BODY$
declare
    local_id_pic numeric;
BEGIN
    insert into pic (user_id) values (userid) returning id_pic into local_id_pic;

    return local_id_pic;
END;
$BODY$
  LANGUAGE plpgsql;