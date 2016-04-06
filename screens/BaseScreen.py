import Value


class BaseScreen:
    def __init__(self):
        print("base screen init")

    def dMobile(self):
        return Value.dMobile

    def click_btn(self, btn):
        btn.click.wait()