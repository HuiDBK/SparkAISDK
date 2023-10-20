# SparkAISDK
> 星火AI-SDK，通过webscokets or aiohttp 封装对接星火api
> 
> 通过 pydantic 组织数据形式，重新组织消息格式

# 安装依赖
```python
pip install -r requirements.txt
```

# 快速开始
```python
import asyncio
import random

from spark_ai_sdk.client import SparkClient
from spark_ai_sdk.config import SparkMsgRole, SparkChatConfig, SparkMsgInfo


def build_user_msg_context_list(content):
    msg_context_list = [
        {"role": SparkMsgRole.USER.value, "content": content},  # 用户的历史问题
        # {"role": SparkMsgRole.ASSISTANT.value, "content": "....."},  # AI的历史回答结果
        # ....... 省略的历史对话
        # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
    ]
    return msg_context_list


async def main():
    chat_conf = SparkChatConfig(domain="generalv2", temperature=0.5, max_tokens=2048, top_k=3)
    spark_client = SparkClient(
        # 填写你的讯飞应用密钥信息
        app_id="",
        api_secret="",
        api_key="",
        chat_conf=chat_conf
    )

    questions = ["程序员如何技术提升？", "如何提升系统并发", "如何找女朋友"]
    ques = random.choice(questions)
    msg_context_list = build_user_msg_context_list(content=ques)
    answer_full_content = ""

    async for chat_resp in spark_client.achat(msg_context_list):
        chat_resp: SparkMsgInfo = chat_resp
        answer_full_content += chat_resp.msg_content
        print(chat_resp)
    print(answer_full_content)


if __name__ == '__main__':
    asyncio.run(main())

```