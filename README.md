# AstrBot cursor AI 插件

一个支持多种 AI 模型的 AstrBot 对话插件，支持 Claude、GPT-4、Gemini 等多种模型。

## 功能特点

- 支持多种 AI 模型，包括：
  - Claude 系列 (claude-3.5-sonnet, claude-3-opus 等)
  - GPT 系列 (gpt-4, gpt-3.5-turbo 等)
  - Gemini 系列
  - 其他模型
- 支持实时切换模型
- 支持多种交互方式
  - 命令模式：`/ask <问题>`
  - 对话模式：`/chat <内容>` (需要 @ 机器人)

## 安装方法

1. 克隆仓库：git clone https://github.com/qq254950134/astrbot_plugin_cursor.git

2. 修改配置：
打开 `main.py`，修改以下配置：
API_URL = "http://your-api-url/v1/chat/completions" # 此处修改your-api-url 为你部署好的cursorapi地址
"Authorization": "Bearer YOUR_TOKEN" # 替换为您的 token令牌
3. 安装插件后自动重启 AstrBot 即可使用

## 使用方法

### 基础对话
- 直接提问：
  ```
  /ask 你好，请介绍一下你自己
  ```
- 对话模式：
  ```
  /chat 你好 (@机器人)
  ```

### 模型管理
- 查看可用模型：
  ```
  /model list
  ```
- 切换模型：
  ```
  /model switch claude-3.5-sonnet
  ```

### 支持的模型列表
- Claude 系列
  - claude-3.5-sonnet
  - claude-3-opus
  - claude-3-haiku-200k
  - claude-3-5-sonnet-200k
  - claude-3-5-sonnet-20241022
  - claude-3.5-haiku
- GPT 系列
  - gpt-4
  - gpt-4o
  - gpt-3.5-turbo
  - gpt-4-turbo-2024-04-09
  - gpt-4o-128k
  - gpt-4o-mini
- Gemini 系列
  - gemini-1.5-flash-500k
  - gemini-exp-1206
  - gemini-2.0-flash-thinking-exp
  - gemini-2.0-flash-exp
- 其他模型
  - cursor-fast
  - cursor-small
  - o1-mini
  - o1-preview
  - o1
  - deepseek-v3
  - deepseek-r1

## 配置说明

1. API 配置
- `API_URL`: 您的 API 服务器地址
- `headers`: API 认证信息，包括 token

2. 模型配置
- 插件默认使用 claude-3.5-sonnet 模型
- 可以通过 `/model switch` 命令随时切换到其他模型

## 常见问题

1. Q: 如何查看当前使用的模型？
   A: 使用 `/model list` 命令可以查看当前使用的模型和所有可用的模型列表。

2. Q: 为什么有时候会返回错误？
   A: 可能是网络问题或 API 调用限制，请检查：
   - API 地址是否正确
   - Token 是否有效
   - 网络连接是否正常

## 更新日志

### v1.0.0
- 初始版本发布
- 支持基础对话功能
- 支持多种 AI 模型
- 支持模型切换功能

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 作者

MJJ

## 链接

- [GitHub 仓库](https://github.com/qq254950134/astrbot_plugin_cursor)
- [AstrBot 官网](https://astrbot.app/)
- [cursor-api](https://github.com/wisdgod/cursor-api)
