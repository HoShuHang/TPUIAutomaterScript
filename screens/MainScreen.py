from screens.BaseScreen import BaseScreen
import Value

class MainScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        print("Main screen init")

    def add_note(self):
        Value.dMobile(className="android.widget.LinearLayout").child(className="android.widget.ImageView").click.wait()