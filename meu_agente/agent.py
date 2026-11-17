from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_api_tool import CalendarToolset
import os



calendar_toolset = CalendarToolset(
    client_id=os.environ["OAUTH_CLIENT_ID"],
    client_secret=os.environ["OAUTH_CLIENT_SECRET"],
    tool_filter=[
        "calendar_events_list",
        "calendar_events_get",
        "calendar_events_insert",
        "calendar_freebusy_query",
    ],
)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Um agente pessoal do Dyego (eu) que e a unica pessoa que' \
    'conversa com você, e você faz coisas solicitadas por mim. ',
    instruction='Você é um agente pessoal focado em dar as melhores instruções ' \
    'e deixar a minha vida mais facil para mim , como marcar compromissos, organizar agenda,' \
    'dizer noticias e dentre outros.',
    tools=[calendar_toolset]
)
