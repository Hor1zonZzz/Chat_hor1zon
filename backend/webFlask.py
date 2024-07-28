from flask import Flask, request, jsonify
from flask_cors import CORS
# 创建Flask应用实例
app = Flask(__name__)


# 导入模型所需包
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms.ollama import Ollama
# 导入模板所需包
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
# 导入对话链所需包
from langchain.chains.conversation.base import ConversationChain
# 导入对话链历史记录所需包
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ChatMessageHistory
# 导入对话链历史记录存储所需包
from langchain.schema import messages_to_dict, messages_from_dict
import pickle


# 设置API_KEY和API_ENDPOINT
API_KEY = "AIzaSyDrHTlwVI_26vQ0D2pFMxWWN31lrGbCLc4"
API_ENDPOINT = "https://gemini.hor1zon.org"

# 创建ChatGoogleGenerativeAI
Gemini_chat_model = ChatGoogleGenerativeAI(google_api_key=API_KEY, model="gemini-1.5-pro-latest", transport='rest', client_options={"api_endpoint": API_ENDPOINT})

# 创建ollama
# ollama_chat_model = Ollama(model = "qwen:4b")

# 设置对话缓存的方式
Buffer = ConversationBufferMemory()

# 初始化对话链
def init_conversation(chat_model, memory):

    conversation = ConversationChain(
        memory=memory,
        llm = chat_model,
        verbose=True # verbose参数用于控制是否以详细模式运行对话链
    )

    print("对话创建完成")
    return conversation

# 允许跨域访问
CORS(app, resources={r'/chat': {'origins': '*'}})

@app.route('/chat', methods=['POST'])
def receive_data():

    data = request.get_json()  # 获取前端发送的JSON数据
    # 在这里处理数据，执行后端逻辑
    # print("获得数据：", data['userMessage'])

    if data['Clear'] == 1:
        Buffer.clear()
        print("清空对话链")
        return jsonify({"sys_message": "对话链已清空"})
    else:
        # 初始化对话链
        Conversation = init_conversation(Gemini_chat_model, Buffer)
        # 通过Conversation进行对话
        response = Conversation.invoke(data['userMessage'])
        print("返回数据：", response["response"])
        AIResponse = response["response"]
        # 返回数据
        response_data = {
            "ai_message": AIResponse,
            'type': 'AIMessage'
        }
        return jsonify(response_data)

if __name__ == '__main__':
    app.run()
