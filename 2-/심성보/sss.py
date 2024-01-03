import requests

key1= 'YVTIX7fPjJ+JLD86Xp4wLyDkekN5ui0MHobPBg4mEPE6cSKTF+MMBXcn24ONks/Nxq7b8TfHChk1+4p5Oq9ECA=='
key2='Jq8rDZ5aUrkjhKzqHYNBsu+UDXwfbVvWORbxvUBSM5yvH8dAybf29/H6yahrMC4DsUbSST97H5ObfeFr2UVTuw=='
key3='Jq8rDZ5aUrkjhKzqHYNBsu%2BUDXwfbVvWORbxvUBSM5yvH8dAybf29%2FH6yahrMC4DsUbSST97H5ObfeFr2UVTuw%3D%3D'
key4='HVgh0GJtfha0bssIG8/oBb7dkuTWWgOnt3o47r4Wa1/SrD6VRDqJ0cOzT/6T4vL3KX4JV0bKzNZl9WqYpOdLJg=='

url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
params ={'serviceKey' : key4, 'pageNo' : '1', 'numOfRows' : '100', 'type' : 'xml', 'fstvlNm' : '', 'opar' : '', 'fstvlStartDate' : '', 'fstvlEndDate' : '', 'fstvlCo' : '', 'mnnst' : '', 'auspcInstt' : '', 'suprtInstt' : '', 'phoneNumber' : '', 'homepageUrl' : '', 'relateInfo' : '', 'rdnmadr' : '', 'lnmadr' : '', 'latitude' : '', 'longitude' : '', 'referenceDate' : '', 'instt_code' : '' }

response = requests.get(url, params=params)
print(response.content)



