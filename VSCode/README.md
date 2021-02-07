# VS Code Setup

1.  Install the *Python* and *Pylance* extensions from Microsoft.

1.  Copy the `pyrightconfig.json` file from the `VSCode` folder into your `{OH_CONF}` folder:

    ```sh
    cp VSCode/pyrightconfig.json ../
    ```

1.  Copy the `.pylintrc` file from the `VSCode` folder into your `{OH_CONF}` folder.
    If you already have a `.pylintrc` file you will need to determine whether to keep your existing one or use the one provided here.

    ```sh
    cp VSCode/.pylintrc ../
    ```

    You will also need to install `pylint`, VSCode should prompt you to install it but if it does not you can install it with `pip`:

    ```sh
    pip3 install pylint
    ```

1.  Copy the `.vscode` directory from the `VSCode` folder into your `{OH_CONF}` folder.

    ```sh
    cp -R VSCode/.vscode ../
    ```

    If you already have a `.vscode/settings.json` file you may want to add some or all of the one provided here to your existing file.
    The following options are the ones required for getting type hints:

    ```json
    // Python Type Hints
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.stubPath": "./automation/typings",
    "python.autoComplete.extraPaths": [
        "./automation/lib/python"
    ],
    "python.analysis.extraPaths": [
        "./automation/lib/python"
    ]
    ```
