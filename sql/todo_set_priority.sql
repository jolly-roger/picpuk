create or replace function set_priority(todoid bigint, todopriority integer)
returns boolean
as
$body$
declare
    local_user_id bigint;
begin
    select into local_user_id id_user from "user" as u
    inner join todo_user as tu
        on u.id_user = tu.user_id
    inner join todo as t
        on tu.todo_id = t.id_todo
    where t.id_todo = todoid limit 1;

    update todo
    set priority = priority + 1
    where id_todo <> todoid and priority >= todopriority and
        status_id = (select status_id from todo where id_todo = todoid) and
        id_todo in (select id_todo from todo t0         
            inner join todo_user as tu
                on t0.id_todo = tu.todo_id and tu.is_owner = true and tu.user_id = local_user_id);
    
    return null;
end;
$body$
    language plpgsql;


create or replace function todo_user_set_priority()
returns trigger
as
$body$
declare
    local_priority integer;
begin
    if new.is_owner = true then
        select into local_priority priority from todo where id_todo = new.todo_id;
    
        perform set_priority(new.todo_id, local_priority);
    end if;
    
    return null;
end;
$body$
    language plpgsql;


--create or replace function todo_set_priority()
--returns trigger
--as
--$body$
--begin
--
--    RAISE NOTICE 'id_todo %', new.id_todo;
--    RAISE NOTICE 'priority %', new.priority;  
--
--    perform set_priority(new.id_todo, new.priority);
--    
--    return null;
--end;
--$body$
--    language plpgsql;
    
    
    
    
    --update todo
    --set priority = priority + 1
    --where id_todo <> 180 and priority >= 0 and
    --    status_id = (select status_id from todo where id_todo = 180) and
    --    id_todo in (select id_todo from todo t0         
    --        inner join todo_user as tu
    --            on t0.id_todo = tu.todo_id and tu.is_owner = true and tu.user_id = 4);
    
    
    
    
create or replace function todo_update_priority()
returns trigger
as
$body$
begin
    if old.priority <> new.priority then
        perform set_priority(new.id_todo, new.priority);
    end if;
    
    return null;
end;
$body$
    language plpgsql;
    
    
create trigger todo_update_update_priority
    after update
    on todo
    for each row
    execute procedure todo_update_priority();
    

create trigger todo_user_insert_set_priority
    after insert
    on todo_user
    for each row
    execute procedure todo_user_set_priority();