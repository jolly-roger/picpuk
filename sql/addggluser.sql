CREATE OR REPLACE FUNCTION addggluser(ggluserid numeric)
 RETURNS boolean
AS $BODY$
BEGIN
    if not (case when (select true from "user" where google_user_id = ggluserid limit 1) then true else false end) then
        insert into "user"(google_user_id) values(ggluserid);
    end if;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;