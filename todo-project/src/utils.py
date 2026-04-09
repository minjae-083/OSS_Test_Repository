"""유틸리티 함수 모듈"""

from datetime import datetime


def get_today():
    """오늘 날짜를 한국어 형식으로 반환"""
    now = datetime.now()
    return f"{now.year}년 {now.month}월 {now.day}일"


def format_date(date_str):
    """날짜 문자열을 한국어 형식으로 변환"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return f"{dt.year}년 {dt.month}월 {dt.day}일"
