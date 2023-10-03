import answerCall as screener
caller_codes = "U","T","R","F"
sameAreaCode = True,False
cur_time = "9:00","14:00","23:50","10:40","23:00","10:00","13:00","9:00","16:00"
if():
    cur_time <= "7:00", False
    cur_time >= "10:00", False

def test_answerCallForUnknownSameAreaCodeGoodTime(self):
    result = screener.answerCall("U", True, "09:00")
    expected = True
    assert result == expected


def test_answerCallForUnknownDifferentAreaCodeGoodTime(self):
    result = screener.answerCall("U", False, "14:00")
    expected = False
    assert result == expected


def test_answerCallForUnknownSameAreaCodeBadTime(self):
    result = screener.answerCall("U", True, "23:50")
    expected = False
    assert result == expected


def test_answerCallForTelemarketerSameAreaCodeGoodTime(self):
    result = screener.answerCall("T", True, "10:40")
    expected = False
    assert result == expected


def test_answerCallForTelemarketerDifferentAreaCodeBadTime(self):
    result = screener.answerCall("T", False, "23:00")
    expected = False
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeGoodTime(self):
    result = screener.answerCall("F", False, "10:00")
    expected = True
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeBadTime(self):
    result = screener.answerCall("F", False, "23:00")
    expected = False
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeGoodTime_2(self):
    result = screener.answerCall("F", False, "13:00")
    expected = True
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeGoodTime(self):
    result = screener.answerCall("R", False, "9:00")
    expected = True
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeBadTime(self):
    result = screener.answerCall("R", False, "04:00")
    expected = False
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeGoodTime_2(self):
    result = screener.answerCall("R", False, "16:00")
    expected = True
    assert result == expected
