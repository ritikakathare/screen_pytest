from screen_time import analyze_screen_time
def test_healthy_lower_boundary():
    total, category, _ = analyze_screen_time([0.5, 0.5, 1])
    assert category == "Healthy Usage"

def test_healthy_middle_value():
    total, category, _ = analyze_screen_time([1, 1, 1])
    assert category == "Healthy Usage"

def test_healthy_upper_boundary():
    total, category, _ = analyze_screen_time([1, 1, 1])
    assert total == 3
    assert category == "Healthy Usage"
def test_moderate_lower_boundary():
    total, category, _ = analyze_screen_time([2, 1.5])
    assert category == "Moderate Usage"
def test_moderate_middle_value():
    total, category, _ = analyze_screen_time([2, 2, 1])
    assert category == "Moderate Usage"
def test_moderate_upper_boundary():
    total, category, _ = analyze_screen_time([3, 3])
    assert total == 6
    assert category == "Moderate Usage"
def test_excessive_lower_boundary():
    total, category, _ = analyze_screen_time([4, 3])
    assert category == "Excessive Usage"
def test_excessive_middle_value():
    total, category, _ = analyze_screen_time([3, 3, 2])
    assert category == "Excessive Usage"
def test_excessive_high_value():
    total, category, _ = analyze_screen_time([5, 4, 3])
    assert category == "Excessive Usage"
