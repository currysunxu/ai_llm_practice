from datetime import datetime
from typing import Optional, List

from llama_index.core import Settings
from llama_index.core.base.llms.types import ChatMessage
from llama_index.program.openai import OpenAIPydanticProgram
from pydantic import BaseModel, Field

from structured_data_demo.llms import deepseek_llm

llm = deepseek_llm()
Settings.llm = llm

class TestStep(BaseModel):
    step: str
    data: Optional[str] = None
    result: str

class TestCase(BaseModel):
    key: str
    summary: str
    description: Optional[str] = None
    project: str
    status: str = Field(...,description="test status",pattern='^(passed|failed|obsolete)')
    issue_type: str = Field(default="Test")
    labels: List[str] = []
    components: List[str] = []
    priority: Optional[str] = None
    assignee: Optional[str] = None
    reporter: Optional[str] = None
    created: datetime
    updated: datetime
    steps: List[TestStep]

# Example usage
test_case = TestCase(
    key="TEST-123",
    summary="Verify login functionality",
    description="Test case to verify login functionality with valid credentials.",
    project="MyProject",
    status="passed",
    labels=["regression", "login"],
    components=["Authentication"],
    priority="High",
    assignee="john.doe",
    reporter="jane.smith",
    created=datetime.now(),
    updated=datetime.now(),
    steps=[
        TestStep(step="Navigate to login page", result="Login page is displayed"),
        TestStep(step="Enter valid username and password", result="User is logged in"),
        TestStep(step="Verify user dashboard", result="User dashboard is displayed")
    ]
)

# to verify the test case model
# print(test_case.model_dump_json(indent=4))


def streaming_data_extract():

    streaming_llm = llm.as_structured_llm(output_cls=TestCase)

    input_msg = ChatMessage(content="please help me to design 1 test case for searching baidu")
    streaming_output = streaming_llm.stream_chat([input_msg])
    for text in streaming_output:
        print(text)

    # 问题 1: 为什么要一个case，缺返回 一大堆无效测试用例
    # 1019回答了: streaming output 原理 是叠加的方式

# assistant: {"key":null,"summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":null,"summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":null,"summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":null,"summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"","summary":null,"description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"","description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"","description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"","description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"","description":null,"project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}
# assistant: {"key":"TC_001","summary":"Search functionality on Baidu","description":"","project":null,"status":null,"issue_type":null,"labels":null,"components":null,"priority":null,"assignee":null,"reporter":null,"created":null,"updated":null,"steps":null}


# streaming_data_extract()

# pre-condition: pip install llama-index-program-openai,python3.12 instead of 3.11
def openai_pydantic_api_data_extract(prompt_template_str):

    # prompt_template_str = """
    # design two test {name} cases
    # """

    program = OpenAIPydanticProgram.from_defaults(
        output_cls=TestCase,prompt_template_str=prompt_template_str,verbose=True
    )

    output = program(
        name=TestCase, description="Data model for a common test."
    )
    print(output)

openai_pydantic_api_data_extract()