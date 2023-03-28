from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=10, label='标题', min_length=2, error_messages={
        "min_length": '标题最小为2个字符',
        "max_length": '标题最大为10个字符',
    })
    content = forms.CharField(max_length=100, label='内容', widget=forms.Textarea)
    email = forms.EmailField(label='邮箱', required=True)
    reply = forms.BooleanField(label='是否回复', required=False)
