from urllib.parse import urlencode, urlunparse

# 주어진 URL
# url = "http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api{'serviceKey' : 'bwc3DJ6DBSdRpgK4ZBeKvvb42M0KALQDAzhEhe8AkUP9nwc9VHoO5r6OxJfBrnuNK76bfwk2hAmqEJWaYL+4ag==', 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'xml', 'fstvlNm' : '', 'opar' : '', 'fstvlStartDate' : '', 'fstvlEndDate' : '', 'fstvlCo' : '', 'mnnst' : '', 'auspcInstt' : '', 'suprtInstt' : '', 'phoneNumber' : '', 'homepageUrl' : '', 'relateInfo' : '', 'rdnmadr' : '', 'lnmadr' : '', 'latitude' : '', 'longitude' : '', 'referenceDate' : '', 'instt_code' : ''}"
#
# # URL 파싱
# parsed_url = urlunparse(urlparse(url))
#
# # URL 인코딩
# encoded_url = parsed_url.encode('utf-8')
#
# # 파싱된 URL 출력
# print(encoded_url)
#

import requests
# 서비스키 bwc3DJ6DBSdRpgK4ZBeKvvb42M0KALQDAzhEhe8AkUP9nwc9VHoO5r6OxJfBrnuNK76bfwk2hAmqEJWaYL+4ag==
# 서비스키 bwc3DJ6DBSdRpgK4ZBeKvvb42M0KALQDAzhEhe8AkUP9nwc9VHoO5r6OxJfBrnuNK76bfwk2hAmqEJWaYL%2B4ag%3D%3D
# YVTIX7fPjJ+JLD86Xp4wLyDkekN5ui0MHobPBg4mEPE6cSKTF+MMBXcn24ONks/Nxq7b8TfHChk1+4p5Oq9ECA==
# YVTIX7fPjJ%2BJLD86Xp4wLyDkekN5ui0MHobPBg4mEPE6cSKTF%2BMMBXcn24ONks%2FNxq7b8TfHChk1%2B4p5Oq9ECA%3D%3D
url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
params ={'serviceKey' : 'YVTIX7fPjJ%2BJLD86Xp4wLyDkekN5ui0MHobPBg4mEPE6cSKTF%2BMMBXcn24ONks%2FNxq7b8TfHChk1%2B4p5Oq9ECA%3D%3D', 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'json', 'fstvlNm' : '', 'opar' : '', 'fstvlStartDate' : '', 'fstvlEndDate' : '', 'fstvlCo' : '', 'mnnst' : '', 'auspcInstt' : '', 'suprtInstt' : '', 'phoneNumber' : '', 'homepageUrl' : '', 'relateInfo' : '', 'rdnmadr' : '', 'lnmadr' : '', 'latitude' : '', 'longitude' : '', 'referenceDate' : '', 'instt_code' : '' }

response = requests.get(url, params=params)
print(response.content)