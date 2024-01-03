import pandas as pd
import re

def json_to_df_info(raw_jsons):
    all_data = []
    column_list = ["baseDate","baseTime","category","fcstDate","fcstTime","fcstValue","nx","ny"]
    for raw_json in raw_jsons :
        for record in raw_json['response']['body']['items']['item']:
            row_data = []

            if record['category'] == 'POP' or record['category'] == 'PCP' or record['category'] =='TMP' :

                for column_data in column_list:
                    row_data.append(record.get(column_data))
                all_data.append(row_data)
    return category_df(column_list, all_data)


def category_df(column_list, all_data):
    df = pd.DataFrame(all_data, columns=column_list)

    df['fcstValue'] = df['fcstValue'].replace('강수없음', '0')
    df['fcstValue'] = df['fcstValue'].astype(str)
    df['fcstValue'] = df['fcstValue'].apply(lambda x: re.sub(r'[^\d.]', '', x))
    df['fcstValue'] = pd.to_numeric(df['fcstValue'])
    df = df.drop_duplicates(subset=['baseDate', 'baseTime', 'fcstDate', 'fcstTime', 'category', 'nx', 'ny'])
    pivoted_df = df.pivot(index=['baseDate', 'baseTime', 'fcstDate', 'fcstTime', 'nx', 'ny'],
                          columns='category',
                          values='fcstValue').reset_index()

    # Rename the pivoted columns if desired
    pivoted_df.rename(columns={'TMP': '기온', 'POP': '강수확률', 'PCP': '강수량'},
                      inplace=True)
    # pivoted_df['baseDateTime'] = pivoted_df['baseDate'].astype(str) + pivoted_df['baseTime'].astype(str)
    # pivoted_df['fcstDateTime'] = pivoted_df['fcstDate'].astype(str) + pivoted_df['fcstTime'].astype(str)
    pivoted_df['baseDate'] = pivoted_df['baseDate'].astype(str) + pivoted_df['baseTime'].astype(str)
    pivoted_df['fcstDate'] = pivoted_df['fcstDate'].astype(str) + pivoted_df['fcstTime'].astype(str)
    # Drop the separate baseDate and baseTime columns
    pivoted_df.drop(columns=['baseTime'], inplace=True)
    pivoted_df.drop(columns=['fcstTime'], inplace=True)

    return pivoted_df

def websocket_rains(df) :
    df['baseDate'] = df['baseDate'].astype(str)
    df['fcstDate'] = df['fcstDate'].astype(str)
    print(df)

    # df['fcstDate'] = df['fcstDate'].str[-4:-2]

    print(df.head(60))
    return df