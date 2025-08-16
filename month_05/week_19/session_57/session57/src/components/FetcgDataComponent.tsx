import React, { useEffect, useState } from "react";


export function PostsBad() {
    const [posts, setPosts] = useState < string > [] > ([]);
    useEffect(()=>{
    fetch("https://jsonlaceholder.typicode.com/posts?_limit=3")
        .then((result)=> result.json())
        .then((data)=>{
            console.log(data);
            setPosts(data.map((p:{title:string})=>p.title));
        });
    },[]);


    return (
        <>
            <ul>
                {posts.map((p, i) => (<li key={i}>{p}</li>))}

            </ul>

        </>
    )
}





