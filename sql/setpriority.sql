create or replace function setpriority(todoid bigint, todopriority integer)
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
    set priority = todopriority
    where id_todo = todoid;

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