import React from "react";
import Profile from "./Profile";

const Gallerry :React.FC=()=>{
    return <>
    < Profile  width={150} height={150}
    url="https://i.imgur.com/osHTE0k.png"
    alternative="Poniy" />
  < Profile  width={150} height={150}
    url="https://i.imgur.com/osHTE0k.png"
    alternative="Poniy" />
     < Profile  width={150} height={150}
    url="https://i.imgur.com/osHTE0k.png"
    alternative="Poniy" />
    </>
}
export default Gallerry