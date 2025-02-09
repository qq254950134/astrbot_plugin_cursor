from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult, EventMessageType
from astrbot.api.star import Context, Star, register
import requests
import json

API_URL = "http://117.72.95.35/v1/chat/completions"
headers = {
    "Content-Type": "application/json", 
    "Authorization": "Bearer MJJ"
}

@register("claude", "Your Name", "Claude AI 对话插件", "1.0.0", "你的插件仓库URL")
class ClaudePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        
    async def chat_with_model(self, message: str, model="claude-3.5-sonnet"):
        """调用 Claude API"""
        messages = [
            {"role": "user", "content": message}
        ]
        
        data = {
            "model": model,
            "messages": messages,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=data)
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            return "抱歉,我没有得到有效的回复"
        except Exception as e:
            return f"发生错误: {str(e)}"

    @filter.command("ask")
    async def ask(self, event: AstrMessageEvent):
        """向 Claude 提问
        
        用法: /ask <问题>
        """
        question = event.message_str
        response = await self.chat_with_model(question)
        yield event.plain_result(response)
        
    @filter.event_message_type(EventMessageType.ALL)  
    async def on_message(self, event: AstrMessageEvent):
        """处理所有消息"""
        if event.is_at_me():
            question = event.message_str.strip()
            response = await self.chat_with_model(question)
            yield event.plain_result(response) 
