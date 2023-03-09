from pipelines import tasks, Pipeline


NAME = 'test_project'
VERSION = '2023'


TASKS = [
    tasks.LoadFile(input_file='original/original.csv', table='original'),
    
    tasks.CTAS(
        table='norm',
        sql_query='''
            select *, domain_of_url(url)
            from {original};
        '''
    ),
    tasks.CopyToFile(
        table='norm',
        output_file='norm',
    ),

    # tasks.RunSQL("create TABLE original(id, name, url)"),
    # tasks.RunSQL("create TABLE norm(id, name, url, domain_of_url)"),
    
    # tasks.RunSQL("insert INTO original VALUES(1, 'hello', 'http://hello.com/home')"),
    
    # clean up:
    # tasks.RunSQL('drop table original'),
    # tasks.RunSQL('drop table norm'),
]


pipeline = Pipeline(
    name=NAME,
    version=VERSION,
    tasks=TASKS
)


if __name__ == "__main__":
    # 1: Run as script
    pipeline.run()

    # 2: Run as CLI
    # > pipelines run
