CREATE OR REPLACE FUNCTION addfbuser(fbuserid numeric)
 RETURNS boolean
AS $BODY$
BEGIN
    if not (case when (select true from "user" where facebook_user_id = fbuserid limit 1) then true else false end) then
        insert into "user"(facebook_user_id) values(fbuserid);
    end if;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;