from pipelines import tasks, Pipeline


NAME = 'test_project'
VERSION = '2023'


TASKS = [
    # tasks.RunSQL("create TABLE original(id, name, url)"),
    # tasks.RunSQL("create TABLE norm(id, name, url, domain_of_url)"),
    
    # tasks.LoadFile(input_file='original/original.csv', table='original'),
    
    # tasks.RunSQL("CREATE FUNCTION dbo.domain_of_url(@url text) "
    #             + "RETURNS text "
    #             + "AS "
    #             + "BEGIN "
    #             + "DECLARE @one text; "
    #             + "SELECT @one = INSTR(@url,'\\') position; "
    #             + "DECLARE @two text; "
    #             + "SELECT @two = INSTR(@url,'\') position; "
    #             + "DECLARE @word text; "
    #             + "SELECT @word = SUBSTR(@url, @one + 1, @two - @one); "
    #             + "RETURN @word; "
    #             + "END;"),
    tasks.CTAS(
        table='norm',
        sql_query='''
            select *, domain_of_url(url)
            from original;
        '''
    ),
    # tasks.CopyToFile(
    #     table='norm',
    #     output_file='norm',
    # ),
    
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
