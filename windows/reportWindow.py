import time
from threading import Thread

from kivymd.uix.screen import MDScreen
import appEnvironment as AE
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from windows.myGrid import MyGrid
from kivy.uix.label import Label


class ReportWindow(MDScreen):

    def __init__(self, *args, **kwargs):
        super(ReportWindow, self).__init__(*args, **kwargs)
        self.ids.text_label.text = AE.title_of_windows[4]
        self.ids.text_label.font_size = 30 * AE.koef
        self.ifTriggerReport = 0
        Thread(target=self.threadWindowDrawMainReport).start()
        AE.ReportWObj = self

    def threadWindowDrawMainReport(self):
        while True:
            time.sleep(0.3)
            if (self.ifTriggerReport == 1):
                self.windowDrawMainReport()
                self.ifTriggerReport = 0

    def windowDrawMainReport(self):
        self.ids.ScrollWindowReportGlobalid.bind(minimum_height=self.ids.ScrollWindowReportGlobalid.setter('height'))
        scroll2 = ScrollView(size_hint=(1, 0.8), do_scroll_x=False, do_scroll_y=True)
        base2 = BoxLayout(orientation="vertical", size_hint_y=None)
        base2.bind(minimum_height=base2.setter('height'), minimum_width=base2.setter('width'))
        leftGrid1 = GridLayout(cols=1, spacing=10,
                               size_hint_y=None)  # , size_hint_y=10, size_hint_x=10)len(AE.reportWindowmessageResponce.report_list[0])
        # Убедимся, что высота такая, чтобы было что прокручивать.
        leftGrid1.bind(minimum_height=leftGrid1.setter('height'))  #
        self.toggle = []
        for i in range(len(AE.reportWindowmessageResponce.report_list)):
            nasted = []
            self.toggle.append(nasted)
            for j in range(len(AE.reportWindowmessageResponce.report_list[0])):
                nasted.append('')
        base1 = BoxLayout(orientation="vertical", size_hint=(1, None))
        scroll = ScrollView(size_hint=(1, 1), do_scroll_x=True, do_scroll_y=False)
        grid = MyGrid()
        for index in range(len(AE.reportWindowmessageResponce.report_list[0])):
            if (index == 0):
                width = 50 * AE.koef
            else:
                width = 150 * AE.koef

            self.toggle[0][index] = Label(
                size_hint_y=None,
                size_hint_x=None,
                height=40 * AE.koef,
                width=width,
                # text_size=self.size,
                # halign="left",
                # valign="middle",
                # ,
                padding=(10 * AE.koef, 10 * AE.koef),
                text=str(AE.reportWindowmessageResponce.report_list[0][index]),
                color='black'  # [0, 0, 1, 1]
            )
            grid.add_widget(self.toggle[0][index])
        scroll.add_widget(grid)
        base1.add_widget(scroll)
        leftGrid1.add_widget(base1)

        for index in range(1, len(AE.reportWindowmessageResponce.report_list)):
            base1 = BoxLayout(orientation="vertical", size_hint=(1, None))
            scroll = ScrollView(size_hint=(1, 1), do_scroll_x=True, do_scroll_y=False)
            grid = MyGrid()
            for index1 in range(len(AE.reportWindowmessageResponce.report_list[0])):
                if (index1 == 0):
                    width = 50 * AE.koef
                else:
                    width = 150 * AE.koef
                if (index1 < 5):
                    text_str = str(AE.reportWindowmessageResponce.report_list[index][index1])
                else:
                    text_str = str(round(AE.reportWindowmessageResponce.report_list[index][index1], 2))
                self.toggle[index][index1] = Label(
                    size_hint_y=None,
                    size_hint_x=None,
                    height=40 * AE.koef,
                    width=width,
                    # text_size=self.size,
                    # halign="left",
                    # valign="middle",
                    # text_size=(self.width, None),
                    padding=(10 * AE.koef, 10 * AE.koef),
                    text=text_str,
                    color='black'  # [0, 0, 1, 1]
                    # text_size=(self.width, None)
                )
                grid.add_widget(self.toggle[index][index1])
            scroll.add_widget(grid)
            base1.add_widget(scroll)
            leftGrid1.add_widget(base1)

        scroll2.add_widget(leftGrid1)

        self.ids.ScrollWindowReportGlobalid.add_widget(scroll2)

    def dellwidget(self):
        # удаляет все виджеты, которые находяться в another_box
        for i in range(len(self.ids.ScrollWindowReportGlobalid.children)):
            self.ids.ScrollWindowReportGlobalid.remove_widget(self.ids.ScrollWindowReportGlobalid.children[-1])
        self.ifTriggerReport = 0