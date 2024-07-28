<!-- 用于开发 -->

<template>
    <div class="chat-window">
        <div class="chat-messages" ref="chatMessages">
            <!-- <div v-for="message in messages" :key="message.id" class="chat-message">
                {{ message.text }} -->
            <div v-for="(message, index) in messages" :key="index" :class="message.role === 'User' ? 'sent' : 'received'">
                {{ message.text }}
                <!-- <div class="message-timestamp">{{ message.timestamp }}</div> -->
            </div>
        </div>
        <div class="chat-input">
            <input v-model="messageInput" @keydown.enter="sendMessage" placeholder="Type your message..." />
            <el-button type="primary" size="default" @click="sendMessage">Send</el-button>
            <el-button type="danger" size="default" @click="clearMessages">NewChat</el-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ChatWindow',
  data() {
    return {
        messageInput: '',
        userMessages: [], // 存储用户发送的消息
        aiMessages: [], // 存储AI回复的消息
        messages: [] // 用户和AI的消息
    };
  },
  methods: {
    clearMessages() {
        const Clear = 1;
        this.messages = [];
        axios.post('http://127.0.0.1:5000/chat', { Clear })
    },
    sendMessage() {
        const userMessage = this.messageInput.trim(); // 获取用户输入的消息并去掉首尾空格。
        const Clear = 0;
        if (!userMessage) return; // 注意userMessage和userMessages区别

        // 将用户消息添加到 messages 数组中
        this.messages.push({
            text: userMessage,
            role: 'User',
            timestamp: new Date().toLocaleString()
        });

        // 清空输入框
        this.messageInput = '';

        // 发送消息到后端
        axios.post('http://127.0.0.1:5000/chat', { Clear, userMessage })
        .then(response => {
            // 从响应中提取 AI 的回复
            const aiResponse = response.data;
            console.log(response);
            console.log(aiResponse);
            // 将 AI 响应添加到 messages 数组中
            this.messages.push({
                text: aiResponse.ai_message,
                role: 'AI',
                timestamp: new Date().toLocaleString()
            });
            console.log("打印出messages：",this.messages);
        })
        .catch(error => {
            console.error('Error sending message:', error);
        });
    
},
    scrollToBottom() {
      this.$nextTick(() => {
        const chatMessages = this.$refs.chatMessages;
        chatMessages.scrollTop = chatMessages.scrollHeight;
      });
    }

  },
  updated() {
    this.scrollToBottom();
  }
}
</script>

<style scoped>
.chat-window {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    height: 60vh;
    width: 50%;
    border: 3px solid #798f94;
    border-radius: 25px;
    overflow: hidden;
}

.chat-messages {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto;
}

.chat-message {
    margin-bottom: 10px;
}

.chat-input {
    display: flex;
    align-items: center;
    padding: 10px;
    background-color: #f0f0f0;
}

.chat-input input {
    flex: 1;
    padding: 5px;
    border: 1px solid #75d3ff;
    border-radius: 4px;
    margin-right: 10px;
}

.chat-input button {
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.sent {
    text-align: right;
    color: #007bff
}

.received {
    text-align: left;
    color: #28a745
}

.message-timestamp {
    font-size: 0.8em;
    color: #6c757d;
}
</style>
