CREATE OR REPLACE FUNCTION getuserpics(outeruserid varchar(128)) returns setof pic AS
$BODY$
BEGIN
    return query select * from pic where user_id = (select * from getuserid(outeruserid));
END;
$BODY$
  LANGUAGE plpgsql;