import { useState } from 'react';
import axios from 'axios';
import styles from '../styles/Chat.module.css';

export default function Chat() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const [isLoading, setIsLoading] = useState(false); // Add this line

  const sendMessage = async (e) => {
    e.preventDefault();
    setIsLoading(true); // Add this line
    const response = await axios.post('http://localhost:5000/chat', {
      user_message: message,
    });
    setChat([...chat, { user: 'You', text: message }, { user: 'Bot', text: response.data.bot_response }]);
    setMessage('');
    setIsLoading(false); // Add this line
  };

  return (
    <div className={styles.pageContainer}>
      <h1 className={styles.title}>DevExGPT Chat</h1>
      <div className={styles.chat}>
        {chat.map((message, index) => (
          <div key={index} className={`${styles.message} ${message.user === 'You' ? styles.userMessage : styles.botMessage}`}>
            <strong>{message.user}:</strong> {message.text}
          </div>
        ))}
        {isLoading && <div>Loading...</div>}
        <div className={styles.inputContainer}>
          <form onSubmit={sendMessage} className={styles.form}>
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              className={styles.input}
              placeholder="Start chatting here..."
            />
            <button className={styles.button} type="submit">Send</button>
          </form>
        </div>
      </div>
    </div>
  );
}
