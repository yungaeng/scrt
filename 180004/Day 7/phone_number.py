import re

# 지역 번호 리스트
area_codes = ['02', '031', '032', '033', '041', '042', '043', '044', '051', '052', '053', '054', '055', '061', '062',
              '063', '064']


def format_phone_number(phone_number):
    # 숫자를 제외한 모든 문자 제거
    phone_number = re.sub(r'[^0-9]', '', phone_number)

    # 핸드폰 번호인 경우
    if len(phone_number) == 10:
        formatted_number = re.sub(r'^(\d{3})(\d{3})(\d{4})$', r'\2 - \3', phone_number)
        return f'(010) {formatted_number}'

    # 지역 번호 + 전화번호인 경우
    elif len(phone_number) == 11:
        # 지역 번호 추출
        area_code = phone_number[0:3]
        if area_code not in area_codes:
            return 'Wrong Local Number'

        # 전화번호 추출
        phone_number = phone_number[3:]
        formatted_number = re.sub(r'^(\d{4})(\d{4})$', r'\1 - \2', phone_number)
        return f'({area_code}) {formatted_number}'

    # 잘못된 전화번호인 경우
    else:
        return 'Wrong Number'


print(format_phone_number('(031) 8041 - 0550'))   # (031) 8041-0550
print(format_phone_number('3533435'))             # (010) 353-3435
print(format_phone_number('34239872'))            # (010) 3424-9872
print(format_phone_number('353 3435'))            # (010) 353-3435
print(format_phone_number('01034243424'))         # (010) 3424-3424
print(format_phone_number('(031) - 8041 0123'))   # (031) 8041-0123
print(format_phone_number('(010) - 333 - 4444'))  # (010) 333-4444
print(format_phone_number('010333344444'))        # Wrong Number
print(format_phone_number('010-3333-444'))        # Wrong Number
print(format_phone_number('010 333 3444'))        # (010) 333-3444
print(format_phone_number('3542 - 8795'))         # (010) 3542-8795
print(format_phone_number('099 - 353 - 3435'))    # Wrong Local Number
print(format_phone_number('010 - 34 - 34554'))    # Wrong Number
print(format_phone_number('342498765'))           # Wrong Number
