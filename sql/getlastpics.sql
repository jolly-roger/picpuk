CREATE OR REPLACE FUNCTION getlastpics(picscpunt int)
 RETURNS setof pic
AS $BODY$
BEGIN
    return query select * from pic order by id_pic desc limit picscpunt;
END;
$BODY$
  LANGUAGE plpgsql;