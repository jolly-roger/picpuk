create or replace function todo_user_set_isshared()
returns trigger
as
$body$
begin
    if new.is_owner = false then
        update todo set is_shared = true where id_todo = new.todo_id;
    end if;
    
    return null;
end;
$body$
language plpgsql;


create trigger todo_user_insert_set_isshared
    after insert
    on todo_user
    for each row
    execute procedure todo_user_set_isshared();