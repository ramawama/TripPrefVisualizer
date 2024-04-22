const { app, BrowserWindow } = require("electron");
const { spawn } = require("child_process");
const kill = require("tree-kill");

let mainWindow;
let nextServerProcess = null;
let flaskServerProcess = null;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  const NEXT_URL = "http://localhost:3000";
  mainWindow.loadURL(NEXT_URL);

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

function startNextJsServer() {
  nextServerProcess = spawn("npm", ["run", "dev"], {
    cwd: "../client",
    shell: true,
  });

  nextServerProcess.stdout.on("data", (data) => {
    console.log(`Next.js: ${data}`);
  });

  nextServerProcess.stderr.on("data", (data) => {
    console.error(`Next.js error: ${data}`);
  });
}

function startFlaskServer() {
  // Adjust the path and commands according to your project setup
  flaskServerProcess = spawn("pipenv", ["run", "python", "server.py"], {
    cwd: "../server",
    shell: true,
  });

  flaskServerProcess.stdout.on("data", (data) => {
    console.log(`Flask: ${data}`);
  });

  flaskServerProcess.stderr.on("data", (data) => {
    console.error(`Flask error: ${data}`);
  });
}

app.whenReady().then(() => {
  startNextJsServer();
  startFlaskServer();
  createWindow();
});

app.on("window-all-closed", () => {
  if (nextServerProcess !== null) {
    kill(nextServerProcess.pid);
  }
  if (flaskServerProcess !== null) {
    kill(flaskServerProcess.pid);
  }
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

app.on("quit", () => {
  if (nextServerProcess !== null) {
    kill(nextServerProcess.pid);
  }
  if (flaskServerProcess !== null) {
    kill(flaskServerProcess.pid);
  }
});
