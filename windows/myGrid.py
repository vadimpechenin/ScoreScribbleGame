from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows = 1
        self.spacing = 10
        self.size_hint = (None, 1)
        self.bind(minimum_width=self.setter('width'))