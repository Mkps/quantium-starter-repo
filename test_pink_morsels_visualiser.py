from pink_morsels_visualiser import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=15)

def test_visualiser_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualiser", timeout=15)

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-selector", timeout=15)

def test_callback_updates_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualiser", timeout=15)
    inputs = dash_duo.find_elements("#region-selector input")
    inputs[1].click()
    expected_title = f"Sales of Pink Morsels over time - region: north"
    dash_duo.wait_for_contains_text("#visualiser .gtitle", expected_title, timeout=30)
    title = dash_duo.find_element("#visualiser .gtitle").text
    assert "region: north" in title

