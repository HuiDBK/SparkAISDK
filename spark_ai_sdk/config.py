#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 配置模块 }
# @Date: 2023/10/20 19:43
import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SparkChatConfig(BaseModel):
    """星火聊天配置"""
    domain: str = Field(default="generalv2", description="api版本")
    temperature: float = Field(
        default=0.5,
        ge=0, le=1,
        description="取值为[0,1],默认为0.5, 核采样阈值。用于决定结果随机性，取值越高随机性越强即相同的问题得到的不同答案的可能性越高"
    )
    max_tokens: int = Field(default=2048, le=8192, ge=1, description="模型回答的tokens的最大长度")
    top_k: int = Field(default=4, le=6, ge=1, description="从k个候选中随机选择⼀个（⾮等概率）")


class SparkMsgRole(Enum):
    """星火消息角色"""

    USER = "user"
    ASSISTANT = "assistant"


class SparkMessageStatus(Enum):
    """
    星火消息响应状态
    0-代表首个文本结果；1-代表中间文本结果；2-代表最后一个文本结果
    """

    FIRST_RET = 0
    MID_RET = 1
    END_RET = 2


class SparkChatUsageInfo(BaseModel):
    """星火聊天使用信息"""
    question_tokens: int = Field(default=0, description="问题token数量")
    prompt_tokens: int = Field(default=0, description="提示token数量")
    completion_tokens: int = Field(default=0, description="完成token数量")
    total_tokens: int = Field(default=0, description="总token数量")


class SparkMsgInfo(BaseModel):
    """星火消息信息"""

    msg_sid: str = Field(default=uuid.uuid4().hex, description="消息id，用于唯一标识⼀条消息")
    msg_type: str = Field(default="text", description="消息类型，目前仅支持text")
    msg_content: str = Field(default="", description="消息内容")
    answer_full_content: Optional[str] = Field(default="", description="最后完整的消息内容")
    msg_status: SparkMessageStatus = Field(default=SparkMessageStatus.FIRST_RET, description="消息状态")

    usage_info: Optional[SparkChatUsageInfo] = Field(default=None, description="消息使用信息")
