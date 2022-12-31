from models.Ap import Ap
from models.Gr import Gr
from models.GrProduction import GrProduction
# init lists
automatas = []
grs = []
aps = []

# add gr to list
grs.append(Gr("GR 1", ["S", "A", "B", "C"], ["a", "b", "z"], "S", [], [
    GrProduction("S", ["A"]),
    GrProduction("A", ["a", "A", "a"]),
    GrProduction("A", ["B"]),
    GrProduction("B", ["b", "B", "b"]),
    GrProduction("B", ["C"]),
    GrProduction("C", ["z", "C"]),
    GrProduction("C", ["z"]),
]))
aps.append(Ap("AP 1", ["a", "b"], ["a", "b", "#"], ["I", "A", "B", "C", "F"], "I", "F", [
    ["I", "$", "$", "A", "#"],
    ["A", "a", "$", "B", "a"],
    ["B", "a", "$", "B", "a"],
    ["B", "b", "a", "C", "$"],
    ["C", "b", "a", "C", "$"],
    ["C", "$", "#", "F", "$"]
]))

print(aps[0].validateString('ab'))