from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

__all__ = [
    "Event",
    "NcaParams",
    "NcaParty",
    "Abo",
    "SurveyQuestionType",
    "SurveyResponseType",
    "NcaSurveyResponse",
    "NcaNode",
    "AboResponse",
    "AboMaster",
    "SurveyTerms"
]

Event = Dict[str, Any]


@dataclass
class NcaParams:
    nca_event: str
    series: Optional[int] = None
    abo_id: Optional[str] = None
    abo_name: Optional[str] = None
    phone: Optional[str] = None
    event_date_from: Optional[str] = None
    event_time_from: Optional[int] = None
    event_minute_from: Optional[int] = None
    event_date_to: Optional[str] = None
    event_time_to: Optional[int] = None
    event_minute_to: Optional[int] = None
    apply_date_from: Optional[str] = None
    apply_time_from: Optional[int] = None
    apply_minute_from: Optional[int] = None
    apply_date_to: Optional[str] = None
    apply_time_to: Optional[int] = None
    apply_minute_to: Optional[int] = None
    activity_date_from: Optional[str] = None
    activity_time_from: Optional[int] = None
    activity_minute_from: Optional[int] = None
    activity_date_to: Optional[str] = None
    activity_time_to: Optional[int] = None
    activity_minute_to: Optional[int] = None

    @property
    def event_modification_date_from(self) -> Optional[str]:
        if not self.event_date_from:
            return None

        split = [int(s) for s in self.event_date_from.split("-")] + \
                [
                    self.event_time_from if self.event_time_from is not None else 0,
                    self.event_minute_from if self.event_minute_from is not None else 0
                ]

        return NcaParams._parse_datetime(split)

    @property
    def event_modification_date_to(self) -> Optional[str]:
        if not self.event_date_to:
            return None

        split = [int(s) for s in self.event_date_to.split("-")] + \
                [
                    self.event_time_to if self.event_time_to is not None else 0,
                    self.event_minute_to if self.event_minute_to is not None else 0,
                ]

        return NcaParams._parse_datetime(split)

    @property
    def apply_modification_date_from(self) -> Optional[str]:

        if not self.apply_date_from:
            return None

        split = [int(s) for s in self.apply_date_from.split("-")] + \
                [
                    self.apply_time_from if self.apply_time_from is not None else 0,
                    self.apply_minute_from if self.apply_minute_from is not None else 0
                ]

        return NcaParams._parse_datetime(split)

    @property
    def apply_modification_date_to(self) -> Optional[str]:

        if not self.apply_date_to:
            return None

        split = [int(s) for s in self.apply_date_to.split("-")] + \
                [
                    self.apply_time_to if self.apply_time_to is not None else 0,
                    self.apply_minute_to if self.apply_minute_to is not None else 0,
                ]

        return NcaParams._parse_datetime(split)

    @property
    def activity_modification_date_from(self) -> Optional[str]:

        if not self.activity_date_from:
            return None

        split = [int(s) for s in self.activity_date_from.split("-")] + \
                [
                    self.activity_time_from if self.activity_time_from is not None else 0,
                    self.activity_minute_from if self.activity_minute_from is not None else 0
                ]

        return NcaParams._parse_datetime(split)

    @property
    def activity_modification_date_to(self) -> Optional[str]:

        if not self.activity_date_to:
            return None

        split = [int(s) for s in self.activity_date_to.split("-")] + \
                [
                    self.activity_time_to if self.activity_time_to is not None else 0,
                    self.activity_minute_to if self.activity_minute_to is not None else 0,
                ]

        return NcaParams._parse_datetime(split)

    @staticmethod
    def _parse_datetime(split_date: List[int]) -> str:
        year = split_date[0]
        month = split_date[1]
        day = split_date[2]
        hour = split_date[3]
        minute = split_date[4]

        return datetime(year, month, day, hour, minute).isoformat().replace("T", " ")


@dataclass
class NcaParty:
    sr_seq: int
    s_code: str
    wave_number: int
    abo_uid: str
    name: str
    user_type_code: str
    user_type: str
    attendance_yn: str
    creation_time: str
    modification_time: str
    info_modification_time: Optional[str] = None
    info_revision_time: Optional[str] = None
    activity_modification_time: Optional[str] = None
    activity_revision_time: Optional[str] = None
    schedule_modification_time: Optional[str] = None
    schedule_revision_time: Optional[str] = None
    phone: Optional[str] = None
    is_native: Optional[str] = None
    social_id: Optional[str] = None
    english_name: Optional[str] = None
    gender_code: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    passport_id: Optional[str] = None
    passport_issued_date: Optional[str] = None
    passport_expiration_date: Optional[str] = None
    safety_confirm: Optional[str] = None
    passport: Optional[str] = None
    safety_agreement: Optional[str] = None
    portrait_right: Optional[str] = None
    family_certificate: Optional[str] = None
    non_abo_spouse: Optional[str] = None
    terms_first: Optional[str] = None
    terms_first_agreed_date: Optional[str] = None
    terms_second: Optional[str] = None
    terms_second_agreed_date: Optional[str] = None
    terms_third: Optional[str] = None
    terms_third_agreed_date: Optional[str] = None
    terms_fourth: Optional[str] = None
    terms_fourth_agreed_date: Optional[str] = None
    terms_fifth: Optional[str] = None
    terms_fifth_agreed_date: Optional[str] = None
    activity_day_third: Optional[str] = None
    activity_day_fourth: Optional[str] = None
    activity_day_fifth: Optional[str] = None
    homecoming_date: Optional[str] = None
    allergy: Optional[str] = None
    visa_eta: Optional[str] = None
    visa_num: Optional[str] = None
    visa_expiration_date: Optional[str] = None


class Abo:

    def __init__(self):
        self.first = None
        self.second = None


class SurveyQuestionType(Enum):
    A = "객관식"
    B = "주관식"
    F = "첨부"


class SurveyResponseType(Enum):
    E = "단독사업자"
    P1 = "공동사업자1"
    P2 = "공동사업자2"
    S = "비사업배우자"
    F = "가족"

    @staticmethod
    def find_by_name(name: str) -> "SurveyResponseType":
        return next(filter(lambda x: x.name == name, iter(SurveyResponseType)))


@dataclass
class AboMaster:
    abo_uid: str
    wave_number: int


@dataclass(init=False)
class AboResponse:
    response_code: int
    abo_uid: str
    name: str
    user_type: str
    creation_time: datetime
    attendance_yn: str
    payment_yn: Optional[str] = None
    payment_type: Optional[str] = None
    payment_remark: Optional[str] = None
    modification_time: Optional[datetime] = None
    info_modification_time: Optional[datetime] = None
    activity_modification_time: Optional[datetime] = None
    schedule_modification_time: Optional[datetime] = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass(init=False)
class NcaSurveyResponse:
    question_code: str
    question_type: str  # A | B | F -> show SurveyQuestionType
    question: str
    answer: Union[str, int, datetime, None]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


family_relation: Dict[str, str] = {
    "F1": "(1촌) 아버지",
    "F2": "(1촌) 어머니",
    "F3": "(2촌) 조부모 (할아버지, 할머니)",
    "F4": "(2촌) 외조부모 (외할아버지, 외할머니)",
    "F5": "(2촌) 형제 (형, 오빠, 남동생)",
    "F6": "(2촌) 자매 (누나, 언니, 여동생)",
    "F7": "(2촌) 손자녀 (손자, 손녀)",
    "F8": "(2촌) 손자녀의 배우자 (손자며느리, 손자사위)",
    "F9": "(3촌) 증조부모 (증조 할아버지, 증조 할머니)",
    "F10": "(3촌) 외증조부모 (외증조 할아버지, 외증조 할머니)",
    "F11": "(3촌) 증손자녀 (증손자, 증손녀)",
    "F12": "(3촌) 증손자녀의 배우자 (증손자며느리,증 손자사위)",
    "F13": "(3촌) 형제·자매의 자녀 (조카)",
    "F14": "(3촌) 아버지의 형제 (큰아버지, 작은아버지)",
    "F15": "(3촌) 아버지 형제의 배우자(큰어머니, 작은어머니)",
    "F16": "(3촌) 아버지의 누이 (고모)",
    "F17": "(3촌) 아버지 누이의 배우자 (고모부)",
    "F18": "(3촌) 어머니의 형제 (외삼촌)",
    "F19": "(3촌) 어머니 형제의 배우자 (외숙모)",
    "F20": "(3촌) 어머니의 자매 (이모)"
}


@dataclass
class SurveyTerms:
    terms_code: int
    title: str
    required: bool
    agreed: bool


@dataclass(init=False)
class NcaNode:
    survey_code: str
    wave_number: int
    abo_uid: str
    name: str
    user_type: str
    attendance_yn: str
    creation_time: datetime
    payment_yn: Optional[str] = None
    payment_type: Optional[str] = None
    payment_remark: Optional[str] = None
    terms: List[SurveyTerms] = field(default_factory=list)
    survey_responses: List[NcaSurveyResponse] = field(default_factory=list)
    modification_time: Optional[datetime] = None
    info_modification_time: Optional[datetime] = None
    activity_modification_time: Optional[datetime] = None
    schedule_modification_time: Optional[datetime] = None
    children: Optional[List["NcaNode"]] = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @staticmethod
    def _parse_datetime(value: Optional[datetime]) -> Optional[str]:
        return value.isoformat().replace("T", " ") if value is not None else None

    def flat(self) -> dict:
        result_dict = {}
        result_dict.setdefault("survey_code", self.survey_code)
        result_dict.setdefault("wave_number", self.wave_number)
        result_dict.setdefault("abo_uid", self.abo_uid)
        result_dict.setdefault("payment_yn", self.payment_yn)
        result_dict.setdefault("payment_type", self.payment_type)
        result_dict.setdefault("payment_remark", self.payment_remark)

        principal: Dict[str, Any] = {"user_type": SurveyResponseType.find_by_name(self.user_type).value}

        principal.setdefault("name", self.name)
        principal.setdefault("attendance_yn", self.attendance_yn)
        principal.setdefault("creation_time", NcaNode._parse_datetime(self.creation_time))
        principal.setdefault("modification_time", NcaNode._parse_datetime(self.modification_time))
        principal.setdefault("info_modification_time", NcaNode._parse_datetime(self.info_modification_time))
        principal.setdefault("activity_modification_time", NcaNode._parse_datetime(self.activity_modification_time))
        principal.setdefault("schedule_modification_time", NcaNode._parse_datetime(self.schedule_modification_time))

        for idx, response in enumerate(self.survey_responses):
            if "가족관계" == response.question and response.answer:
                response.answer = family_relation.get(response.answer)
            principal.setdefault(f"q{idx}", {"key": response.question, "answer": response.answer})

        result_dict.setdefault("principal", principal)

        if self.children is not None:
            for _idx, child in enumerate(self.children):
                family: Dict[str, Any] = {}
                key = ""

                family.setdefault("name", child.name)
                family.setdefault("attendance_yn", child.attendance_yn)
                family.setdefault("creation_time", NcaNode._parse_datetime(child.creation_time))
                family.setdefault("modification_time", NcaNode._parse_datetime(child.modification_time))
                family.setdefault("info_modification_time", NcaNode._parse_datetime(child.info_modification_time))
                family.setdefault("activity_modification_time",
                                  NcaNode._parse_datetime(child.activity_modification_time))
                family.setdefault("schedule_modification_time",
                                  NcaNode._parse_datetime(child.schedule_modification_time))

                if child.user_type == "P2" or child.user_type == "S":
                    key = "spouse"
                else:
                    key = f"family{_idx}"

                family.setdefault("user_type", SurveyResponseType.find_by_name(child.user_type).value)

                for __idx, _response in enumerate(child.survey_responses):
                    if "가족관계" == _response.question and _response.answer:
                        _response.answer = family_relation.get(_response.answer)
                    family.setdefault(f"q{__idx}", {"key": _response.question, "answer": _response.answer})

                result_dict.setdefault(key, family)

        return result_dict
