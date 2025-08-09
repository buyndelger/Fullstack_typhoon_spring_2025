import React, {useState}from  "react"


type User ={
    id: number
    name: string
    email: string
}

const UserProfile: React.FC = ()=>{
    const [user, setUser]= useState<User>({
        id:1,
        name: "John Doe",
        email: "john.doe@example.com"
    });
    const handleNAmeChange=(event: React.ChangeEvent<HTMLInputElement>)=>{
        setUser({
            ...user,
            name: event.target.value
        })
    }

    return(
        <>
        <h2>User Profile</h2>
        <p>
            <strong>name:</strong> {user.name}
            <strong>Email:</strong> {user.email}
        </p>

        <input type="text" 
        value={user.name}
        onChange={handleNAmeChange}
        placeholder="Update name"
        />
        </>
    )
}
export default UserProfile;