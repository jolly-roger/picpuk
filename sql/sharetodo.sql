CREATE OR REPLACE FUNCTION sharetodo(todoid bigint, friendid bigint) returns boolean AS
$BODY$
BEGIN
    insert into todo_user values (todoid, (select * from getuserid(friendid)), false);
    update todo set is_shared = true where id_todo = todoid;
    
    return true;
END;
$BODY$
  LANGUAGE plpgsql;