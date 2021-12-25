from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine

import time

class Container(BoxLayout):
    pass
    # def on_star_click(self):
    #     self.qq.right_action_items = [['star', lambda x: print('qq')]]
        # self.qq.title = 'qq'
        # time.sleep(2)
        # self.qq.right_action_items = [['star-outline']]

class Tab(MDFloatLayout, MDTabsBase):
    pass

class Content(MDBoxLayout):
    '''Custom content.'''
    qq = """
============
Part title..
============
hshhdhd

.. code-block:: ruby
   

    def on_star_click(self):
        #Container().qq.right_action_items = [['menu']]
        #Container().qq.title = 'qq'
        print('qq')

"""

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class PythonGuideApp(MDApp):
    title = 'Python Guide'
    by_who = 'author ara'

    def build(self):
        return Container()

    def qq(self):
        print('qq')

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        tabs_names = [
                'string',
                'list',
                'dict',
                'set',
                'files'
        ]
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        for tab_name in tabs_names:
            #self.root.ids.tabs.add_widget(Tab(title=tab_name))
            for i in range(5):
                #self.root.ids[tab_name].add_widget(
                    #OneLineListItem(
                        #text=f"Single-line item {i} {tab_name}",
                        #on_press=lambda x: self.root.ids.tabs.add_widget(MDLabel(title=tab_name)))
                self.root.ids[tab_name].add_widget(MDExpansionPanel(
                    content=Content(),
                    panel_cls=MDExpansionPanelOneLine(
                        text="[size=20][color=ff3333]str[color=3333ff].capitalize()[/color][/color][/size]",
                    )
                )
            )



    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print(self.root.ids)

    def on_star_click(self):
        #Container().qq.right_action_items = [['menu']]
        #Container().qq.title = 'qq'
        print('qq')

if __name__ == '__main__':
    PythonGuideApp().run()

q = 'str.capitalize()\nВозвращает копию строки, переводя первую буквы в верхний регистр, а остальные в нижний.\n\n\t"нАЧАТЬ С ЗАГЛАВНОЙ ".capitalize()  # Начать с заглавной'