CREATE OR REPLACE FUNCTION addtodo(todoname varchar(256), userid bigint) returns boolean AS
$BODY$
declare
    new_todo_id bigint;
    local_user_id bigint;
    local_priority integer;
BEGIN
    insert into todo (name) values (todoname) returning id_todo into new_todo_id;
    insert into todo_user values (new_todo_id, (select * from getuserid(userid)));
    
    select into local_priority priority from todo where id_todo = new_todo_id;
    
    perform setpriority(new_todo_id, local_priority);
    
    return true;
END;
$BODY$
  LANGUAGE plpgsql;