import React, { useState } from "react";

type User = {
    id: number,
    name: string,
    age: number
};

const UserAge: React.FC = () => {
    const [user, setUser] = useState<User>({
        id: 1,
        name: "John Doe",
        age: 31
    }
    );
    const handleAgeChaneg = () => {
        setUser((preUser) => ({
            ...preUser,
            age: preUser.age + 1
        }));



    }
    return(<>
    <h2>User Age</h2>
    <p>
        <strong>Name:</strong>{user.name}
    </p>
    <p>
        <strong>Location:</strong>{user.age}
    </p>
    <button onClick={handleAgeChaneg}>Age Up by 1 </button>
    
    </>)

}
export default UserAge;