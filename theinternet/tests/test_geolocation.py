
import pytest

from theinternet.pages.geolocation_page import GeolocationPage

from theinternet.config.config import base_url,resource_url
from theinternet.tests.basetest import BaseTest


@pytest.fixture(scope="function")
def get_url():
    return base_url+str(resource_url.get("geolocation_url"))


class TestGeolocationPage(BaseTest):

    def test_get_geolocation(self,get_url):
        """Scenario: click Where Am I? button"""

        geolocation_page=GeolocationPage(self.driver)

        self.driver.get(get_url)
        geolocation_page.click_whereami()
        assert geolocation_page.assert_coordinates_presence()
        geolocation_page.display_location()

    def test_open_googlemaps(self,get_url):
        """Scenario: click Where Am I? button. Then click on the See it on Google link"""

        geolocation_page = GeolocationPage(self.driver)

        self.driver.get(get_url)
        geolocation_page.click_whereami()
        assert geolocation_page.assert_coordinates_presence()
        geolocation_page.display_location()
        geolocation_page.click_open_maps()
        assert "www.google.com/maps" in geolocation_page.get_url()

