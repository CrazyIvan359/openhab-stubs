
# Installation

These instructions will guide you through copying a set of stubs and setting up your IDE to use them.
Follow the instructions below to copy the stubs, then jump to the section for your IDE.
You will need Python 3.6 or higher installed on the computer running your IDE.

* [Stubs](#Stubs)
* IDE Setup
  * [VS Code](VSCode/README.md)
  * [Eclipse](Eclipse/README.md)

## Stubs

First you will need to gather the correct stubs for the version of openHAB that you are running and get them copied into your openHAB `conf` directory.

1.  Choose a folder you want to put the stubs in, these instructions will use `{OH_CONF}/automation/typings/`.
    Create that folder now:

    ```sh
    mkdir ../automation/typings
    ```

    If your openHAB configuration is store in source control like Git, you may want to add this folder to your `.gitignore`:

    ```gitignore
    automation/typings/
    ```

1.  Copy the Java stubs into the folder you just created from the `Java` folder in this repo.
    Use `Java/8` for openHAB 2.x and `Java/11` for openHAB 3.x.

    ```sh
    cp -R Stubs/Java/11/* ../automation/typings/
    ```

    When copied correctly the folder structure should look like this:

    ```text
    typings
      |-- java
      |-- javax
    ```

1.  Copy the openHAB stubs for your version of openHAB.
    Not all versions of openHAB have had stubs generated for them; if you can't find your exact version, use the oldest version available that is **not older** than your version.
    If stubs are not available for your exact version you may find some small differences between openHAB and the stubs which may cause errors.

    Ex. if you are running OH3.0.1 and there are stubs for OH3.0.0 and OH3.0.2, use the stubs from OH3.0.2.

    ```sh
    cp -R Stubs/openHAB/OH3.0.0-Release/* ../automation/typings/
    ```

    When copied correctly the folder structure should now look like this:

    ```text
    typings
      |-- actions
      |-- java
      |-- javax
      |-- org
    ```

1.  If you are using the openHAB Scripters Helper Libraries, copy the stub files that came with them for the version of openHAB you are using into `{OH_CONF}/automation/typings/`.

1.  Follow the instructions for your IDE (links above) to complete the installation.
