from DBcm import UseDatabase


def work_with_db(dbconfig: dict, _sql: str):
    with UseDatabase(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        else:
            cursor.execute(_SQL)
            stud_result = cursor.fetchall()

        return stud_result


if __name__ == '__main__':

    group_index = 'РК6-41'
    dbconfig = {'host': '127.0.0.1', 'user': 'root', 'password': 'root', 'database': 'decanat'}
    _SQL = f"""select s_name,birthday from Student join s_group using(g_id)
          where g_index='{group_index}'"""
    result = work_with_db(dbconfig, _SQL)
    if result:
        for line in result:
            print(line[0], line[1])
    else:
        print('Результат не получен')

