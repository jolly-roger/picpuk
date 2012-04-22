CREATE OR REPLACE FUNCTION removeresource(resourceid bigint)
 RETURNS boolean
AS $BODY$
BEGIN
    update resource set is_removed = true where id_resource = resourceid;

    return true;
END;
$BODY$
  LANGUAGE plpgsql;