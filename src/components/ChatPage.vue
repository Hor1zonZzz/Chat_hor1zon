<template>
  <div class="chat-container">  
    <!-- <h1>Chat Window</h1> -->
    <div class="chat-window">
      <div class="message-container">
        <!-- 循环渲染消息 -->
        <!-- 用户消息和AI消息，按发送顺序循环渲染 -->
        <div v-for="(message, index) in messages" :key="index" :class="message.sender === 'User' ? 'sent' : 'received'">
          {{ message.text }}
          <div class="message-timestamp">{{ message.timestamp }}</div>
        </div>
      </div>
      <div class="input-container">
        <input type="text" v-model="messageInput" placeholder="Type your message here..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

.chat-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%; /* 修改为100vh以填充整个页面 */
}

.chat-window {
  width: 65%;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.message-container {
  padding: 10px;
  max-height: 300px;
  overflow-y: auto;
}

.message {
  margin-bottom: 10px;
  padding: 8px 12px;
  border-radius: 8px;
  max-width: 70%;
}

.received {
  background-color: #f0f0f0;
  align-self: flex-start;
}

.sent {
  background-color: #007bff;
  color: #fff;
  align-self: flex-end;
}

.input-container {
  display: flex;
  align-items: center;
  padding: 10px;
}

.input-container input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

.input-container button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}
</style>


<script>
import axios from 'axios';
export default {
  name: 'ChatPage',
  data() {
    return {
      messageInput: '',
      userMessages: [], // 存储用户发送的消息
      aiMessages: [], // 存储AI回复的消息
      messages: [] // 用户和AI的消息
    };
  },
  methods: {
    sendMessage() {
  const userMessage = this.messageInput.trim();
  if (!userMessage) return;

  // 将用户消息添加到 messages 数组中
  this.messages.push({
    text: userMessage,
    sender: 'User',
    timestamp: new Date().toLocaleString()
  });

  // 清空输入框
  this.messageInput = '';

  // 发送消息到后端
  axios.post('http://8.130.111.178:5000/chat', { userMessage })
    .then(response => {
      // 从响应中提取 AI 的回复
      const aiResponse = response.data;
      console.log(aiResponse);
      // 将 AI 响应添加到 messages 数组中
      this.messages.push({
        text: aiResponse.ai_message,
        sender: 'AI',
        timestamp: new Date().toLocaleString()
      });
    })
    .catch(error => {
      console.error('Error sending message:', error);
    });
}
  }
}
</script>