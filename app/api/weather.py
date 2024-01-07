from flask import Blueprint, request, jsonify
import requests
import xmltodict
from datetime import datetime

bp = Blueprint('weather', __name__, url_prefix='/weather')

@bp.route('/', methods=['GET'])
def get_weather():
    values = {
        'POP': '강수확률',
        'PTY': '강수형태',
        'PCP': '1시간 강수량',
        'REH': '습도',
        'SNO': '1시간 신적설',
        'SKY': '하늘상태',
        'TMP': '1시간 기온',
        'TMN': '일 최저기온',
        'TMX': '일 최고기온',
        'UUU': '풍속(동서성분)',
        'VVV': '풍속(남북성분)',
        'WAV': '파고',
        'VEC': '풍향',
        'WSD': '풍속',
        'T1H': '기온',
        'RN1': '1시간 강수량',
        'SKY': '하늘상태',
        'LGT': '낙뢰',
    }

    current_date = datetime.now()

    date = current_date.date().strftime("%Y%m%d")
    time = current_date.time().strftime("%H%M")

    response = requests.get(f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?ServiceKey=itjde0Gu8qwR%2FBOyEoxWD1L%2Fy6FmbK8E34wGcdGVxNRFNhe4v4NNAeMONUDFyChoKf6ih14CugCbreFwp4fbpg%3D%3D&numOfRows=10&pageNo=1&base_date={date}&base_time=0800&nx=54&ny=124')

    json_date = xmltodict.parse(response.text)
    items = []

    for i in range(len(json_date['response']['body']['items']['item'])):
        search_value = [values.get(key, []) for key in values.keys() if key == json_date['response']['body']['items']['item'][i]['category']]
        obsr_value = [json_date['response']['body']['items']['item'][i]['obsrValue']]
        item = [search_value[0], obsr_value[0]]
        items.append(item)


    return jsonify({
        "result": "success",
        "message": "날씨 조회 성공",
        "items": [
            {
                "category": item[0],
                "obsrValue": item[1]
            }
            for item in items
        ]
    }), 200
