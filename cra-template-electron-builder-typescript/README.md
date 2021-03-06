# cra-template-electron-builder-typescript

This is a create-react-app (CRA) TypeScript template for Electron applications based on the [official TypeScript template for Create React App](https://github.com/facebook/create-react-app/tree/master/packages/cra-template-typescript).

## Getting Started

To create a React-Electron TypeScript application and run it in dev mode, run:

```
npx create-react-app my-app --template electron-builder-typescript
cd my-app
npm start
```

These commands will do the following:

1. Create a React-Electron TypeScript application called `my-app` using the CRA [electron-builder-typescript](https://www.npmjs.com/package/cra-template-electron-builder-typescript) template.
2. Change the current directory to `my-app`
3. Launch the application in dev mode, with hot reloading and the Developer tools console installed with [React DevTools extension](https://github.com/facebook/react/tree/master/packages/react-devtools-extensions)

For more information on how to use CRA, see the [Create React App docs](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app).

## Distribution

This template uses [electron-builder](https://www.electron.build/) to package and build a ready for distribution application for Windows, macOS and Linux.

To build the application, run:

```
npm run dist:win
npm run dist:mac
npm run dist:linux
```

These commands will generate distributables for Windows, macOS and Linux respectively.
By default, the distributables will be in NSIS (Windows), dmg (macOS) and deb (linux) form.

_Remember to change the author, description, build.appId and build.productName in `package.json` before creating a distributable_

## JavaScript

For creating an application without TypeScript, use the CRA [electron-builder](https://www.npmjs.com/package/cra-template-electron-builder) template.

```
npx create-react-app my-app --template electron-builder
cd my-app
npm start
```
