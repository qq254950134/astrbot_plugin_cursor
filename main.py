from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests
import json

API_URL = "http://your-ip/v1/chat/completions"
headers = {
    "Content-Type": "application/json", 
    "Authorization": "Bearer your-password"
}

AVAILABLE_MODELS = [
    "claude-3.5-sonnet", "gpt-4", "gpt-4o", "claude-3-opus",
    "cursor-fast", "cursor-small", "gpt-3.5-turbo",
    "gpt-4-turbo-2024-04-09", "gpt-4o-128k", "gemini-1.5-flash-500k",
    "claude-3-haiku-200k", "claude-3-5-sonnet-200k",
    "claude-3-5-sonnet-20241022", "gpt-4o-mini", "o1-mini",
    "o1-preview", "o1", "claude-3.5-haiku", "gemini-exp-1206",
    "gemini-2.0-flash-thinking-exp", "gemini-2.0-flash-exp",
    "deepseek-v3", "deepseek-r1"
]

@register("claude", "Your Name", "Claude AI 对话插件", "1.0.0", "https://github.com/qq254950134/astrbot_plugin_cursor")
class ClaudePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.current_model = "claude-3.5-sonnet"  # 默认模型
        
    async def chat_with_model(self, message: str, model=None):
        """调用 API"""
        if model is None:
            model = self.current_model
            
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
            logger.error(f"调用 API 出错: {str(e)}")
            return f"发生错误: {str(e)}"

    @filter.command_group("model")
    def model_group(self):
        """模型管理指令组"""
        pass

    @model_group.command("list")
    async def list_models(self, event: AstrMessageEvent):
        """列出所有可用的模型
        
        用法: /model list
        """
        models_text = "\n".join([f"- {model}" for model in AVAILABLE_MODELS])
        current_model = f"当前使用的模型: {self.current_model}\n\n可用的模型列表:\n{models_text}"
        yield event.plain_result(current_model)

    @model_group.command("switch")
    async def switch_model(self, event: AstrMessageEvent, model_name: str):
        """切换使用的模型
        
        用法: /model switch <模型名称>
        """
        if model_name not in AVAILABLE_MODELS:
            yield event.plain_result(f"错误：未知的模型 {model_name}\n请使用 /model list 查看可用的模型")
            return
            
        self.current_model = model_name
        yield event.plain_result(f"已切换到模型: {model_name}")

    @filter.command("ask")
    async def ask(self, event: AstrMessageEvent):
        """向 AI 提问
        
        用法: /ask <问题>
        """
        user_name = event.get_sender_name()
        question = event.message_str
        message_chain = event.get_messages()
        logger.info(f"用户 {user_name} 发送问题: {question}")
        logger.info(f"消息链: {message_chain}")
        
        response = await self.chat_with_model(question)
        yield event.plain_result(response)

    @filter.command("chat")
    async def chat(self, event: AstrMessageEvent):
        """与 AI 对话
        
        用法: /chat <内容>
        """
        if event.is_at_me():
            user_name = event.get_sender_name()
            question = event.message_str.strip()
            message_chain = event.get_messages()
            logger.info(f"用户 {user_name} 发送对话: {question}")
            logger.info(f"消息链: {message_chain}")
            
            response = await self.chat_with_model(question)
            yield event.plain_result(response) 
