def test_geckodriver_starts_correctly(driver, live_server):
    """Dummy test to ensure Geckodriver works correctly."""
    driver.get(live_server.url)
