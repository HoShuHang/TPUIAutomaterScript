from screens.BaseScreen import BaseScreen
import Value

class MainScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        print("Main screen init")
        self.add = self.dMobile()(className="android.widget.LinearLayout").child(className="android.widget.ImageView")
        self.text_note = self.dMobile()(text="Text Note")
        self.format = self.dMobile()(resourceId="com.evernote:id/format_btn")

    def add_note(self):
        self.click_btn(self.add)
        self.click_btn(self.text_note)
