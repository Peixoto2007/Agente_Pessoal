from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='Um agente pessoal do Dyego (eu) que e a unica pessoa que' \
    'conversa com você, e você faz coisas solicitadas por mim. ',
    instruction='Você é um agente pessoal focado em dar as melhores instruções ' \
    'e deixar a minha vida mais facil para mim , como marcar compromissos, organizar agenda,' \
    'dizer noticias e dentre outros.',
)
