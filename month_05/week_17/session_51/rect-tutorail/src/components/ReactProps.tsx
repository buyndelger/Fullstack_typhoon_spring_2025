import React from "react";
type Props={
    language: string
    name?: string
}
const Greeting: React.FC<Props> =(props)=>{
    console.log(props);
    
    return (
        <h1>
            {props.language}
            {props.name}
        </h1>
    )   
}

export default Greeting