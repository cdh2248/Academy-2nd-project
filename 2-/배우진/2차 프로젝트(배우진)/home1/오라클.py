import cx_Oracle
import pandas as pd
from datetime import datetime, timedelta

def preprocessed_df_to_oracle(df):
    # con = cx_Oracle.connect('bwj917/1111@14.55.241.104:1521/xe')
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()

    for i in range(len(df)):
        sql_insert = '''
            insert into rains(baseDate, fcstDate, nx, ny, 강수량 , 강수확률, 기온) 
            values(:baseDate, :fcstDate, :nx, :ny, :PCP, :POP,:TMP)
            '''
        baseDate = datetime.strptime(df.iloc[i]['baseDate'], "%Y%m%d%H%M")
        fcstDate = datetime.strptime(df.iloc[i]['fcstDate'], "%Y%m%d%H%M")
        nx = int(df.iloc[i]['nx'])
        ny = int(df.iloc[i]['ny'])
        PCP = float(df.iloc[i]['강수량'])
        POP = float(df.iloc[i]['강수확률'])
        TMP = float(df.iloc[i]['기온'])

        cur.execute(sql_insert,
                 (baseDate, fcstDate, nx, ny, PCP, POP, TMP)
                 )
    print('오라클 저장 완료!')
    con.commit()
    cur.close()
    con.close()

def preprocessed_df_to_oracle2(df):
    # con = cx_Oracle.connect('bwj917/1111@14.55.241.104:1521/xe')
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()

    for i in range(len(df)):
        sql_insert = '''
            insert into rains2(baseDate, fcstDate, nx, ny, 강수량 , 강수확률, 기온) 
            values(:baseDate, :fcstDate, :nx, :ny, :PCP, :POP,:TMP)
            '''
        baseDate = datetime.strptime(df.iloc[i]['baseDate'], "%Y%m%d%H%M")
        fcstDate = datetime.strptime(df.iloc[i]['fcstDate'], "%Y%m%d%H%M")
        nx = int(df.iloc[i]['nx'])
        ny = int(df.iloc[i]['ny'])
        PCP = float(df.iloc[i]['강수량'])
        POP = float(df.iloc[i]['강수확률'])
        TMP = float(df.iloc[i]['기온'])

        cur.execute(sql_insert,
                 (baseDate, fcstDate, nx, ny, PCP, POP, TMP)
                 )
    print('오라클 저장 완료!')
    con.commit()
    cur.close()
    con.close()



def select_from_oracle(new_nx,new_ny):
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    # con = cx_Oracle.connect('bwj917/1111@14.55.241.104:1521/xe')
    cur = con.cursor()
    column_list_ra = ['baseDate', 'fcstDate', 'nx', 'ny', '강수량', '강수확률','기온']
    data = []
    sql_select = '''
            SELECT * FROM rains WHERE nx = :nx_val AND ny = :ny_val
             '''
    # SELECT * FROM rains WHERE nx = 67 AND ny = 137
    rs = cur.execute(sql_select, nx_val=new_nx,ny_val=new_ny)

    for record in rs:
        row=[]
        for source in range(0, len(record)):
            row.append(record[source])
        data.append(row)
    ra_df = pd.DataFrame(data, columns=column_list_ra)
    con.commit()
    cur.close()
    con.close()
    return ra_df

def select_from_oracle2(new_nx,new_ny):
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    # con = cx_Oracle.connect('bwj917/1111@14.55.241.104:1521/xe')
    cur = con.cursor()
    column_list_ra = ['baseDate', 'fcstDate', 'nx', 'ny', '강수량', '강수확률','기온']
    data = []
    sql_select = '''
            SELECT * FROM rains2 WHERE nx = :nx_val AND ny = :ny_val
             '''
    # SELECT * FROM rains WHERE nx = 67 AND ny = 137
    rs = cur.execute(sql_select, nx_val=new_nx,ny_val=new_ny)

    for record in rs:
        row=[]
        for source in range(0, len(record)):
            row.append(record[source])
        data.append(row)
    ra_df = pd.DataFrame(data, columns=column_list_ra)
    con.commit()
    cur.close()
    con.close()
    return ra_df

def new_oracle():
    # con = cx_Oracle.connect('bwj917/1111@14.55.241.104:1521/xe')
    print("왔는가")
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()
    drop_table = '''
            drop table rains2
        '''

    create_table_query = '''
        CREATE TABLE rains2 (
            BASEDATE DATE,
            FCSTDATE DATE,
            NX NUMBER,
            NY NUMBER,
            강수량 NUMBER,
            강수확률 NUMBER,
            기온 NUMBER
        )
    '''

    cur.execute(drop_table)
    print("rains2 삭제 완료")
    cur.execute(create_table_query)

    print('rains2 생성 완료!')
    con.commit()
    cur.close()
    con.close()