source blog
{{
    type      = {database.type}
    sql_host  = {database.host}
    sql_user  = {database.user}
    sql_pass  = {database.password}
    sql_db    = {database.name}
    sql_port  = {database.port}

    sql_query = SELECT id, title, body FROM articles
}}

indexer blog
{{
    source = blog
    path   = {index_path}/blog
}}

searchd
{{
    listen   = {host}:{port}
    log      = {log_path}/searchd.log
    pid_file = {pid_file}
}}