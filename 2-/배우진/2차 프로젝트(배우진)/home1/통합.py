from 단기예보 import get_request_url;
from 전처리 import json_to_df_info,websocket_rains;
from 오라클 import preprocessed_df_to_oracle,select_from_oracle;

#== 베이스 좌표 == 한개의 좌표에 대해서만 확인하고 싶을 때
x = [67]
y = [137]



#############################################################################
#####   ######   ###########   #########  #####  ######  #######  ###########
####  #  ####  #  #########     ########  #####  #  ###  #######  ###########
###  ##  ###  ##  ########  ###  #######  #####  ##  ##  #######  ###########
##  ####  #  ####  ######         ######  #####  ###  #  ####################
#  ######  #######  ####   #####   #####  #####  ####    #######  ###########
#############################################################################

# ============== 요청 날씨 제이슨으로 받아보고 확인하고 싶을 때 실행 ================
# print(get_request_url(x,y))

# ============== 제이슨을 전처리하여 테이블로 만든 걸 확인하고 싶을 때 실행 ==========
# print(json_to_df_info(get_request_url(x,y)))


#=============== 현재 날씨 정보를 받아 전처리 후 오라클에 저장 ====================
# preprocessed_df_to_oracle(json_to_df_info(get_request_url(x,y)))

# ============== 오라클에 저장된 날씨 데이터를 뽑아올 때 ==========================
# print(select_from_oracle())

# ============== 데이터 테이블 차트에 보내기 위해 전처리 ==========================
# websocket_rains(select_from_oracle())


# f_dict = categorys.to_dict(orient='records')