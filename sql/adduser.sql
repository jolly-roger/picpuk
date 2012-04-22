CREATE OR REPLACE FUNCTION adduser(outeruserid varchar(128))
 RETURNS boolean
AS $BODY$
BEGIN
    if not (case when (select true from "user" where outer_user_id = outeruserid limit 1) then true else false end) then
        insert into "user"(outer_user_id) values(outeruserid);
    end if;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;