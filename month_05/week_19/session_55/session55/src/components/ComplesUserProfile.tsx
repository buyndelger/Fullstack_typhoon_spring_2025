// import React from "react";


// type State = {
//     name: string,
//     age: number,
//     address: {
//         city: string,
//         country: string
//     };
// };

// type Actoin =
//     | { type: "UPDATE_NAME", payload: string }
// | { type: "INCREMENT_AGE" }
// | { type: "UPDATE_CITY", payload: string };


// const userReducer = (state: State, action: Actoin): State => {
//     switch (action.type) {
//         case "UPDATE_NAME":
//             return { ...state, name: action.payload };

//         case "INCREMENT_AGE":
//             return{...state, age: state.age}
//         case "UPDATE_CITY":
//             return {
//                 ...state,
//                 address:{
//                 city:action.payload
//             },};
//             default:
//             return state;

//     }
// }

// const initialUserState: State={
//     name: "buynaa",
//     age: 22,
//     address: {city:" Ulaanbaatar", country:"Mongolia"}
// }

// const ComplesUserProfile: React.FC=()=>{
//     const [state, dispatch]= userReducer(userReducer, initialUserState);
//     return(
//         <>
//         <h3>Complex User profile</h3>
//         <p>
//         <strong>Name:</strong>{state.name}
//     </p>
//     <p>
//         <strong>Location:</strong>{state.age}
//     </p>
//     <p>
//         <strong>City:</strong>{state.address.city}
//     </p>
//         <hr />

//         <input type="text" 
//         placeholder="New Name"
//         onChange={(e)=>{
//             dispatch({
//                 type: "UPDATE_CITY",
//                payload: e.target.value 
//             })
//         }}/>
//         <button onClick={()=>dispatch({
//             type:"INCREMENT_AGE"
//         })}>
//             INCREMENT age
//         </button>
//         </>
//     ) 
// }

// export default ComplesUserProfile