const fs = require("fs");
const path = require("path");

const webpack = require("webpack");


function createWebpackConfig() {
    const environment = process.env.NODE_ENV || "development";
    const isDevelopment = environment === "development";
    const version = JSON.parse(fs.readFileSync("package.json", "utf-8")).version;
    const staticDir = path.resolve(__dirname, "server/static/server/");

    return {
        mode: environment,
        devtool: isDevelopment ? "nosources-source-map" : false,
        entry: {
            index: "./client/index.ts",
        },
        module: {
            rules: [
                // Rules (and individual loaders within rules) are executed in reverse order.
                // So the test-runner.ts is first passed to the test-runner-loader and then to the ts-loader.
                { test: /\.tsx?$/, use: "ts-loader", exclude: /node_modules/ },
            ],
        },
        output: {
            filename: "[name].js?[contenthash]",
            path: staticDir + "/js/",
        },
        plugins: [
            new webpack.DefinePlugin({
                __DEBUG__: JSON.stringify(isDevelopment),
                __VERSION__: JSON.stringify(version),
            }),
            new WatchStatusPlugin(),
        ],
        resolve: {
            extensions: [ ".js", ".ts", ".tsx" ],
        },
    };
}


class WatchStatusPlugin {
    constructor() {
        this._name = WatchStatusPlugin.name;
        this._isWatching = false;
    }

    apply(compiler) {
        compiler.hooks.invalid.tap(this._name, () => {
            process.stdout.write("\n" + new Date().toISOString() + " File change detected.\n");
        });
    }
}


module.exports = createWebpackConfig();
