CREATE OR REPLACE FUNCTION getusertodos(userid bigint, statusid bigint) returns setof todo AS
$BODY$
BEGIN
    return query select * from todo as t
        where t.id_todo in (select tu.todo_id from todo_user as tu
            where tu.user_id = (select id_user from "user" where facebook_user_id = userid)) and
        t.status_id = statusid;
END;
$BODY$
  LANGUAGE plpgsql;