CREATE OR REPLACE FUNCTION getuserid(outeruserid varchar(128)) returns numeric AS
$BODY$
declare
    local_id_user numeric;
BEGIN
    if not (case when (select true from "user" where outer_user_id = outeruserid limit 1) then true else false end) then
        insert into "user"(outer_user_id) values(outeruserid);
    end if;
    
    select into local_id_user id_user from "user" where outer_user_id = outeruserid limit 1;
    
    return local_id_user;
END;
$BODY$
  LANGUAGE plpgsql;