from flet import Container, Column, ResponsiveRow, CircleAvatar, Text, ListTile, Icon, IconButton, TextField, ScrollMode, MainAxisAlignment, CrossAxisAlignment, alignment, FontWeight, padding, colors, icons
from joblib import load

model = load('model/model.joblib')

class Message(Container):
    def __init__(self, text:str, sender:str):
        super().__init__()
        self.width=350
        self.text = text
        self.sender = sender
        self.alignment=alignment.center_left if sender == 'Bot' else alignment.center_right
        self.content=ResponsiveRow(
            width=300,
            columns=6,
            controls=[
                CircleAvatar(
                    content=Text(self.sender[0]),
                    radius=20,
                    col=1
                ),
                Container(
                    bgcolor=colors.GREEN_100,
                    border_radius=10,
                    padding=10,
                    alignment=alignment.center_left,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.START,
                        controls=[
                            Text(self.sender, weight=FontWeight.BOLD),
                            Text(self.text) 
                        ]
                    ),
                    col=5
                )
            ]
        ) if sender == 'Bot' else ResponsiveRow(
            width=300,
            columns=6,
            controls=[
                Container(
                    bgcolor=colors.GREEN_100,
                    border_radius=10,
                    padding=10,
                    alignment=alignment.center_right,
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.END,
                        controls=[
                            Text(self.sender, weight=FontWeight.BOLD),
                            Text(self.text)
                        ]
                    ),
                    col=5
                ),
                CircleAvatar(
                    content=Text(self.sender[0]),
                    radius=20,
                    col=1
                )
            ]
        )
    def build(self):
        return self
            
class ChatBot(Container):
    def __init__(self):
        super().__init__()
        self.data=''
        self.visible=False
        self.bgcolor=colors.GREEN_100
        self.padding=10
        self.width=350
        self.height=400
        self.bottom=20
        self.right=20
        self.border_radius=10
        self.header = self.Header()
        self.messages = self.Message_List()
        self.prompt = self.Prompt()
        self.content=Column(
            controls=[
                self.header,
                self.messages,
                self.prompt
            ]
        )
        
    def show_chatbot(self,e):
        self.visible = not self.visible
        self.update()
    
        
    def Header(self):
        return ListTile(
            leading=Icon(icons.CHAT, size=22.0),
            title=Text('MedicalBot', weight=FontWeight.BOLD, size=20),
            trailing=IconButton(icon=icons.REMOVE_ROUNDED, icon_size=22.0, on_click=self.show_chatbot),
            bgcolor=colors.GREEN_800,
            content_padding=0,
            dense=True
        )
        
    def Prompt(self):
        
        def response(input):
            if input == '': 
                return
            if input == 'Không': 
                message = Message(f'Có thể bạn đang mang bệnh {model.predict([self.data])[0][0]}', 'Bot')
                self.messages.controls.append(message)
            else: 
                self.data = self.data + ',' + input
                message = Message('Được rồi. Còn gì nữa không?', 'Bot')
                self.messages.controls.append(message)
        
        def send(e):
            if prompt.value == '': return
            message = Message(prompt.value, 'You')
            self.messages.controls.append(message)
            response(prompt.value)
            prompt.value = ''
            prompt.focus()
            self.messages.scroll_to(offset=-1, duration=0.5)
            self.update()
        
        prompt = TextField(
            hint_text='Nhập nội dung cần hỗ trợ',
            content_padding=padding.symmetric(horizontal=10, vertical=0),
            on_submit=send,
            col=6
        )
        send_btn = IconButton(icon=icons.SEND_ROUNDED, icon_size=26.0, on_click=send, col=1)
        
        return ResponsiveRow(
            columns=7,
            controls=[
                prompt,
                send_btn
            ]
        )
        
    def Message_List(self):
        return Column(
            expand=True,
            tight=True,
            scroll=ScrollMode.AUTO,
            alignment=MainAxisAlignment.END,
            controls=[
                Message('Xin chào, tôi là chatbot của phòng khám Medical có khả năng dự đoán bệnh thông qua triệu chứng bạn cung cấp, tôi có thể giúp gì cho bạn?', 'Bot')
            ]
        )
