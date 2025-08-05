import React, { useState } from "react";

const ControlledInput: React.FC = () => {
  const [value, setValue] = useState<string>("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValue(event.currentTarget.value);
  };

  return (
    <>
      <h3>On Change Example</h3>
      <input
        type="text"
        placeholder="Type Something ..."
        value={value}
        onChange={handleInputChange}
      />
      <p>Current Value: {value}</p>
    </>
  );
};

export default ControlledInput;
