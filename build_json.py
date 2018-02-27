import json

_occupied = True
_posture = 1.0
_confidence = 0.6
_score = 0.3
_x = 0.5
_y = 0.5
_z = -0.5
_ui = "Intervene not necessary"
_r1 = 0.7
_r2 = 0.6
_r3 = 0.3
_r4 = 0.2

data = {}
data["occupied"] = _occupied
data["posture"] = _posture
data["confidence"] = _confidence
data["score"] = _score
data["x"] = _x
data["y"] = _y
data["z"] = _z
data["ui"] = _ui

data["raw"] = [_r1, _r2, _r3, _r4]

with open('data.json','w') as outfile:
    json.dump(data, outfile)

