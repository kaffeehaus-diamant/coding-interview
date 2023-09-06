import React from "react";
import {createRoot} from "react-dom/client";

export default (): void => {
    const container = document.getElementById("app");
    if (!container) {
        throw new Error("main app container does not exist");
    }

    const root = createRoot(container);
    root.render(<App />)
};


function App(): React.ReactElement {
    return (
        <React.Fragment>
            <Header />
            <Content />
        </React.Fragment>
    )
}

function Header(): React.ReactElement {
    return (
        <header className="navbar navbar-dark navbar-sticky bg-dark">
            <div className="container-fluid">
                <span className="navbar-brand">Foo</span>
            </div>
        </header>
    );
}

function Content(): React.ReactElement{
    return (
        <main className="container">
            <h1>Hello World!</h1>
        </main>
    );
}
