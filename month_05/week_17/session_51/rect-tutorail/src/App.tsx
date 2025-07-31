import React from "react";
import Greeting from "./components/ReactProps";
import Gallerry from "./components/Gallery";
import TodoList from "./components/TodoList";


const App: React.FC = () => {

  const messages: string[]=['New eamil 1 ' ,'New eamil 2']
  const noMessages: string[] =[]
  
  return (
    <>
      <h1>Hello, Manual React and Typescript</h1>
      <div className="application">
    
      <TodoList/>
      </div>
    </>
  );
};

export default App;
