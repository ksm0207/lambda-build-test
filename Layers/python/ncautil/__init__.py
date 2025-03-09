from typing import Tuple, Dict, Any, List

try:
    from typealias import Event, NcaParams, NcaParty, Abo
except ImportError:
    from Layers.python.typealias import Event, NcaParams, NcaParty, Abo


__all__ = ["nca_reduce"]


def nca_reduce(data: Tuple[Dict[str, Any]]) -> List[Abo]:
    uid_row_map: Dict[str, Dict[int, NcaParty]] = {}
    for row in data:

        party = NcaParty(**row)
        if not uid_row_map.get(party.abo_uid):
            uid_row_map.setdefault(party.abo_uid, {})

        key = party.sr_seq
        if party.user_type == "공동사업자1":
            party.user_type_code += "1"
        elif party.user_type == "공동사업자2":
            party.user_type_code += "2"

        uid_row_map[party.abo_uid].setdefault(key, party)

    result: List[Abo] = []

    for value in uid_row_map.values():
        abo = Abo()
        for party in value.values():
            if party.user_type_code == "E" or party.user_type_code == "P1":
                setattr(abo, "first", party.__dict__)
            elif party.user_type_code == "P2":
                setattr(abo, "second", party.__dict__)
            elif party.user_type_code == "S":
                setattr(abo, "second", party.__dict__)

        result.append(abo)

    return result

