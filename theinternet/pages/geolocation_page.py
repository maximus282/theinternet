from page_objects import PageObject, PageElement


class GeolocationPage(PageObject):
    # locators
    _whereami_btn_loc = "//button"
    _lat_loc = "lat-value"
    _long_loc = "long-value"
    _maplink_loc="#map-link > a"

    # elements
    whereami_btn = PageElement(xpath=_whereami_btn_loc)
    lat_value = PageElement(id_=_lat_loc)
    long_value = PageElement(id_=_long_loc)
    maplink=PageElement(css=_maplink_loc)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("Created GeolocationPage")

    def return_whereami_btn(self):
        return self.whereami_btn

    def click_whereami(self):
        self.whereami_btn.click()

    def return_lat(self):
        return self.lat_value

    def return_long(self):
        return self.long_value

    def return_lat_value(self):
        return self.lat_value.text

    def return_long_value(self):
        return self.long_value.text

    def display_location(self):
        print("Your Latitude {}, your longitude {}".format(self.return_lat_value(), self.return_long_value()))

    def assert_coordinates_presence(self):
        try:
            if self.return_long().is_displayed() is True and self.return_lat().is_displayed() is True:
                return True
        except AttributeError:
            return False

    def click_open_maps(self):
        self.maplink.click()

    def get_url(self):
        return self.driver.current_url

