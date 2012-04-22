CREATE OR REPLACE FUNCTION verifyresource(resourceid bigint)
 RETURNS boolean
AS $BODY$
BEGIN
    update resource set is_verified = true where id_resource = resourceid;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;