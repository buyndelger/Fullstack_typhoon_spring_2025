import React from "react";
type Props={
    width: number,
    height: number,
    url:string,
    alternative: string
}
const Profile :React.FC<Props>=(Props)=>{
    return <>
    <img src={Props.url}
     alt={Props.alternative}
    width={Props.width}
    height={Props.height}/>
    </>
}
export default Profile ;