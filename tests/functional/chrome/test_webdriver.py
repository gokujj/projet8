def test_chromedriver_works_correctly(driver, live_server):
    """Dummy test to verify chromedriver works correctly."""
    driver.get(live_server.url)
