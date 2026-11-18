import pytest
from physics import destruction_fracture as mod

CASES = [
    ("cells_wood", "m.fracture_cells('wood', 2) == 4"),
    ("cells_stone", "m.fracture_cells('stone', 2) == 2"),
    ("mass_double", "m.fragment_mass(2.0, 3.0) == approx(6.0)"),
    ("mass_zero", "m.fragment_mass(0.0, 3.0) == approx(0.0)"),
    ("impulse_half", "m.impulse_transfer(6.0, 2.0) == approx(3.0)"),
    ("support_nodes", "m.rebuild_support({'a': ['b'], 'b': []}) == ['a', 'b']"),
    ("filter_other", "m.collision_filter('a', 'b') is True"),
    ("filter_same", "m.collision_filter('a', 'a') is False"),
    ("sleep_true", "m.sleep_threshold(0.1, 0.5) is True"),
    ("sleep_false", "m.sleep_threshold(1.0, 0.5) is False"),
    ("unique_true", "m.unique_face('n1', ['n2']) is True"),
    ("unique_false", "m.unique_face('n1', ['n1']) is False"),
    ("queue_len", "len(m.async_queue(['a', 'b'])) == 2"),
    ("seed_same", "m.deterministic_seed(7, 2) == m.deterministic_seed(7, 2)"),
    ("seed_diff", "m.deterministic_seed(7, 2) != m.deterministic_seed(7, 3)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
