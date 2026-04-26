import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([{text: "Chào anh, tôi là AI kỹ sư Vinasumo. Hãy gửi kích thước xưởng hoặc ảnh bản vẽ để tôi tư vấn giải pháp tối ưu nhất.", sender: "ai"}]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if(!input) return;
    const newMsgs = [...messages, {text: input, sender: "user"}];
    setMessages(newMsgs);
    setInput("");
    
    try {
        const res = await fetch('http://localhost:8000/ai-consultant', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: input})
        });
        const data = await res.json();
        setMessages([...newMsgs, {text: data.reply, sender: "ai"}]);
    } catch (e) {
        setMessages([...newMsgs, {text: "Hệ thống đang kết nối AI... Vui lòng gọi 0829483868 để tư vấn gấp.", sender: "ai"}]);
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>VINASUMO - AI INDUSTRIAL SOLUTIONS</h1>
        <div className="contact-bar">Zalo/Hotline: 0829483868</div>
      </header>
      
      <div className="product-banner">
        <h3>QUẠT HÚT VUÔNG | COMPOSITE | LY TÂM | MÁY LÀM MÁT</h3>
      </div>

      <div className="chat-container">
        <div className="messages-list">
          {messages.map((m, i) => (
            <div key={i} className={`message-bubble ${m.sender}`}>
              {m.text}
            </div>
          ))}
        </div>
        <div className="input-group">
          <input 
            value={input} 
            onChange={(e)=>setInput(e.target.value)} 
            placeholder="Ví dụ: Tính quạt cho phòng sơn 7x4x2.6m..." 
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          />
          <button onClick={handleSend}>TƯ VẤN AI</button>
        </div>
      </div>
    </div>
  );
}
export default App;
