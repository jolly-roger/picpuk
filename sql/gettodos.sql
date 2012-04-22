create or replace type todo_status as (
    id_todo integer,
    name varchar(256),
    status_id integer,
    status_name varchar(50),
    is_shared boolean,
    priority integer
);


CREATE OR REPLACE FUNCTION gettodos(userid bigint, statusid bigint, isowner boolean, excludestatus boolean,
    isshared boolean, excludeisshared boolean)
returns setof todo_status
AS
$BODY$
BEGIN
    return query select t.id_todo, t.name, t.status_id, s.name as status_name, t.is_shared, t.priority
        from todo as t
        inner join status as s
            on t.status_id = s.id_status
        inner join todo_user as tu
            on t.id_todo = tu.todo_id and tu.is_owner = isowner
        inner join "user" as u
            on tu.user_id = u.id_user and u.facebook_user_id = userid
        where (case when excludestatus then t.status_id <> statusid else t.status_id = statusid end) and
            (case when excludeisshared then true else t.is_shared = isshared end)
        order by t.priority asc;
END;
$BODY$
  LANGUAGE plpgsql;