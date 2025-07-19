import Plot from "react-plotly.js";

const MainPage = () => {
    return (
        <div className="h-screen bg-orange-500 p-8 flex flex-col items-center justify-center">
            <h1 className="text-3xl font-bold text-white">¡Hola Tailwind CSS!</h1>
            <p className="mt-4 text-white">
                Tailwind CSS es increíblemente poderoso. ¡No puedo esperar para seguir explorándolo!
            </p>


            <div
                className="App"
                style={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    height: "100vh",
                }}
            >
                <Plot
                    data={[
                        {
                            x: [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18],
                            y: [32, 37, 40.5, 43, 49, 54, 59, 63.5, 69.5, 73, 74],
                            mode: "markers",
                            type: "scatter",
                        },
                    ]}
                    layout={{
                        title: "Growth Rate in Boys",
                        xaxis: {
                            title: "Age (years)",
                        },
                        yaxis: {
                            title: "Height (inches)",
                        },
                    }}
                />
            </div>
        </div>
    );
}

export default MainPage;
