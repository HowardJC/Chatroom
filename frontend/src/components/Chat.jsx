import React, {useState} from "react"
import io from "socket.io-client";
let endpoint = "http://localhost:5000";
let socket = io.connect(endpoint);

const Chat = () =>{

    const [messages,setMessages]=useState([]);
    const [message,setMessage]=useState("")

    socket.off("message")

    socket.on("message", msg =>{
        setMessages([...messages,msg])});

    const onChange=(event)=>{
        setMessage(event.target.value)

    }

    const onClick =() =>{
        socket.emit("message",message);
        setMessage("")
    };

    return(
        <div className = "Chat">
            <h2>Messages</h2>
            {messages.map(msg=>(<p>{msg}</p>))}

                <input type="text" onChange={onChange} value={message} />
                <input type="button" onClick={onClick} value="Send"/>
 </div>


    )
}
export default Chat