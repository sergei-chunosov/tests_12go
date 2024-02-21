import pytest
from selene import browser
from utils import attach
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


DEFAULT_BROWSER_VERSION = '100.0'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    # browser_version = request.config.getoption('--browser_version')
    # browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": browser_version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )
    # browser.config.driver = webdriver

    browser.config.base_url = "https://12go.asia/"
    browser.config.window_width = '1200'
    browser.config.window_height = '720'
    browser.config.timeout = 4
    # cookies = get_cookie()
    # browser.driver.add_cookie({'name': 'tuid', 'value': cookies})

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()