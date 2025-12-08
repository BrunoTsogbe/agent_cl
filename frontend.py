import streamlit
from conversation_agent import ConversationAgent 

if "conversation_agent" not in streamlit.session_state :
	streamlit.session_state.conversation_agent = ConversationAgent()

def show_discussion_history():
	for message in streamlit.session_state.conversation_agent.history:
		if message["role"] != "system":
			with streamlit.chat_message(message["role"]):
				streamlit.write(message["content"])











# initialisation de la page
streamlit.set_page_config(page_title="Jarvis", page_icon="🤖")
streamlit.title("🤖 Jarvis votre baron préféré !")
streamlit.write("N'oublie pas à qui tu parles...")


# Zone de saisie utilisateur
user_input = streamlit.chat_input("Jarvis est un peu enervé, fais attention à ce que tu racontes !")
if user_input:
	streamlit.session_state.conversation_agent.ask_llm(user_interaction=user_input)
	show_discussion_history()