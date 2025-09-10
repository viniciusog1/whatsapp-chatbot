import oracledb

def db_connection():
    oracledb.init_oracle_client()  # se necessário, ajuste o path do cliente

    dsn = oracledb.makedsn(
        host='172.16.18.8',
        port=1521,
        service_name='WINT'
    )

    connection = oracledb.connect(
        user='CONSULTA2',
        password='z3355df#2023',
        dsn=dsn
    )
    return connection
