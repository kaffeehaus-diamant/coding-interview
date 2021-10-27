import React from "react";
import ReactDOM from "react-dom";

export default (): void => {
    const container = document.getElementById("app");
    if (!container) {
        throw new Error("main app container does not exist");
    }

    ReactDOM.render(<App />, container);
};


class App extends React.Component {
    public render(): React.ReactNode {
        return <div>Hello World!</div>
    }
}
