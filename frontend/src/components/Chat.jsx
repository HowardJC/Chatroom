import React, {useState} from "react"
import io from "socket.io-client";
import Axios from "axios";
let endpoint = "http://localhost:5000";
let socket = io.connect(endpoint);

const Chat = () =>{

    const [messages,setMessages]=useState([]);
    const [message,setMessage]=useState("")

    socket.off("message")

/*
    socket.on("message", msg =>{
        setMessages([...messages,msg])});

*/

    const onChange=(event)=>{
        setMessage(event.target.value)

    }

    const onClick =() =>{
/*        socket.emit("message",message);*/
        setMessage("")
        Axios.post("http:/xd/localhost:3000/api/chat", {}, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`
            }
        }).then(res => {
        console.log("Lose")        })
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